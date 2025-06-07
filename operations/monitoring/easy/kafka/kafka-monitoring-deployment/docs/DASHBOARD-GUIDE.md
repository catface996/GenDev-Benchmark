# Kafka Dashboard使用指南

## 📊 Dashboard概览

我们为你创建了两个专业的Kafka监控Dashboard：

### 1. Kafka集群监控Dashboard (`kafka-cluster-dashboard.json`)
**用途**: 集群级别的整体监控和健康状态
**特点**: 
- 集群整体视图
- 跨Topic的聚合指标
- Broker和Consumer组统计
- 集群性能趋势

### 2. Kafka Topic详细监控Dashboard (`kafka-topic-dashboard.json`)
**用途**: 单个Topic的深度分析和监控
**特点**:
- Topic选择器 (支持动态切换)
- 分区级别的详细监控
- Consumer消费情况分析
- 实时性能指标

## 🚀 导入步骤

### 步骤1: 访问Grafana
```
http://localhost:3000
用户名: admin
密码: admin
```

### 步骤2: 配置数据源 (如果还未配置)
1. 点击左侧菜单 `Configuration` → `Data Sources`
2. 点击 `Add data source`
3. 选择 `Prometheus`
4. 配置:
   - **Name**: `Prometheus`
   - **URL**: `http://prometheus:9090`
5. 点击 `Save & Test`

### 步骤3: 导入Dashboard
1. 点击左侧菜单 `+` → `Import`
2. 选择 `Upload JSON file`
3. 分别上传两个Dashboard文件
4. 确认配置并点击 `Import`

## 📈 集群监控Dashboard详解

### 第一行: 关键指标统计 (6个Stat面板)
| 面板 | 指标 | 说明 | 告警阈值 |
|------|------|------|----------|
| **Broker总数** | `kafka_brokers` | 集群中的Broker数量 | - |
| **Topic总数** | `count(kafka_topic_partitions)` | 业务Topic数量 | - |
| **Consumer组总数** | `count(consumer_group)` | 活跃Consumer组数 | >20 |
| **分区总数** | `sum(kafka_topic_partitions)` | 所有分区总数 | - |
| **总消息数** | `sum(kafka_topic_partition_current_offset)` | 集群消息总量 | - |
| **总积压消息数** | `sum(kafka_consumer_lag_messages)` | 所有积压消息 | >1000 |

### 第二行: 性能趋势 (2个时间序列)
- **集群消息生产速率**: 整个集群的消息生产QPS
- **Consumer组积压趋势**: 各Consumer组的积压变化

### 第三行: 详细统计表 (2个表格)
- **Topic统计表**: 各Topic的消息数、分区数、生产速率
- **Consumer组积压统计**: 各Consumer组的积压情况

### 第四行: 整体趋势 (1个时间序列)
- **各Topic消息数量趋势**: 所有Topic的消息增长趋势

## 🎯 Topic监控Dashboard详解

### Topic选择器
- **位置**: Dashboard顶部
- **功能**: 动态选择要监控的Topic
- **选项**: 
  - `All`: 显示所有Topic的聚合数据
  - 具体Topic名称: 显示单个Topic的详细数据

### 第一行: Topic基础统计 (4个Stat面板)
| 面板 | 查询 | 说明 |
|------|------|------|
| **分区数** | `kafka_topic_partitions{topic=~"$topic"}` | 选中Topic的分区数量 |
| **消息总数** | `sum(kafka_topic_partition_current_offset{topic=~"$topic"})` | 选中Topic的消息总数 |
| **生产速率** | `sum(rate(kafka_topic_partition_current_offset{topic=~"$topic"}[5m]))` | 选中Topic的生产速率 |
| **积压消息数** | `sum(kafka_consumer_lag_messages{topic=~"$topic"})` | 选中Topic的积压总数 |

### 第二行: 分区级监控 (2个时间序列)
- **各分区消息数量趋势**: 每个分区的消息增长情况
- **各分区生产速率趋势**: 每个分区的生产速率变化

### 第三行: 分区详细信息 (1个表格)
- **分区详细信息**: 包含每个分区的消息数和生产速率

### 第四行: Consumer监控 (2个时间序列)
- **Consumer积压趋势**: 各Consumer组在该Topic上的积压情况
- **Consumer消费进度**: 各Consumer组的消费进度百分比

### 第五行: Consumer详细信息 (1个表格)
- **Consumer详细信息**: 包含积压数、当前偏移量、消费进度

## 🔍 使用场景

### 集群监控Dashboard适用于:
- **运维人员**: 监控整个Kafka集群的健康状态
- **架构师**: 分析集群容量和性能规划
- **管理者**: 了解系统整体运行情况
- **告警配置**: 设置集群级别的告警规则

### Topic监控Dashboard适用于:
- **开发人员**: 监控特定业务Topic的性能
- **业务分析**: 分析特定业务线的消息流量
- **问题排查**: 深入分析单个Topic的问题
- **性能优化**: 优化特定Topic的分区和消费策略

## 📊 关键查询语句

### 集群级查询
```promql
# 集群总生产速率
sum(rate(kafka_topic_partition_current_offset{topic!~"__.*"}[5m]))

# 集群总积压
sum(kafka_consumer_lag_messages)

# Topic数量
count by () (group by (topic) (kafka_topic_partitions{topic!~"__.*"}))

# Consumer组数量
count by () (group by (consumer_group) (kafka_consumer_lag_messages))
```

### Topic级查询
```promql
# 特定Topic的分区数
kafka_topic_partitions{topic="your-topic"}

# 特定Topic的消息总数
sum(kafka_topic_partition_current_offset{topic="your-topic"})

# 特定Topic的生产速率
sum(rate(kafka_topic_partition_current_offset{topic="your-topic"}[5m]))

# 特定Topic的Consumer积压
sum(kafka_consumer_lag_messages{topic="your-topic"})

# Consumer消费进度
(kafka_consumer_current_offset{topic="your-topic"} / kafka_consumer_log_end_offset{topic="your-topic"}) * 100
```

## 🚨 告警建议

### 集群级告警
```promql
# 总积压过多
sum(kafka_consumer_lag_messages) > 1000

# Consumer组过多
count by () (group by (consumer_group) (kafka_consumer_lag_messages)) > 20

# 集群生产速率异常
sum(rate(kafka_topic_partition_current_offset{topic!~"__.*"}[5m])) > 10000
```

### Topic级告警
```promql
# 特定Topic积压过多
sum(kafka_consumer_lag_messages{topic="important-topic"}) > 100

# 特定Topic生产速率异常
sum(rate(kafka_topic_partition_current_offset{topic="important-topic"}[5m])) > 1000

# Consumer消费进度过低
(kafka_consumer_current_offset{topic="important-topic"} / kafka_consumer_log_end_offset{topic="important-topic"}) * 100 < 50
```

## 🎨 自定义建议

### 添加更多变量
可以在Topic Dashboard中添加更多变量：
- **Consumer组选择器**: 过滤特定Consumer组
- **分区选择器**: 监控特定分区
- **时间范围选择器**: 快速切换时间范围

### 面板自定义
- **调整刷新频率**: 根据需要调整自动刷新间隔
- **修改颜色阈值**: 根据业务需求调整告警颜色
- **添加注释**: 在重要时间点添加事件注释
- **创建快照**: 保存重要时刻的监控快照

## 📝 最佳实践

1. **分层监控**: 先看集群Dashboard了解整体，再用Topic Dashboard深入分析
2. **定期检查**: 建议每天检查集群Dashboard，发现异常时使用Topic Dashboard
3. **告警配置**: 为关键指标配置告警，及时发现问题
4. **性能基线**: 记录正常情况下的指标基线，便于异常检测
5. **文档记录**: 记录重要的配置变更和性能事件

## 🔧 故障排查流程

### 发现问题
1. 在集群Dashboard中发现异常指标
2. 确定是哪个Topic或Consumer组的问题

### 深入分析
1. 使用Topic Dashboard选择问题Topic
2. 查看分区级别的详细数据
3. 分析Consumer的消费情况

### 解决问题
1. 根据监控数据定位根本原因
2. 采取相应的优化措施
3. 持续监控验证效果

---

现在你拥有了两个功能完整的Kafka监控Dashboard！🎉
