#!/bin/bash

# Kafka消息生成器 - 生成各种类型的负载来测试监控指标

echo "🚀 启动Kafka消息生成器"
echo "======================"

# 函数：生成高频小消息
generate_high_frequency() {
    echo "⚡ 启动高频消息生成器..."
    for i in {1..100}; do
        echo "HighFreq-Message-$i-$(date '+%Y-%m-%d %H:%M:%S')" | \
        docker exec -i kafka kafka-console-producer --topic high-throughput --bootstrap-server localhost:9092 2>/dev/null
        sleep 0.1
    done &
}

# 函数：生成中等负载消息
generate_medium_load() {
    echo "📊 启动中等负载消息生成器..."
    for i in {1..50}; do
        # 生成较大的JSON消息
        message="{\"id\":$i,\"timestamp\":\"$(date -Iseconds)\",\"user_id\":$((RANDOM % 10000)),\"event\":\"user_action\",\"data\":\"$(head -c 200 /dev/urandom | base64 | tr -d '\n')\"}"
        echo "$message" | \
        docker exec -i kafka kafka-console-producer --topic medium-load --bootstrap-server localhost:9092 2>/dev/null
        sleep 0.5
    done &
}

# 函数：生成低延迟消息
generate_low_latency() {
    echo "🔥 启动低延迟消息生成器..."
    for i in {1..200}; do
        echo "LowLatency-$i-$(date '+%H:%M:%S.%3N')" | \
        docker exec -i kafka kafka-console-producer --topic low-latency --bootstrap-server localhost:9092 2>/dev/null
        sleep 0.05
    done &
}

# 函数：生成批处理消息
generate_batch_messages() {
    echo "📦 启动批处理消息生成器..."
    for batch in {1..10}; do
        echo "开始批次 $batch..."
        for i in {1..20}; do
            # 生成大消息
            large_data=$(head -c 1000 /dev/urandom | base64 | tr -d '\n')
            message="Batch-$batch-Message-$i-$(date -Iseconds)-Data:$large_data"
            echo "$message" | \
            docker exec -i kafka kafka-console-producer --topic batch-processing --bootstrap-server localhost:9092 2>/dev/null
        done
        echo "批次 $batch 完成，等待..."
        sleep 2
    done &
}

# 函数：生成性能测试消息
generate_performance_test() {
    echo "🎯 启动性能测试消息生成器..."
    for i in {1..150}; do
        # 随机大小的消息
        size=$((RANDOM % 500 + 100))
        data=$(head -c $size /dev/urandom | base64 | tr -d '\n')
        message="PerfTest-$i-$(date '+%Y-%m-%d %H:%M:%S')-Size:$size-Data:$data"
        echo "$message" | \
        docker exec -i kafka kafka-console-producer --topic performance-test --bootstrap-server localhost:9092 2>/dev/null
        sleep $((RANDOM % 3 + 1))
    done &
}

# 函数：监控消息生成统计
monitor_stats() {
    echo "📈 启动统计监控..."
    while true; do
        sleep 10
        echo ""
        echo "📊 当前Topic消息统计:"
        echo "===================="
        
        for topic in high-throughput medium-load low-latency batch-processing performance-test; do
            count=$(docker exec kafka kafka-run-class kafka.tools.GetOffsetShell \
                --broker-list localhost:9092 --topic $topic --time -1 2>/dev/null | \
                awk -F: '{sum += $3} END {print sum}' 2>/dev/null || echo "0")
            printf "%-20s: %s 条消息\n" "$topic" "$count"
        done
        
        echo ""
        echo "🔍 实时指标检查:"
        echo "Kafka Exporter指标数量: $(curl -s http://localhost:9308/metrics | grep -c kafka_topic 2>/dev/null || echo "N/A")"
        echo "Consumer Lag指标数量: $(curl -s http://localhost:9309/metrics | grep -c kafka_consumer 2>/dev/null || echo "N/A")"
    done &
}

# 主函数
main() {
    echo "🎯 开始生成各种类型的Kafka消息负载..."
    echo "这将帮助测试Dashboard中的各项监控指标"
    echo ""
    
    # 启动所有生成器
    generate_high_frequency
    sleep 2
    generate_medium_load
    sleep 2
    generate_low_latency
    sleep 2
    generate_batch_messages
    sleep 2
    generate_performance_test
    sleep 2
    monitor_stats
    
    echo "✅ 所有消息生成器已启动"
    echo "📊 统计监控已启动"
    echo ""
    echo "⏳ 消息生成将持续运行..."
    echo "💡 可以通过以下方式查看效果:"
    echo "   • Prometheus: http://localhost:9090"
    echo "   • Kafka Metrics: http://localhost:9308/metrics"
    echo "   • Consumer Lag: http://localhost:9309/metrics"
    echo ""
    echo "🛑 按 Ctrl+C 停止生成器"
    
    # 等待所有后台任务完成
    wait
}

# 捕获中断信号
trap 'echo ""; echo "⏹️  正在停止所有消息生成器..."; kill $(jobs -p) 2>/dev/null; echo "✅ 已停止"; exit 0' INT

# 运行主函数
main
