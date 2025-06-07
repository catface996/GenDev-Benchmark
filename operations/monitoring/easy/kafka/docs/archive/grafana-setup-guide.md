# Grafana Kafka Dashboard 设置指南

## 🎯 快速导入Dashboard

### 步骤1: 访问Grafana
1. 打开浏览器访问: `http://localhost:3000`
2. 使用默认账号登录:
   - 用户名: `admin`
   - 密码: `admin`
3. 首次登录会要求修改密码

### 步骤2: 添加Prometheus数据源
1. 点击左侧菜单 `Configuration` → `Data Sources`
2. 点击 `Add data source`
3. 选择 `Prometheus`
4. 配置如下:
   - **Name**: `Prometheus`
   - **URL**: `http://prometheus:9090`
   - **Access**: `Server (default)`
5. 点击 `Save & Test`，确保显示绿色的成功消息

### 步骤3: 导入Dashboard
1. 点击左侧菜单 `+` → `Import`
2. 选择 `Upload JSON file`
3. 上传 `kafka-dashboard.json` 文件
4. 或者复制JSON内容粘贴到文本框中
5. 点击 `Load`
6. 确认配置:
   - **Name**: Kafka监控仪表板
   - **Folder**: General (或选择其他文件夹)
   - **Prometheus**: 选择刚才创建的Prometheus数据源
7. 点击 `Import`

## 📊 Dashboard功能说明

### 面板1: Topic消息总数
- **类型**: 时间序列图
- **功能**: 显示各个Topic的消息总数变化趋势
- **查询**: `sum by (topic) (kafka_topic_partition_current_offset)`

### 面板2: Topic概览
- **类型**: 表格
- **功能**: 显示所有Topic的消息数和分区数
- **包含**: Topic名称、消息数、分区数

### 面板3: 消息生产速率
- **类型**: 时间序列图
- **功能**: 显示每个分区的消息生产速率
- **查询**: `rate(kafka_topic_partition_current_offset[5m])`

### 面板4: 消费者积压情况
- **类型**: 表格
- **功能**: 显示各消费者组的积压消息数
- **颜色编码**: 绿色(正常) → 黄色(警告) → 红色(严重)

### 面板5: 消费者积压趋势
- **类型**: 时间序列图
- **功能**: 显示消费者积压的变化趋势
- **查询**: `kafka_consumer_lag_messages`

### 面板6-9: 统计面板
- **Topic总数**: 集群中的Topic数量
- **总消息数**: 所有Topic的消息总数
- **消费者组数量**: 活跃的消费者组数量
- **总积压消息数**: 所有消费者组的积压总数

## 🔧 自定义配置

### 修改刷新频率
- 默认: 30秒自动刷新
- 可在右上角时间选择器旁边修改

### 调整时间范围
- 默认: 最近1小时
- 可在右上角时间选择器中修改

### 设置告警
1. 选择任意面板
2. 点击面板标题 → `Edit`
3. 切换到 `Alert` 标签页
4. 配置告警规则和通知渠道

## 🚨 常见问题

### Q: Dashboard显示"No data"
**A**: 检查以下项目:
1. Prometheus数据源配置是否正确
2. Kafka Exporter是否正常运行: `curl http://localhost:9308/metrics`
3. 消费者积压监控是否启动: `curl http://localhost:9309/metrics`

### Q: 消费者积压面板无数据
**A**: 确保:
1. 消费者积压监控器正在运行
2. Prometheus配置中包含了消费者积压监控的target
3. 存在消费者组和积压数据

### Q: 如何添加新的监控面板
**A**: 
1. 点击Dashboard右上角的 `Add panel`
2. 选择可视化类型
3. 配置Prometheus查询
4. 设置面板标题和样式

## 📈 推荐的Prometheus查询

```promql
# Topic消息增长率
rate(kafka_topic_partition_current_offset[5m])

# 消费者组积压排行
topk(10, sum by (consumer_group) (kafka_consumer_lag_messages))

# 分区消息分布
kafka_topic_partition_current_offset

# 消费进度百分比
(kafka_consumer_current_offset / kafka_consumer_log_end_offset) * 100

# 积压超过阈值的消费者组
sum by (consumer_group) (kafka_consumer_lag_messages) > 50
```

## 🎨 美化建议

1. **使用变量**: 添加Topic和消费者组变量进行过滤
2. **设置阈值**: 为关键指标设置颜色阈值
3. **添加注释**: 在重要事件时间点添加注释
4. **创建文件夹**: 按环境或业务线组织Dashboard

完成以上步骤后，你就拥有了一个功能完整的Kafka监控仪表板！
