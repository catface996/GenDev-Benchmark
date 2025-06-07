#!/bin/bash

# Kafka增强监控部署脚本
# 包含JMX指标、IO监控、连接数等Broker指标

set -e

echo "🚀 部署Kafka增强监控环境"
echo "=========================="

# 检查必要文件
required_files=(
    "kafka-enhanced-compose.yml"
    "prometheus-enhanced.yml"
    "jmx-exporter/jmx_prometheus_javaagent.jar"
    "jmx-exporter/kafka-broker.yml"
)

for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ 缺少必要文件: $file"
        exit 1
    fi
done

echo "✅ 文件检查通过"

# 停止现有服务
echo "🛑 停止现有服务..."
docker-compose -f kafka-enhanced-compose.yml down 2>/dev/null || true
docker-compose down 2>/dev/null || true

# 清理旧容器
echo "🧹 清理旧容器..."
docker container prune -f

# 启动增强监控服务
echo "🚀 启动增强监控服务..."
docker-compose -f kafka-enhanced-compose.yml up -d

echo "⏳ 等待服务启动..."
sleep 20

# 检查服务状态
echo "🔍 检查服务状态..."
docker-compose -f kafka-enhanced-compose.yml ps

# 等待Kafka完全启动
echo "⏳ 等待Kafka完全启动..."
sleep 15

# 重启kafka-exporter确保连接成功
echo "🔄 重启kafka-exporter..."
docker-compose -f kafka-enhanced-compose.yml restart kafka-exporter
sleep 5

# 创建测试数据
echo "📝 创建测试数据..."

# 创建测试topic
docker exec kafka kafka-topics --create --topic performance-test --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1 2>/dev/null || echo "Topic可能已存在"

# 发送测试消息
echo "📨 发送测试消息..."
for i in {1..100}; do
    echo "Performance test message $i - $(date)" | docker exec -i kafka kafka-console-producer --topic performance-test --bootstrap-server localhost:9092 2>/dev/null
done

# 创建消费者组产生积压
echo "👥 创建测试消费者组..."
docker exec kafka kafka-consumer-groups --bootstrap-server localhost:9092 --group perf-consumer-1 --reset-offsets --to-earliest --topic performance-test --execute > /dev/null 2>&1 || true
docker exec kafka kafka-consumer-groups --bootstrap-server localhost:9092 --group perf-consumer-2 --reset-offsets --to-offset 50 --topic performance-test --execute > /dev/null 2>&1 || true

# 启动消费者积压监控
if [ -f "kafka_consumer_lag_monitor.py" ]; then
    echo "🔄 启动消费者积压监控..."
    pkill -f kafka_consumer_lag_monitor.py || true
    nohup python3 kafka_consumer_lag_monitor.py > consumer_lag_monitor.log 2>&1 &
    echo $! > consumer_lag_monitor.pid
    sleep 3
fi

# 验证所有监控端点
echo ""
echo "🎯 监控端点验证:"
echo "================"

# 检查Kafka Exporter
if curl -s http://localhost:9308/metrics | grep -q kafka_topic; then
    echo "✅ Kafka Exporter (9308): 正常"
else
    echo "❌ Kafka Exporter (9308): 异常"
fi

# 检查JMX Exporter
if curl -s http://localhost:8080/metrics | grep -q kafka_server; then
    echo "✅ JMX Exporter (8080): 正常"
else
    echo "❌ JMX Exporter (8080): 异常"
fi

# 检查Prometheus
if curl -s http://localhost:9090/api/v1/status/config | grep -q success; then
    echo "✅ Prometheus (9090): 正常"
else
    echo "❌ Prometheus (9090): 异常"
fi

# 检查消费者积压监控
if curl -s http://localhost:9309/health | grep -q healthy 2>/dev/null; then
    echo "✅ 消费者积压监控 (9309): 正常"
else
    echo "⚠️  消费者积压监控 (9309): 未启动或异常"
fi

echo ""
echo "📊 可用指标类型:"
echo "==============="
echo "• Topic指标: kafka_topic_*"
echo "• Broker指标: kafka_server_*"
echo "• 网络指标: kafka_network_*"
echo "• JVM指标: jvm_*"
echo "• 消费者积压: kafka_consumer_lag_*"

echo ""
echo "🎉 Kafka增强监控环境部署完成！"
echo "==============================="
echo ""
echo "📊 访问地址:"
echo "• Kafka: localhost:9092"
echo "• Prometheus: http://localhost:9090"
echo "• Kafka Metrics: http://localhost:9308/metrics"
echo "• JMX Metrics: http://localhost:8080/metrics"
echo "• Consumer Lag: http://localhost:9309/metrics"
echo ""
echo "📈 Grafana Dashboard:"
echo "• 导入文件: kafka-enhanced-dashboard.json"
echo "• 数据源: http://prometheus:9090"
echo ""
echo "🔧 管理命令:"
echo "• 查看日志: docker-compose -f kafka-enhanced-compose.yml logs -f"
echo "• 停止服务: docker-compose -f kafka-enhanced-compose.yml down"
echo "• 重启服务: docker-compose -f kafka-enhanced-compose.yml restart"
echo ""
echo "📝 测试命令:"
echo "• 发送消息: echo 'test' | docker exec -i kafka kafka-console-producer --topic performance-test --bootstrap-server localhost:9092"
echo "• 查看指标: curl http://localhost:8080/metrics | grep kafka_server"
echo ""

if [ -f "consumer_lag_monitor.pid" ]; then
    echo "🛑 停止消费者积压监控: kill \$(cat consumer_lag_monitor.pid)"
fi

echo "✅ 部署完成！现在可以导入增强版Dashboard到Grafana"
