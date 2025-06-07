#!/bin/bash

# Kafka监控环境一键部署脚本
# 使用方法: chmod +x setup-kafka-monitoring.sh && ./setup-kafka-monitoring.sh

set -e

echo "🚀 Kafka监控环境部署脚本"
echo "========================="

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    echo "❌ Docker未安装，请先安装Docker"
    exit 1
fi

if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose未安装，请先安装Docker Compose"
    exit 1
fi

# 检查Python3是否安装（用于消费者积压监控）
if ! command -v python3 &> /dev/null; then
    echo "⚠️  Python3未安装，消费者积压监控功能将不可用"
    PYTHON_AVAILABLE=false
else
    PYTHON_AVAILABLE=true
fi

echo "✅ 环境检查通过"

# 创建必要的目录
mkdir -p kafka-monitoring
cd kafka-monitoring

# 检查文件是否存在
if [ ! -f "kafka-monitoring-compose.yml" ]; then
    echo "❌ kafka-monitoring-compose.yml 文件不存在"
    echo "请确保所有必要文件都在当前目录中"
    exit 1
fi

if [ ! -f "prometheus-config.yml" ]; then
    echo "❌ prometheus-config.yml 文件不存在"
    exit 1
fi

# 复制配置文件
cp prometheus-config.yml prometheus.yml

echo "📦 启动Kafka监控环境..."

# 停止可能存在的容器
docker-compose -f kafka-monitoring-compose.yml down 2>/dev/null || true

# 启动服务
docker-compose -f kafka-monitoring-compose.yml up -d

echo "⏳ 等待服务启动..."
sleep 15

# 检查服务状态
echo "🔍 检查服务状态..."
docker-compose -f kafka-monitoring-compose.yml ps

# 等待Kafka完全启动
echo "⏳ 等待Kafka完全启动..."
sleep 10

# 重启kafka-exporter（确保连接成功）
docker-compose -f kafka-monitoring-compose.yml restart kafka-exporter
sleep 5

# 创建测试topic
echo "📝 创建测试topic..."
docker exec kafka kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1 2>/dev/null || echo "Topic可能已存在"

# 发送测试消息
echo "📨 发送测试消息..."
for i in {1..10}; do
    echo "Test message $i - $(date)" | docker exec -i kafka kafka-console-producer --topic test-topic --bootstrap-server localhost:9092 2>/dev/null
done

echo "✅ 测试消息发送完成"

# 启动消费者积压监控（如果Python可用）
if [ "$PYTHON_AVAILABLE" = true ] && [ -f "kafka_consumer_lag_monitor.py" ]; then
    echo "🔄 启动消费者积压监控..."
    nohup python3 kafka_consumer_lag_monitor.py > consumer_lag_monitor.log 2>&1 &
    echo $! > consumer_lag_monitor.pid
    sleep 3
    echo "✅ 消费者积压监控已启动 (PID: $(cat consumer_lag_monitor.pid))"
fi

# 验证服务
echo ""
echo "🎯 服务验证:"
echo "============"

# 检查Kafka
if curl -s http://localhost:9308/metrics | grep -q kafka_topic; then
    echo "✅ Kafka Exporter: 正常"
else
    echo "❌ Kafka Exporter: 异常"
fi

# 检查Prometheus
if curl -s http://localhost:9090/api/v1/status/config | grep -q success; then
    echo "✅ Prometheus: 正常"
else
    echo "❌ Prometheus: 异常"
fi

# 检查消费者积压监控
if [ "$PYTHON_AVAILABLE" = true ] && curl -s http://localhost:9309/health | grep -q healthy; then
    echo "✅ 消费者积压监控: 正常"
elif [ "$PYTHON_AVAILABLE" = false ]; then
    echo "⚠️  消费者积压监控: 未启动 (Python3不可用)"
else
    echo "❌ 消费者积压监控: 异常"
fi

echo ""
echo "🎉 Kafka监控环境部署完成！"
echo "=========================="
echo ""
echo "📊 访问地址:"
echo "• Kafka: localhost:9092"
echo "• Prometheus: http://localhost:9090"
echo "• Kafka Metrics: http://localhost:9308/metrics"
if [ "$PYTHON_AVAILABLE" = true ]; then
    echo "• Consumer Lag: http://localhost:9309/metrics"
fi
echo ""
echo "🔧 管理命令:"
echo "• 查看日志: docker-compose -f kafka-monitoring-compose.yml logs -f"
echo "• 停止服务: docker-compose -f kafka-monitoring-compose.yml down"
echo "• 重启服务: docker-compose -f kafka-monitoring-compose.yml restart"
echo ""
echo "📝 测试命令:"
echo "• 查看topics: docker exec kafka kafka-topics --list --bootstrap-server localhost:9092"
echo "• 发送消息: echo 'test' | docker exec -i kafka kafka-console-producer --topic test-topic --bootstrap-server localhost:9092"
echo "• 消费消息: docker exec kafka kafka-console-consumer --topic test-topic --bootstrap-server localhost:9092 --from-beginning --timeout-ms 5000"
echo ""

if [ "$PYTHON_AVAILABLE" = true ] && [ -f "consumer_lag_monitor.pid" ]; then
    echo "🛑 停止消费者积压监控: kill \$(cat consumer_lag_monitor.pid)"
fi

echo "✅ 部署完成！"
