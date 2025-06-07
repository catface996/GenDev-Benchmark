# Kafka增强监控指南

## 🎯 概述

这个增强版监控方案包含了完整的Kafka Broker指标，涵盖：
- **IO指标**: 字节流量、消息流量
- **连接指标**: 活跃连接数、连接趋势
- **性能指标**: 请求处理时间、请求速率
- **JVM指标**: 内存使用、垃圾回收、线程
- **Topic指标**: 消息数、分区信息
- **消费者指标**: 积压情况、消费进度

## 🚀 快速部署

### 方法1: 一键部署
```bash
cd ~/Desktop/Kafka
./deploy-enhanced-monitoring.sh
```

### 方法2: 手动部署
```bash
# 1. 启动增强监控服务
docker-compose -f kafka-enhanced-compose.yml up -d

# 2. 启动消费者积压监控
python3 kafka_consumer_lag_monitor.py &

# 3. 验证服务
curl http://localhost:8080/metrics | grep kafka_server
```

## 📊 监控端点

| 服务 | 端口 | 用途 | 访问地址 |
|------|------|------|----------|
| Kafka | 9092 | Kafka服务 | localhost:9092 |
| JMX Exporter | 8080 | JMX指标 | http://localhost:8080/metrics |
| Kafka Exporter | 9308 | Topic指标 | http://localhost:9308/metrics |
| Prometheus | 9090 | 指标存储 | http://localhost:9090 |
| Consumer Lag | 9309 | 消费者积压 | http://localhost:9309/metrics |

## 📈 Dashboard面板说明

### 第一行: 关键统计 (4个Stat面板)
1. **Topic总数** - 集群中的Topic数量
2. **总消息数** - 所有Topic的消息总数
3. **活跃连接数** - 当前活跃的客户端连接
4. **JVM堆内存使用** - Java堆内存使用量

### 第二行: IO指标 (2个时间序列)
5. **网络IO - 字节流量** - 字节输入/输出速率
6. **消息IO - 消息流量** - 消息输入速率

### 第三行: 请求指标 (2个时间序列)
7. **请求处理时间** - 各类请求的平均和99分位处理时间
8. **请求速率** - 各类请求的处理速率

### 第四行: 连接和JVM (2个时间序列)
9. **连接数趋势** - 连接数变化趋势
10. **JVM内存使用** - 堆内存和非堆内存使用情况

### 第五行: Topic详情 (1个表格)
11. **Topic详细信息** - 包含消息数、分区数、流量等

### 第六行: GC和线程 (2个时间序列)
12. **垃圾回收** - GC次数和时间
13. **JVM线程** - 线程数量统计

### 第七行: 消费者监控 (1个时间序列)
14. **消费者积压趋势** - 各消费者组的积压变化

## 🔍 关键指标说明

### IO指标
```promql
# 字节输入速率
rate(kafka_server_bytes_in_total[5m])

# 字节输出速率  
rate(kafka_server_bytes_out_total[5m])

# 消息输入速率
rate(kafka_server_messages_in_total[5m])
```

### 连接指标
```promql
# 活跃连接数
kafka_server_connection_count

# 按监听器分组的连接数
sum by (listener) (kafka_server_connection_count)
```

### 性能指标
```promql
# 请求处理平均时间
kafka_network_request_total_time_ms_mean

# 请求处理99分位时间
kafka_network_request_total_time_ms_99p

# 请求速率
rate(kafka_network_request_total[5m])
```

### JVM指标
```promql
# 堆内存使用
jvm_memory_heap_used_bytes

# 非堆内存使用
jvm_memory_nonheap_used_bytes

# GC次数
rate(jvm_gc_collection_count_total[5m])

# GC时间
rate(jvm_gc_collection_time_ms_total[5m])

# 线程数
jvm_threads_current
```

## 🚨 告警建议

### 性能告警
```promql
# 请求处理时间过长 (>100ms)
kafka_network_request_total_time_ms_mean > 100

# 连接数过多 (>1000)
sum(kafka_server_connection_count) > 1000

# 堆内存使用率过高 (>80%)
(jvm_memory_heap_used_bytes / jvm_memory_heap_max_bytes) * 100 > 80
```

### IO告警
```promql
# 字节输入速率异常高 (>100MB/s)
rate(kafka_server_bytes_in_total[5m]) > 100000000

# 消息积压严重 (>1000条)
sum by (consumer_group) (kafka_consumer_lag_messages) > 1000
```

## 🔧 故障排查

### 常见问题

#### 1. JMX指标无数据
**症状**: Dashboard中JVM、IO指标显示"No data"
**解决**:
```bash
# 检查JMX Exporter是否正常
curl http://localhost:8080/metrics | grep kafka_server

# 检查Kafka JMX配置
docker exec kafka env | grep JMX

# 重启Kafka容器
docker-compose -f kafka-enhanced-compose.yml restart kafka
```

#### 2. 连接数指标异常
**症状**: 连接数显示为0或异常值
**解决**:
```bash
# 检查网络监听器配置
docker exec kafka kafka-configs --bootstrap-server localhost:9092 --describe --entity-type brokers --entity-name 1

# 查看实际连接
docker exec kafka netstat -an | grep :9092
```

#### 3. IO指标不准确
**症状**: 字节流量显示异常
**解决**:
```bash
# 检查Topic流量
docker exec kafka kafka-run-class kafka.tools.JmxTool --object-name kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec --jmx-url service:jmx:rmi:///jndi/rmi://localhost:9101/jmxrmi
```

## 📊 性能基准

### 正常指标范围
- **连接数**: < 1000 (取决于客户端数量)
- **请求处理时间**: < 50ms (平均)
- **堆内存使用率**: < 70%
- **GC频率**: < 1次/秒
- **字节流量**: 取决于业务需求

### 性能优化建议
1. **连接池**: 使用连接池减少连接数
2. **批处理**: 增加批处理大小提高吞吐量
3. **内存调优**: 根据堆内存使用情况调整JVM参数
4. **网络优化**: 调整网络缓冲区大小

## 🎨 Dashboard自定义

### 添加新面板
1. 点击Dashboard右上角的"Add panel"
2. 选择可视化类型
3. 配置Prometheus查询
4. 设置面板标题和样式

### 常用自定义查询
```promql
# Topic消息增长率
increase(kafka_topic_partition_current_offset[1h])

# 分区Leader分布
kafka_topic_partition_leader

# 副本同步状态
kafka_topic_partition_in_sync_replica

# 请求队列大小
kafka_network_request_queue_size

# 磁盘使用情况
kafka_log_size_bytes
```

## 📝 维护建议

### 日常检查
- 监控连接数趋势
- 检查GC频率和时间
- 观察IO流量模式
- 关注消费者积压情况

### 定期维护
- 清理旧的监控数据
- 更新告警阈值
- 优化Dashboard布局
- 备份监控配置

## 🔗 相关资源

- [Kafka JMX指标文档](https://kafka.apache.org/documentation/#monitoring)
- [Prometheus查询语法](https://prometheus.io/docs/prometheus/latest/querying/)
- [Grafana面板配置](https://grafana.com/docs/grafana/latest/panels/)

---

完成以上配置后，你将拥有一个功能完整的Kafka增强监控系统！
