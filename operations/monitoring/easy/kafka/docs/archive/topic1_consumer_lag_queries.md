# 📊 Topic-1 消费者积压监控 - Prometheus 查询指南

## 🎯 当前积压情况概览

### 消费者组状态
| 消费者组 | 状态 | 总积压 | 描述 |
|----------|------|--------|------|
| consumer-group-1 | 🟢 活跃 | 0条 | 已消费完所有消息 |
| consumer-group-2 | 🔴 非活跃 | 100条 | 从头开始积压 |
| consumer-group-3 | 🔴 非活跃 | 70条 | 从offset 10开始积压 |

### 分区详细积压情况
| 消费者组 | 分区0 | 分区1 | 分区2 | 总计 |
|----------|-------|-------|-------|------|
| consumer-group-1 | 0 | 0 | 0 | 0 |
| consumer-group-2 | 32 | 30 | 38 | 100 |
| consumer-group-3 | 22 | 20 | 28 | 70 |

## 🔍 Prometheus 查询指令

### 1. 查看Topic-1所有消费者的积压情况
```promql
kafka_consumer_lag_messages{topic="topic-1"}
```

### 2. 按消费者组聚合总积压
```promql
sum by (consumer_group) (kafka_consumer_lag_messages{topic="topic-1"})
```

### 3. 查看特定消费者组的积压
```promql
kafka_consumer_lag_messages{topic="topic-1", consumer_group="consumer-group-2"}
```

### 4. 查看积压最严重的消费者组
```promql
topk(3, sum by (consumer_group) (kafka_consumer_lag_messages{topic="topic-1"}))
```

### 5. 查看无积压的消费者组
```promql
sum by (consumer_group) (kafka_consumer_lag_messages{topic="topic-1"}) == 0
```

### 6. 查看有积压的消费者组
```promql
sum by (consumer_group) (kafka_consumer_lag_messages{topic="topic-1"}) > 0
```

### 7. 查看积压超过50条的消费者组
```promql
sum by (consumer_group) (kafka_consumer_lag_messages{topic="topic-1"}) > 50
```

### 8. 查看每个分区的积压情况
```promql
kafka_consumer_lag_messages{topic="topic-1", partition="0"}
```

### 9. 查看消费者当前offset
```promql
kafka_consumer_current_offset{topic="topic-1"}
```

### 10. 查看Topic-1的最新offset
```promql
kafka_consumer_log_end_offset{topic="topic-1"}
```

## 📈 高级监控查询

### 11. 计算消费进度百分比
```promql
(kafka_consumer_current_offset{topic="topic-1"} / kafka_consumer_log_end_offset{topic="topic-1"}) * 100
```

### 12. 查看积压率 (积压/总消息数)
```promql
(kafka_consumer_lag_messages{topic="topic-1"} / kafka_consumer_log_end_offset{topic="topic-1"}) * 100
```

### 13. 监控积压变化趋势 (5分钟内的变化)
```promql
increase(kafka_consumer_lag_messages{topic="topic-1"}[5m])
```

### 14. 查看平均每分区积压
```promql
avg by (consumer_group) (kafka_consumer_lag_messages{topic="topic-1"})
```

### 15. 查看积压分布的标准差
```promql
stddev by (consumer_group) (kafka_consumer_lag_messages{topic="topic-1"})
```

## 🚨 告警规则建议

### 16. 积压超过阈值告警
```promql
sum by (consumer_group) (kafka_consumer_lag_messages{topic="topic-1"}) > 50
```

### 17. 消费者组无活动告警 (积压持续增长)
```promql
increase(kafka_consumer_lag_messages{topic="topic-1"}[10m]) > 0
```

### 18. 分区积压不均衡告警
```promql
(max by (consumer_group) (kafka_consumer_lag_messages{topic="topic-1"}) - min by (consumer_group) (kafka_consumer_lag_messages{topic="topic-1"})) > 20
```

## 📊 实时查询示例

### 当前积压情况查询
```bash
# 查看所有消费者组的积压
curl -s "http://localhost:9090/api/v1/query?query=sum%20by%20(consumer_group)%20(kafka_consumer_lag_messages%7Btopic%3D%22topic-1%22%7D)"

# 查看积压最多的消费者组
curl -s "http://localhost:9090/api/v1/query?query=topk(3,%20sum%20by%20(consumer_group)%20(kafka_consumer_lag_messages%7Btopic%3D%22topic-1%22%7D))"

# 查看有积压的消费者组
curl -s "http://localhost:9090/api/v1/query?query=sum%20by%20(consumer_group)%20(kafka_consumer_lag_messages%7Btopic%3D%22topic-1%22%7D)%20%3E%200"
```

## 🎯 业务场景查询

### 19. 识别需要扩容的消费者组
```promql
sum by (consumer_group) (kafka_consumer_lag_messages{topic="topic-1"}) > 100
```

### 20. 监控消费效率
```promql
rate(kafka_consumer_current_offset{topic="topic-1"}[5m])
```

### 21. 预测消费完成时间 (基于当前消费速率)
```promql
kafka_consumer_lag_messages{topic="topic-1"} / rate(kafka_consumer_current_offset{topic="topic-1"}[5m])
```

## 📋 Grafana 仪表板建议

### 面板配置建议:
1. **积压总览**: 使用表格显示各消费者组的积压情况
2. **积压趋势**: 使用时间序列图显示积压变化
3. **分区分布**: 使用饼图显示各分区的积压分布
4. **消费速率**: 使用仪表盘显示消费速率
5. **告警状态**: 使用状态面板显示告警情况

### 告警配置:
- 积压超过50条消息时发送警告
- 积压超过100条消息时发送严重告警
- 消费者组长时间无活动时发送通知

## 🔧 故障排查指南

### 常见问题及查询:
1. **消费者组停止消费**: 查看 `kafka_consumer_lag_messages` 是否持续增长
2. **分区消费不均衡**: 比较各分区的积压情况
3. **消费速度过慢**: 监控 `rate(kafka_consumer_current_offset[5m])`
4. **重复消费**: 检查 offset 是否异常回退

## 💡 优化建议

1. **监控频率**: 建议每30秒收集一次指标
2. **数据保留**: 建议保留至少7天的历史数据
3. **告警策略**: 设置多级告警阈值
4. **自动化**: 考虑基于积压情况自动扩缩容消费者
