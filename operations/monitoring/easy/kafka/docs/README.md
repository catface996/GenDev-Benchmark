# Kafka监控环境部署包

## 📦 包含文件
- `kafka-monitoring-compose.yml` - Docker Compose配置文件
- `prometheus-config.yml` - Prometheus配置文件  
- `kafka_consumer_lag_monitor.py` - 消费者积压监控器
- `setup-kafka-monitoring.sh` - 一键部署脚本
- `README.md` - 使用说明

## 🚀 快速部署

### 方法1: 一键脚本部署
```bash
chmod +x setup-kafka-monitoring.sh
./setup-kafka-monitoring.sh
```

### 方法2: 手动部署
```bash
# 1. 复制配置文件
cp prometheus-config.yml prometheus.yml

# 2. 启动服务
docker-compose -f kafka-monitoring-compose.yml up -d

# 3. 启动消费者积压监控(可选)
python3 kafka_consumer_lag_monitor.py &
```

## 📊 服务访问
- Kafka: `localhost:9092`
- Prometheus: `http://localhost:9090`
- Kafka Metrics: `http://localhost:9308/metrics`
- Consumer Lag: `http://localhost:9309/metrics`

## 🔧 管理命令
```bash
# 查看状态
docker-compose -f kafka-monitoring-compose.yml ps

# 查看日志
docker-compose -f kafka-monitoring-compose.yml logs -f

# 停止服务
docker-compose -f kafka-monitoring-compose.yml down
```

## 📝 测试命令
```bash
# 创建topic
docker exec kafka kafka-topics --create --topic test --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1

# 发送消息
echo "test message" | docker exec -i kafka kafka-console-producer --topic test --bootstrap-server localhost:9092

# 消费消息
docker exec kafka kafka-console-consumer --topic test --bootstrap-server localhost:9092 --from-beginning --timeout-ms 5000
```
