#!/bin/bash

# Kafka监控环境部署验证脚本
# 验证所有服务是否正常运行

echo "🔍 Kafka监控环境部署验证"
echo "========================"

# 获取主机IP
HOST_IP=$(hostname -I | awk '{print $1}' 2>/dev/null || ip route get 1 | awk '{print $7}' | head -1 2>/dev/null || echo "localhost")

echo "🔍 验证主机: $HOST_IP"
echo ""

# 验证Docker服务状态
echo "📊 1. Docker服务状态验证:"
echo "------------------------"
if docker-compose -f configs/docker-compose-new-host.yml ps | grep -q "Up"; then
    echo "✅ Docker服务正在运行"
    docker-compose -f configs/docker-compose-new-host.yml ps
else
    echo "❌ Docker服务未运行或异常"
    exit 1
fi

echo ""

# 验证端口连通性
echo "🔌 2. 端口连通性验证:"
echo "-------------------"

ports=("2181:Zookeeper" "9092:Kafka" "9090:Prometheus" "3000:Grafana" "9308:Kafka-Exporter")

for port_info in "${ports[@]}"; do
    port=$(echo $port_info | cut -d: -f1)
    service=$(echo $port_info | cut -d: -f2)
    
    if nc -z $HOST_IP $port 2>/dev/null || timeout 3 bash -c "</dev/tcp/$HOST_IP/$port" 2>/dev/null; then
        echo "✅ $service ($port): 可访问"
    else
        echo "❌ $service ($port): 不可访问"
    fi
done

echo ""

# 验证HTTP服务
echo "🌐 3. HTTP服务验证:"
echo "-----------------"

# Prometheus
if curl -s "http://$HOST_IP:9090/api/v1/status/config" | grep -q "success"; then
    echo "✅ Prometheus (9090): 正常"
else
    echo "❌ Prometheus (9090): 异常"
fi

# Grafana
if curl -s "http://$HOST_IP:3000/api/health" | grep -q "ok"; then
    echo "✅ Grafana (3000): 正常"
else
    echo "❌ Grafana (3000): 异常"
fi

# Kafka Exporter
if curl -s "http://$HOST_IP:9308/metrics" | grep -q "kafka_topic"; then
    echo "✅ Kafka Exporter (9308): 正常"
else
    echo "❌ Kafka Exporter (9308): 异常"
fi

# Consumer Lag Monitor
if curl -s "http://$HOST_IP:9309/health" 2>/dev/null | grep -q "healthy"; then
    echo "✅ Consumer Lag Monitor (9309): 正常"
else
    echo "⚠️  Consumer Lag Monitor (9309): 未运行或异常"
fi

echo ""

# 验证Kafka功能
echo "📨 4. Kafka功能验证:"
echo "------------------"

# 创建测试topic
if docker exec kafka kafka-topics --create --topic test-deployment --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 2>/dev/null; then
    echo "✅ Topic创建: 成功"
    
    # 发送测试消息
    if echo "deployment-test-$(date)" | docker exec -i kafka kafka-console-producer --topic test-deployment --bootstrap-server localhost:9092 2>/dev/null; then
        echo "✅ 消息发送: 成功"
        
        # 消费测试消息
        if timeout 5s docker exec kafka kafka-console-consumer --topic test-deployment --bootstrap-server localhost:9092 --from-beginning --timeout-ms 3000 2>/dev/null | grep -q "deployment-test"; then
            echo "✅ 消息消费: 成功"
        else
            echo "⚠️  消息消费: 超时或异常"
        fi
    else
        echo "❌ 消息发送: 失败"
    fi
    
    # 清理测试topic
    docker exec kafka kafka-topics --delete --topic test-deployment --bootstrap-server localhost:9092 2>/dev/null
else
    echo "❌ Topic创建: 失败"
fi

echo ""

# 验证Prometheus指标
echo "📈 5. Prometheus指标验证:"
echo "------------------------"

# 检查Kafka指标
kafka_metrics=$(curl -s "http://$HOST_IP:9090/api/v1/query?query=kafka_topic_partitions" | grep -o '"result":\[[^]]*\]' | grep -o '\[.*\]')
if [ ! -z "$kafka_metrics" ] && [ "$kafka_metrics" != "[]" ]; then
    echo "✅ Kafka指标: 有数据"
else
    echo "❌ Kafka指标: 无数据"
fi

# 检查进程指标
process_metrics=$(curl -s "http://$HOST_IP:9090/api/v1/query?query=process_network_receive_bytes_total" | grep -o '"result":\[[^]]*\]' | grep -o '\[.*\]')
if [ ! -z "$process_metrics" ] && [ "$process_metrics" != "[]" ]; then
    echo "✅ 进程指标: 有数据"
else
    echo "❌ 进程指标: 无数据"
fi

echo ""

# 生成验证报告
echo "📋 6. 验证报告:"
echo "-------------"

# 统计验证结果
total_checks=0
passed_checks=0

# 这里可以添加更详细的统计逻辑
echo "🎯 部署验证完成"
echo ""
echo "🔗 访问地址:"
echo "• Kafka: $HOST_IP:9092"
echo "• Prometheus: http://$HOST_IP:9090"
echo "• Grafana: http://$HOST_IP:3000 (admin/admin)"
echo ""
echo "📊 下一步:"
echo "1. 访问Grafana导入Dashboard文件"
echo "2. 运行: ./scripts/simple_message_generator.sh 生成测试数据"
echo "3. 在Dashboard中查看监控数据"
echo ""
echo "📚 如有问题，请查看:"
echo "• Docker日志: docker-compose -f configs/docker-compose-new-host.yml logs"
echo "• 消费者积压监控日志: cat consumer_lag_monitor.log"
