#!/usr/bin/env python3
"""
Kafka Consumer Lag Exporter for Prometheus
自定义的Kafka消费者积压指标导出器
"""

import subprocess
import json
import time
import re
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

class KafkaLagExporter:
    def __init__(self):
        self.metrics = {}
    
    def get_consumer_groups(self):
        """获取所有消费者组"""
        try:
            result = subprocess.run([
                'docker', 'exec', 'kafka', 
                'kafka-consumer-groups', '--bootstrap-server', 'localhost:9092', '--list'
            ], capture_output=True, text=True, check=True)
            return result.stdout.strip().split('\n')
        except subprocess.CalledProcessError:
            return []
    
    def get_consumer_group_lag(self, group_name):
        """获取特定消费者组的积压信息"""
        try:
            result = subprocess.run([
                'docker', 'exec', 'kafka',
                'kafka-consumer-groups', '--bootstrap-server', 'localhost:9092',
                '--describe', '--group', group_name
            ], capture_output=True, text=True, check=True)
            
            lines = result.stdout.strip().split('\n')
            lag_info = []
            
            for line in lines[1:]:  # 跳过标题行
                if line.strip() and 'topic-1' in line:
                    parts = line.split()
                    if len(parts) >= 6:
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
            
            return lag_info
        except subprocess.CalledProcessError:
            return []
    
    def collect_metrics(self):
        """收集所有指标"""
        self.metrics = {}
        consumer_groups = self.get_consumer_groups()
        
        for group in consumer_groups:
            if group.strip():
                lag_info = self.get_consumer_group_lag(group.strip())
                for info in lag_info:
                    if info['topic'] == 'topic-1':
                        key = f"{info['consumer_group']}_{info['partition']}"
                        self.metrics[key] = info
    
    def generate_prometheus_metrics(self):
        """生成Prometheus格式的指标"""
        self.collect_metrics()
        
        output = []
        output.append("# HELP kafka_consumer_lag_messages Consumer lag in messages")
        output.append("# TYPE kafka_consumer_lag_messages gauge")
        
        for key, info in self.metrics.items():
            labels = f'topic="{info["topic"]}",partition="{info["partition"]}",consumer_group="{info["consumer_group"]}"'
            output.append(f'kafka_consumer_lag_messages{{{labels}}} {info["lag"]}')
        
        output.append("")
        output.append("# HELP kafka_consumer_current_offset Current offset of consumer")
        output.append("# TYPE kafka_consumer_current_offset gauge")
        
        for key, info in self.metrics.items():
            labels = f'topic="{info["topic"]}",partition="{info["partition"]}",consumer_group="{info["consumer_group"]}"'
            output.append(f'kafka_consumer_current_offset{{{labels}}} {info["current_offset"]}')
        
        output.append("")
        output.append("# HELP kafka_consumer_log_end_offset Log end offset")
        output.append("# TYPE kafka_consumer_log_end_offset gauge")
        
        for key, info in self.metrics.items():
            labels = f'topic="{info["topic"]}",partition="{info["partition"]}",consumer_group="{info["consumer_group"]}"'
            output.append(f'kafka_consumer_log_end_offset{{{labels}}} {info["log_end_offset"]}')
        
        return '\n'.join(output)

class MetricsHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, exporter=None, **kwargs):
        self.exporter = exporter
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        if self.path == '/metrics':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            metrics = self.exporter.generate_prometheus_metrics()
            self.wfile.write(metrics.encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        pass  # 禁用日志输出

def run_server():
    exporter = KafkaLagExporter()
    
    def handler(*args, **kwargs):
        return MetricsHandler(*args, exporter=exporter, **kwargs)
    
    server = HTTPServer(('0.0.0.0', 9309), handler)
    print("🚀 Kafka Consumer Lag Exporter 启动在端口 9309")
    print("📊 访问 http://localhost:9309/metrics 查看指标")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n⏹️  服务器已停止")
        server.server_close()

if __name__ == '__main__':
    run_server()
