#!/usr/bin/env python3
"""
Kafka负载模拟器 - 生成各种类型的消息流量
用于测试监控Dashboard的各项指标
"""

import subprocess
import threading
import time
import random
import json
from datetime import datetime

class KafkaLoadSimulator:
    def __init__(self):
        self.running = True
        self.stats = {
            'messages_sent': 0,
            'bytes_sent': 0,
            'errors': 0
        }
    
    def generate_message(self, message_type="default", size="medium"):
        """生成不同类型和大小的消息"""
        timestamp = datetime.now().isoformat()
        
        if message_type == "json":
            if size == "small":
                message = {
                    "timestamp": timestamp,
                    "id": random.randint(1, 10000),
                    "status": random.choice(["active", "inactive", "pending"])
                }
            elif size == "large":
                message = {
                    "timestamp": timestamp,
                    "id": random.randint(1, 10000),
                    "user_id": random.randint(1000, 9999),
                    "event_type": random.choice(["login", "logout", "purchase", "view", "click"]),
                    "properties": {
                        "browser": random.choice(["Chrome", "Firefox", "Safari", "Edge"]),
                        "os": random.choice(["Windows", "macOS", "Linux", "iOS", "Android"]),
                        "location": random.choice(["US", "EU", "ASIA", "OTHER"]),
                        "session_id": f"sess_{random.randint(100000, 999999)}",
                        "ip_address": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
                    },
                    "metadata": {
                        "version": "1.0",
                        "source": "web_app",
                        "processed": False,
                        "tags": [f"tag_{i}" for i in range(random.randint(1, 5))]
                    },
                    "payload": "x" * random.randint(100, 500)  # 随机填充数据
                }
            else:  # medium
                message = {
                    "timestamp": timestamp,
                    "id": random.randint(1, 10000),
                    "user_id": random.randint(1000, 9999),
                    "event": random.choice(["order", "payment", "shipment", "delivery"]),
                    "amount": round(random.uniform(10.0, 1000.0), 2),
                    "currency": random.choice(["USD", "EUR", "GBP", "JPY"]),
                    "data": "x" * random.randint(50, 200)
                }
            return json.dumps(message)
        
        elif message_type == "log":
            log_levels = ["INFO", "WARN", "ERROR", "DEBUG"]
            components = ["auth-service", "payment-service", "order-service", "notification-service"]
            
            if size == "large":
                stack_trace = "\n".join([f"    at com.example.service.Class{i}.method{i}(Class{i}.java:{random.randint(10,200)})" 
                                       for i in range(random.randint(5, 15))])
                message = f"[{timestamp}] {random.choice(log_levels)} {random.choice(components)} - Error processing request: {random.choice(['NullPointerException', 'TimeoutException', 'DatabaseConnectionException'])}\nStack trace:\n{stack_trace}\nAdditional context: {{'request_id': '{random.randint(100000, 999999)}', 'user_id': '{random.randint(1000, 9999)}', 'session': 'sess_{random.randint(100000, 999999)}'}}"
            else:
                message = f"[{timestamp}] {random.choice(log_levels)} {random.choice(components)} - {random.choice(['Request processed successfully', 'User authenticated', 'Payment completed', 'Order created', 'Notification sent'])} (duration: {random.randint(10, 500)}ms)"
            
            return message
        
        else:  # simple text
            if size == "large":
                return f"Message-{random.randint(1, 10000)}-{timestamp}-{'x' * random.randint(200, 1000)}"
            elif size == "small":
                return f"Msg-{random.randint(1, 1000)}-{timestamp}"
            else:
                return f"Message-{random.randint(1, 10000)}-{timestamp}-{'data' * random.randint(5, 20)}"
    
    def send_message(self, topic, message):
        """发送消息到Kafka"""
        try:
            cmd = ['docker', 'exec', '-i', 'kafka', 'kafka-console-producer', 
                   '--topic', topic, '--bootstrap-server', 'localhost:9092']
            
            process = subprocess.Popen(cmd, stdin=subprocess.PIPE, 
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
                                     text=True)
            
            stdout, stderr = process.communicate(input=message, timeout=5)
            
            if process.returncode == 0:
                self.stats['messages_sent'] += 1
                self.stats['bytes_sent'] += len(message.encode('utf-8'))
                return True
            else:
                self.stats['errors'] += 1
                return False
                
        except Exception as e:
            self.stats['errors'] += 1
            return False
    
    def high_throughput_producer(self):
        """高吞吐量生产者 - 快速发送大量小消息"""
        print("🚀 启动高吞吐量生产者...")
        while self.running:
            try:
                # 批量发送小消息
                for _ in range(random.randint(5, 15)):
                    message = self.generate_message("json", "small")
                    self.send_message("high-throughput", message)
                
                time.sleep(random.uniform(0.1, 0.5))  # 短间隔
            except Exception as e:
                print(f"高吞吐量生产者错误: {e}")
                time.sleep(1)
    
    def medium_load_producer(self):
        """中等负载生产者 - 稳定发送中等大小消息"""
        print("📊 启动中等负载生产者...")
        while self.running:
            try:
                message = self.generate_message("json", "medium")
                self.send_message("medium-load", message)
                time.sleep(random.uniform(1, 3))  # 中等间隔
            except Exception as e:
                print(f"中等负载生产者错误: {e}")
                time.sleep(2)
    
    def low_latency_producer(self):
        """低延迟生产者 - 频繁发送小消息"""
        print("⚡ 启动低延迟生产者...")
        while self.running:
            try:
                message = self.generate_message("text", "small")
                self.send_message("low-latency", message)
                time.sleep(random.uniform(0.05, 0.2))  # 很短间隔
            except Exception as e:
                print(f"低延迟生产者错误: {e}")
                time.sleep(0.5)
    
    def batch_processing_producer(self):
        """批处理生产者 - 间歇性发送大消息"""
        print("📦 启动批处理生产者...")
        while self.running:
            try:
                # 发送一批大消息
                batch_size = random.randint(3, 8)
                for _ in range(batch_size):
                    message_type = random.choice(["json", "log"])
                    message = self.generate_message(message_type, "large")
                    self.send_message("batch-processing", message)
                    time.sleep(0.1)  # 批内短间隔
                
                time.sleep(random.uniform(5, 15))  # 批间长间隔
            except Exception as e:
                print(f"批处理生产者错误: {e}")
                time.sleep(5)
    
    def performance_test_producer(self):
        """性能测试生产者 - 向现有Topic发送消息"""
        print("🔥 启动性能测试生产者...")
        while self.running:
            try:
                message_type = random.choice(["json", "log", "text"])
                size = random.choice(["small", "medium", "large"])
                message = self.generate_message(message_type, size)
                self.send_message("performance-test", message)
                time.sleep(random.uniform(0.5, 2))
            except Exception as e:
                print(f"性能测试生产者错误: {e}")
                time.sleep(1)
    
    def stats_reporter(self):
        """统计报告器"""
        print("📈 启动统计报告器...")
        last_messages = 0
        last_bytes = 0
        
        while self.running:
            time.sleep(10)  # 每10秒报告一次
            
            current_messages = self.stats['messages_sent']
            current_bytes = self.stats['bytes_sent']
            
            msg_rate = (current_messages - last_messages) / 10
            byte_rate = (current_bytes - last_bytes) / 10
            
            print(f"📊 统计报告 - 消息: {current_messages} (+{msg_rate:.1f}/s), "
                  f"字节: {current_bytes} (+{byte_rate:.1f}B/s), "
                  f"错误: {self.stats['errors']}")
            
            last_messages = current_messages
            last_bytes = current_bytes
    
    def start_simulation(self, duration_minutes=30):
        """启动负载模拟"""
        print(f"🎯 开始Kafka负载模拟 (持续 {duration_minutes} 分钟)")
        print("=" * 50)
        
        # 启动所有生产者线程
        threads = [
            threading.Thread(target=self.high_throughput_producer, daemon=True),
            threading.Thread(target=self.medium_load_producer, daemon=True),
            threading.Thread(target=self.low_latency_producer, daemon=True),
            threading.Thread(target=self.batch_processing_producer, daemon=True),
            threading.Thread(target=self.performance_test_producer, daemon=True),
            threading.Thread(target=self.stats_reporter, daemon=True)
        ]
        
        for thread in threads:
            thread.start()
        
        try:
            # 运行指定时间
            time.sleep(duration_minutes * 60)
        except KeyboardInterrupt:
            print("\n⏹️  收到中断信号，正在停止...")
        
        self.running = False
        print(f"\n✅ 负载模拟完成!")
        print(f"📊 最终统计: 消息 {self.stats['messages_sent']}, "
              f"字节 {self.stats['bytes_sent']}, 错误 {self.stats['errors']}")

if __name__ == "__main__":
    simulator = KafkaLoadSimulator()
    
    # 运行5分钟的负载测试
    simulator.start_simulation(duration_minutes=5)
