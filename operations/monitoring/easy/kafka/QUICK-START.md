# Kafka监控环境快速启动指南

## 🚀 5分钟快速启动

### 步骤1: 启动监控环境
```bash
cd ~/Desktop/Kafka
docker-compose -f configs/docker-compose.yml up -d
```

### 步骤2: 启动消费者积压监控
```bash
python3 scripts/kafka_consumer_lag_monitor.py &
```

### 步骤3: 生成测试数据
```bash
./scripts/simple_message_generator.sh
```

### 步骤4: 访问Grafana
1. 打开浏览器访问: http://localhost:3000
2. 登录: admin/admin
3. 导入Dashboard:
   - `dashboards/kafka-dashboard-fixed.json` (推荐)
   - `dashboards/kafka-cluster-dashboard.json`
   - `dashboards/kafka-topic-dashboard.json`

## 📊 Dashboard推荐使用顺序

1. **kafka-dashboard-fixed.json** - 查看整体状况和网络IO
2. **kafka-cluster-dashboard.json** - 集群级别监控
3. **kafka-topic-dashboard.json** - 深入分析特定Topic

## 🔗 访问地址
- **Grafana**: http://localhost:3000 (admin/admin)
- **Prometheus**: http://localhost:9090
- **Kafka**: localhost:9092

## 🛑 停止环境
```bash
# 停止消息生成器
pkill -f simple_message_generator.sh

# 停止消费者积压监控
pkill -f kafka_consumer_lag_monitor.py

# 停止Docker容器
docker-compose -f configs/docker-compose.yml down
```

## 📚 详细文档
- [完整使用指南](README.md)
- [Dashboard使用指南](docs/DASHBOARD-GUIDE.md)

## 🎉 开始监控
环境启动后，即可在Grafana中查看实时的Kafka监控数据！
