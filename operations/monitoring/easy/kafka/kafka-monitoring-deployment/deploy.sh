#!/bin/bash

# Kafka监控环境新主机部署脚本

echo "🚀 Kafka监控环境部署脚本"
echo "========================"

# 检查Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker未安装，请先安装Docker"
    exit 1
fi

if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose未安装，请先安装Docker Compose"
    exit 1
fi

# 获取主机IP
HOST_IP=$(hostname -I | awk '{print $1}' 2>/dev/null || ip route get 1 | awk '{print $7}' | head -1 2>/dev/null || echo "localhost")
echo "🔍 检测到主机IP: $HOST_IP"

# 询问是否使用检测到的IP
read -p "是否使用检测到的IP地址 $HOST_IP? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    read -p "请输入正确的主机IP地址: " HOST_IP
fi

echo "✅ 使用主机IP: $HOST_IP"

# 替换配置文件中的占位符
echo "⚙️  配置网络地址..."
sed -i.bak "s/YOUR_HOST_IP/$HOST_IP/g" configs/docker-compose-new-host.yml
sed -i.bak "s/YOUR_HOST_IP/$HOST_IP/g" configs/prometheus-new-host.yml

# 启动服务
echo "🚀 启动Kafka监控服务..."
docker-compose -f configs/docker-compose-new-host.yml up -d

echo "⏳ 等待服务启动..."
sleep 20

# 检查服务状态
echo "🔍 检查服务状态:"
docker-compose -f configs/docker-compose-new-host.yml ps

# 启动消费者积压监控
if [ -f "scripts/kafka_consumer_lag_monitor.py" ]; then
    echo "🔄 启动消费者积压监控..."
    if command -v python3 &> /dev/null; then
        nohup python3 scripts/kafka_consumer_lag_monitor.py > consumer_lag_monitor.log 2>&1 &
        echo $! > consumer_lag_monitor.pid
        echo "✅ 消费者积压监控已启动"
    else
        echo "⚠️  Python3未安装，跳过消费者积压监控"
    fi
fi

echo ""
echo "🎉 Kafka监控环境部署完成！"
echo "=========================="
echo ""
echo "🔗 访问地址:"
echo "• Kafka: $HOST_IP:9092"
echo "• Prometheus: http://$HOST_IP:9090"
echo "• Grafana: http://$HOST_IP:3000 (admin/admin)"
echo ""
echo "📊 下一步:"
echo "1. 访问Grafana导入Dashboard文件"
echo "2. 运行测试脚本生成数据: ./scripts/simple_message_generator.sh"
echo "3. 查看监控数据"
echo ""
echo "🛑 停止服务: docker-compose -f configs/docker-compose-new-host.yml down"
