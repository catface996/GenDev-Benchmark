#!/usr/bin/env python3
"""
Kafka Consumer Lag Exporter for Prometheus
自定义的Kafka消费者积压指标导出器

使用方法:
1. 确保Docker环境中的Kafka容器名为 'kafka'
2. 运行: python3 kafka_consumer_lag_monitor.py
3. 访问: http://localhost:9309/metrics

依赖: 需要Docker环境
"""

import subprocess
import json
import time
import re
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import threading

class KafkaLagExporter:
    def __init__(self, kafka_container_name='kafka'):
        self.metrics = {}
        self.kafka_container = kafka_container_name
        self.last_update = 0
        self.cache_duration = 30  # 缓存30秒
    
    def get_consumer_groups(self):
        """获取所有消费者组"""
        try:
            result = subprocess.run([
                'docker', 'exec', self.kafka_container, 
                'kafka-consumer-groups', '--bootstrap-server', 'localhost:9092', '--list'
            ], capture_output=True, text=True, check=True, timeout=10)
            
            groups = [g.strip() for g in result.stdout.strip().split('\n') if g.strip()]
            return [g for g in groups if not g.startswith('console-consumer-')]
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return []
    
    def get_consumer_group_lag(self, group_name):
        """获取特定消费者组的积压信息"""
        try:
            result = subprocess.run([
                'docker', 'exec', self.kafka_container,
                'kafka-consumer-groups', '--bootstrap-server', 'localhost:9092',
                '--describe', '--group', group_name
            ], capture_output=True, text=True, check=True, timeout=10)
            
            lines = result.stdout.strip().split('\n')
            lag_info = []
            
            for line in lines[1:]:  # 跳过标题行
                if line.strip() and not line.startswith('GROUP'):
                    parts = line.split()
                    if len(parts) >= 6:
                        try:
                            topic = parts[1]
                            partition = parts[2]
                            current_offset = int(parts[3]) if parts[3].isdigit() else 0
                            log_end_offset = int(parts[4]) if parts[4].isdigit() else 0
                            lag = int(parts[5]) if parts[5].isdigit() else 0
                            
                            lag_info.append({
                                'topic': topic,
                                'partition': partition,
                                'current_offset': current_offset,
                                'log_end_offset': log_end_offset,
                                'lag': lag,
                                'consumer_group': group_name
                            })
                        except (ValueError, IndexError):
                            continue
            
            return lag_info
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return []
    
    def collect_metrics(self):
        """收集所有指标"""
        current_time = time.time()
        
        # 使用缓存避免频繁查询
        if current_time - self.last_update < self.cache_duration:
            return
        
        self.metrics = {}
        consumer_groups = self.get_consumer_groups()
        
        for group in consumer_groups:
            if group.strip():
                lag_info = self.get_consumer_group_lag(group.strip())
                for info in lag_info:
                    key = f"{info['consumer_group']}_{info['topic']}_{info['partition']}"
                    self.metrics[key] = info
        
        self.last_update = current_time
    
    def generate_prometheus_metrics(self):
        """生成Prometheus格式的指标"""
        self.collect_metrics()
        
        output = []
        
        # Consumer Lag Messages
        output.append("# HELP kafka_consumer_lag_messages Consumer lag in messages")
        output.append("# TYPE kafka_consumer_lag_messages gauge")
        
        for key, info in self.metrics.items():
            labels = f'topic="{info["topic"]}",partition="{info["partition"]}",consumer_group="{info["consumer_group"]}"'
            output.append(f'kafka_consumer_lag_messages{{{labels}}} {info["lag"]}')
        
        output.append("")
        
        # Consumer Current Offset
        output.append("# HELP kafka_consumer_current_offset Current offset of consumer")
        output.append("# TYPE kafka_consumer_current_offset gauge")
        
        for key, info in self.metrics.items():
            labels = f'topic="{info["topic"]}",partition="{info["partition"]}",consumer_group="{info["consumer_group"]}"'
            output.append(f'kafka_consumer_current_offset{{{labels}}} {info["current_offset"]}')
        
        output.append("")
        
        # Log End Offset
        output.append("# HELP kafka_consumer_log_end_offset Log end offset")
        output.append("# TYPE kafka_consumer_log_end_offset gauge")
        
        for key, info in self.metrics.items():
            labels = f'topic="{info["topic"]}",partition="{info["partition"]}",consumer_group="{info["consumer_group"]}"'
            output.append(f'kafka_consumer_log_end_offset{{{labels}}} {info["log_end_offset"]}')
        
        # 添加统计信息
        output.append("")
        output.append("# HELP kafka_consumer_groups_total Total number of consumer groups")
        output.append("# TYPE kafka_consumer_groups_total gauge")
        
        unique_groups = set(info['consumer_group'] for info in self.metrics.values())
        output.append(f'kafka_consumer_groups_total {len(unique_groups)}')
        
        return '\n'.join(output)

class MetricsHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, exporter=None, **kwargs):
        self.exporter = exporter
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        if self.path == '/metrics':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            
            try:
                metrics = self.exporter.generate_prometheus_metrics()
                self.wfile.write(metrics.encode('utf-8'))
            except Exception as e:
                error_msg = f"# Error generating metrics: {str(e)}\n"
                self.wfile.write(error_msg.encode('utf-8'))
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            health_info = {
                "status": "healthy",
                "timestamp": time.time(),
                "metrics_count": len(self.exporter.metrics)
            }
            self.wfile.write(json.dumps(health_info).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')
    
    def log_message(self, format, *args):
        # 只记录错误日志
        if '404' in str(args) or '500' in str(args):
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {format % args}")

def run_server(port=9309, kafka_container='kafka'):
    exporter = KafkaLagExporter(kafka_container)
    
    def handler(*args, **kwargs):
        return MetricsHandler(*args, exporter=exporter, **kwargs)
    
    server = HTTPServer(('0.0.0.0', port), handler)
    print(f"🚀 Kafka Consumer Lag Exporter 启动在端口 {port}")
    print(f"📊 访问 http://localhost:{port}/metrics 查看指标")
    print(f"🏥 访问 http://localhost:{port}/health 查看健康状态")
    print(f"🐳 监控Kafka容器: {kafka_container}")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n⏹️  服务器已停止")
        server.server_close()

if __name__ == '__main__':
    import sys
    
    # 支持命令行参数
    port = 9309
    kafka_container = 'kafka'
    
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("错误: 端口号必须是数字")
            sys.exit(1)
    
    if len(sys.argv) > 2:
        kafka_container = sys.argv[2]
    
    run_server(port, kafka_container)
