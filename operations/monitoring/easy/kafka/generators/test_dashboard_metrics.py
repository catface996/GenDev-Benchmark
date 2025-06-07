#!/usr/bin/env python3
"""
Dashboard指标测试验证脚本
验证所有关键指标是否可以在Prometheus中查询到
"""

import requests
import json
import time

class DashboardMetricsValidator:
    def __init__(self, prometheus_url="http://localhost:9090"):
        self.prometheus_url = prometheus_url
        self.test_results = {}
    
    def query_prometheus(self, query):
        """查询Prometheus指标"""
        try:
            url = f"{self.prometheus_url}/api/v1/query"
            params = {"query": query}
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data["status"] == "success" and data["data"]["result"]:
                    return data["data"]["result"]
            return None
        except Exception as e:
            print(f"查询错误: {e}")
            return None
    
    def test_topic_metrics(self):
        """测试Topic相关指标"""
        print("🔍 测试Topic指标...")
        
        tests = {
            "Topic消息总数": 'sum by (topic) (kafka_topic_partition_current_offset{topic!~"__.*"})',
            "Topic分区数": 'kafka_topic_partitions{topic!~"__.*"}',
            "消息生产速率": 'sum by (topic) (rate(kafka_topic_partition_current_offset{topic!~"__.*"}[5m]))',
            "分区消息分布": 'kafka_topic_partition_current_offset{topic!~"__.*"}'
        }
        
        for test_name, query in tests.items():
            result = self.query_prometheus(query)
            if result:
                self.test_results[test_name] = "✅ 通过"
                print(f"  ✅ {test_name}: {len(result)} 个数据点")
            else:
                self.test_results[test_name] = "❌ 失败"
                print(f"  ❌ {test_name}: 无数据")
    
    def test_consumer_metrics(self):
        """测试Consumer相关指标"""
        print("\n🔍 测试Consumer指标...")
        
        tests = {
            "消费者积压": 'kafka_consumer_lag_messages',
            "消费者组积压汇总": 'sum by (consumer_group) (kafka_consumer_lag_messages)',
            "消费者当前偏移量": 'kafka_consumer_current_offset',
            "消费者日志结束偏移量": 'kafka_consumer_log_end_offset'
        }
        
        for test_name, query in tests.items():
            result = self.query_prometheus(query)
            if result:
                self.test_results[test_name] = "✅ 通过"
                print(f"  ✅ {test_name}: {len(result)} 个数据点")
            else:
                self.test_results[test_name] = "❌ 失败"
                print(f"  ❌ {test_name}: 无数据")
    
    def test_system_metrics(self):
        """测试系统相关指标"""
        print("\n🔍 测试系统指标...")
        
        tests = {
            "CPU使用率": '100 - (avg(irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)',
            "内存使用率": '(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100',
            "磁盘使用率": '(1 - (node_filesystem_avail_bytes{fstype!="tmpfs"} / node_filesystem_size_bytes{fstype!="tmpfs"})) * 100',
            "TCP连接数": 'node_netstat_Tcp_CurrEstab',
            "网络接收速率": 'rate(node_network_receive_bytes_total{device!="lo"}[5m])',
            "网络发送速率": 'rate(node_network_transmit_bytes_total{device!="lo"}[5m])',
            "磁盘读取速率": 'rate(node_disk_read_bytes_total[5m])',
            "磁盘写入速率": 'rate(node_disk_written_bytes_total[5m])'
        }
        
        for test_name, query in tests.items():
            result = self.query_prometheus(query)
            if result:
                self.test_results[test_name] = "✅ 通过"
                print(f"  ✅ {test_name}: {len(result)} 个数据点")
            else:
                self.test_results[test_name] = "⚠️  无数据"
                print(f"  ⚠️  {test_name}: 无数据 (可能需要node_exporter)")
    
    def test_jvm_metrics(self):
        """测试JVM相关指标"""
        print("\n🔍 测试JVM指标...")
        
        tests = {
            "JVM堆内存使用": 'jvm_memory_heap_used_bytes',
            "JVM堆内存最大": 'jvm_memory_heap_max_bytes',
            "JVM非堆内存使用": 'jvm_memory_nonheap_used_bytes',
            "JVM垃圾回收时间": 'rate(jvm_gc_collection_time_ms_total[5m])',
            "JVM垃圾回收次数": 'rate(jvm_gc_collection_count_total[5m])',
            "JVM当前线程数": 'jvm_threads_current',
            "JVM守护线程数": 'jvm_threads_daemon'
        }
        
        for test_name, query in tests.items():
            result = self.query_prometheus(query)
            if result:
                self.test_results[test_name] = "✅ 通过"
                print(f"  ✅ {test_name}: {len(result)} 个数据点")
            else:
                self.test_results[test_name] = "⚠️  无数据"
                print(f"  ⚠️  {test_name}: 无数据 (可能需要JMX Exporter)")
    
    def test_dashboard_queries(self):
        """测试Dashboard中的关键查询"""
        print("\n🔍 测试Dashboard关键查询...")
        
        dashboard_queries = {
            "集群总消息数": 'sum(kafka_topic_partition_current_offset{topic!~"__.*"})',
            "集群Topic数量": 'count by () (group by (topic) (kafka_topic_partitions{topic!~"__.*"}))',
            "集群消费者组数量": 'count by () (group by (consumer_group) (kafka_consumer_lag_messages))',
            "集群总积压": 'sum(kafka_consumer_lag_messages)',
            "集群生产速率": 'sum(rate(kafka_topic_partition_current_offset{topic!~"__.*"}[5m]))'
        }
        
        for test_name, query in dashboard_queries.items():
            result = self.query_prometheus(query)
            if result and len(result) > 0:
                value = result[0]["value"][1]
                self.test_results[test_name] = "✅ 通过"
                print(f"  ✅ {test_name}: {value}")
            else:
                self.test_results[test_name] = "❌ 失败"
                print(f"  ❌ {test_name}: 无数据")
    
    def generate_report(self):
        """生成测试报告"""
        print("\n" + "="*60)
        print("📊 Dashboard指标验证报告")
        print("="*60)
        
        passed = sum(1 for result in self.test_results.values() if "✅" in result)
        warning = sum(1 for result in self.test_results.values() if "⚠️" in result)
        failed = sum(1 for result in self.test_results.values() if "❌" in result)
        total = len(self.test_results)
        
        print(f"总测试项: {total}")
        print(f"✅ 通过: {passed}")
        print(f"⚠️  警告: {warning}")
        print(f"❌ 失败: {failed}")
        print(f"成功率: {(passed/total)*100:.1f}%")
        
        print("\n📋 详细结果:")
        for test_name, result in self.test_results.items():
            print(f"  {result} {test_name}")
        
        print("\n💡 建议:")
        if failed > 0:
            print("  • 检查Prometheus配置和targets状态")
            print("  • 确保所有exporter正常运行")
        if warning > 0:
            print("  • 考虑添加node_exporter获取系统指标")
            print("  • 考虑添加JMX exporter获取JVM指标")
        if passed == total:
            print("  • 🎉 所有指标正常，Dashboard可以正常使用！")
    
    def run_all_tests(self):
        """运行所有测试"""
        print("🚀 开始Dashboard指标验证...")
        print("="*60)
        
        self.test_topic_metrics()
        self.test_consumer_metrics()
        self.test_system_metrics()
        self.test_jvm_metrics()
        self.test_dashboard_queries()
        
        self.generate_report()

if __name__ == "__main__":
    validator = DashboardMetricsValidator()
    validator.run_all_tests()
