# 📊 Consumer-Group-2 消费模拟报告

## 🎯 消费操作概览
- **消费者组**: consumer-group-2
- **目标Topic**: topic-1
- **消费数量**: 10条消息
- **操作时间**: $(date '+%Y-%m-%d %H:%M:%S')

## 📈 消费前后对比

### 消费前状态
| 分区 | Current Offset | Log End Offset | 积压消息数 |
|------|----------------|----------------|------------|
| 0    | 0              | 32             | 32         |
| 1    | 0              | 30             | 30         |
| 2    | 0              | 38             | 38         |
| **总计** | **0**      | **100**        | **100**    |

### 消费后状态
| 分区 | Current Offset | Log End Offset | 积压消息数 | 消费数量 |
|------|----------------|----------------|------------|----------|
| 0    | 4              | 32             | 28         | 4        |
| 1    | 3              | 30             | 27         | 3        |
| 2    | 3              | 38             | 35         | 3        |
| **总计** | **10**     | **100**        | **90**     | **10**   |

## 📊 关键指标变化

### 积压情况
- **消费前总积压**: 100条消息
- **消费后总积压**: 90条消息
- **积压减少量**: 10条消息 ✅
- **积压减少率**: 10%

### 消费进度
- **消费前进度**: 0% (0/100)
- **消费后进度**: 10% (10/100)
- **进度提升**: +10%

### 分区消费分布
- **分区0**: 消费4条 (40%)
- **分区1**: 消费3条 (30%)
- **分区2**: 消费3条 (30%)

## 🔍 Prometheus查询验证

### 查看消费后的积压情况
```promql
kafka_consumer_lag_messages{topic="topic-1", consumer_group="consumer-group-2"}
```

### 查看当前offset
```promql
kafka_consumer_current_offset{topic="topic-1", consumer_group="consumer-group-2"}
```

### 计算消费进度
```promql
(kafka_consumer_current_offset{topic="topic-1", consumer_group="consumer-group-2"} / kafka_consumer_log_end_offset{topic="topic-1", consumer_group="consumer-group-2"}) * 100
```

## 📋 所有消费者组对比

| 消费者组 | 消费前积压 | 消费后积压 | 变化 | 状态 |
|----------|------------|------------|------|------|
| consumer-group-1 | 0 | 0 | 无变化 | 🟢 正常 |
| consumer-group-2 | 100 | 90 | -10条 | 🟡 改善中 |
| consumer-group-3 | 70 | 70 | 无变化 | 🔴 待处理 |

## 🚨 告警状态变化

### 消费前告警
- 🔴 **严重积压**: consumer-group-2 (100条)
- ⚠️ **中等积压**: consumer-group-3 (70条)

### 消费后告警
- 🟠 **中等积压**: consumer-group-2 (90条) ⬇️ 从严重降级
- ⚠️ **中等积压**: consumer-group-3 (70条) 无变化

## 💡 分析与建议

### 消费效果
✅ **成功消费**: 按计划消费了10条消息
✅ **积压减少**: 总积压从100条降至90条
✅ **告警降级**: 从严重积压降级为中等积压

### 分区均衡性
- 分区0消费最多(4条)，可能因为消息分布不均
- 分区1和2各消费3条，相对均衡
- 建议监控分区间的消费均衡性

### 后续建议
1. **继续消费**: consumer-group-2还有90条积压需要处理
2. **监控consumer-group-3**: 70条积压未处理
3. **优化消费速率**: 可考虑增加消费者实例
4. **设置自动化**: 基于积压阈值自动扩缩容

## 🔄 实时监控命令

```bash
# 查看当前积压情况
curl -s "http://localhost:9090/api/v1/query?query=sum%20by%20(consumer_group)%20(kafka_consumer_lag_messages%7Btopic%3D%22topic-1%22%7D)"

# 查看消费进度
curl -s "http://localhost:9090/api/v1/query?query=(kafka_consumer_current_offset%7Btopic%3D%22topic-1%22%7D%20/%20kafka_consumer_log_end_offset%7Btopic%3D%22topic-1%22%7D)%20*%20100"

# 启动实时监控
./realtime_lag_monitor.sh
```
