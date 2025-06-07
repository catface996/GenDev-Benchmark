# 📊 Kafka Topic Prometheus 查询指令大全

## 🎯 测试环境概览
- **Topic总数**: 11个 (test-topic + topic-1 到 topic-10)
- **分区配置**: 每个新topic有3个分区，test-topic有1个分区
- **消息分布**: 各topic包含不同数量的消息 (25-300条)

## 📈 基础查询指令

### 1. 查看所有Topic的分区数
```promql
kafka_topic_partitions
```

### 2. 查看所有Topic的消息总数
```promql
sum by (topic) (kafka_topic_partition_current_offset)
```

### 3. 查看特定Topic的消息数
```promql
sum by (topic) (kafka_topic_partition_current_offset{topic="topic-8"})
```

### 4. 查看所有Topic的分区详细信息
```promql
kafka_topic_partition_current_offset
```

### 5. 查看Topic的最旧Offset
```promql
kafka_topic_partition_oldest_offset
```

## 🔍 高级聚合查询

### 6. 计算集群中的消息总数
```promql
sum(kafka_topic_partition_current_offset)
```

### 7. 计算每个Topic的平均分区消息数
```promql
sum by (topic) (kafka_topic_partition_current_offset) / sum by (topic) (kafka_topic_partitions)
```

### 8. 查找消息数最多的Topic
```promql
topk(5, sum by (topic) (kafka_topic_partition_current_offset))
```

### 9. 查找消息数最少的Topic
```promql
bottomk(5, sum by (topic) (kafka_topic_partition_current_offset))
```

### 10. 计算Topic总数
```promql
count by () (group by (topic) (kafka_topic_partitions))
```

## 📊 监控和告警查询

### 11. 检查Topic健康状态 (无未充分复制的分区)
```promql
kafka_topic_partition_under_replicated_partition == 0
```

### 12. 查看同步副本数
```promql
kafka_topic_partition_in_sync_replica
```

### 13. 检查分区Leader分布
```promql
kafka_topic_partition_leader
```

### 14. 消息增长率 (每秒新增消息数)
```promql
rate(kafka_topic_partition_current_offset[5m])
```

### 15. 检查是否使用首选Leader
```promql
kafka_topic_partition_leader_is_preferred
```

## 🎯 实用业务查询

### 16. 查看大于100条消息的Topic
```promql
sum by (topic) (kafka_topic_partition_current_offset) > 100
```

### 17. 查看小于50条消息的Topic
```promql
sum by (topic) (kafka_topic_partition_current_offset) < 50
```

### 18. 计算Topic消息数的百分位数
```promql
histogram_quantile(0.95, sum by (topic) (kafka_topic_partition_current_offset))
```

### 19. 查看每个分区的消息分布
```promql
kafka_topic_partition_current_offset{topic=~"topic-.*"}
```

### 20. 监控Topic消息积压 (当前offset - 最旧offset)
```promql
kafka_topic_partition_current_offset - kafka_topic_partition_oldest_offset
```

## 📋 当前测试数据概览

| Topic      | 分区数 | 消息总数 | 平均每分区 |
|------------|--------|----------|------------|
| test-topic | 1      | 1        | 1.0        |
| topic-1    | 3      | 50       | 16.7       |
| topic-2    | 3      | 100      | 33.3       |
| topic-3    | 3      | 25       | 8.3        |
| topic-4    | 3      | 200      | 66.7       |
| topic-5    | 3      | 75       | 25.0       |
| topic-6    | 3      | 150      | 50.0       |
| topic-7    | 3      | 30       | 10.0       |
| topic-8    | 3      | 300      | 100.0      |
| topic-9    | 3      | 80       | 26.7       |
| topic-10   | 3      | 120      | 40.0       |

## 🚀 在Grafana中使用

1. 在Grafana中添加Prometheus数据源: `http://prometheus:9090`
2. 创建新的Dashboard
3. 使用上述查询创建各种图表和面板
4. 设置告警规则监控关键指标

## 💡 实时测试命令

```bash
# 查看实时Topic消息数
curl -s "http://localhost:9090/api/v1/query?query=sum%20by%20(topic)%20(kafka_topic_partition_current_offset)" | python3 -m json.tool

# 查看Topic分区数
curl -s "http://localhost:9090/api/v1/query?query=kafka_topic_partitions" | python3 -m json.tool

# 查看集群总消息数
curl -s "http://localhost:9090/api/v1/query?query=sum(kafka_topic_partition_current_offset)" | python3 -m json.tool
```
