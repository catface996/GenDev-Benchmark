#!/bin/bash

echo "📊 Topic-1 消费者积压监控报告"
echo "=================================="
echo "生成时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 获取topic-1的基本信息
echo "🎯 Topic-1 基本信息:"
echo "-------------------"
topic_info=$(docker exec kafka kafka-topics --describe --topic topic-1 --bootstrap-server localhost:9092)
echo "$topic_info"
echo ""

# 获取所有消费者组
consumer_groups=$(docker exec kafka kafka-consumer-groups --bootstrap-server localhost:9092 --list)

echo "👥 消费者组积压详情:"
echo "-------------------"

total_lag=0
active_consumers=0
inactive_consumers=0

for group in $consumer_groups; do
    echo "🔍 消费者组: $group"
    
    # 获取消费者组详情
    group_info=$(docker exec kafka kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group "$group" 2>/dev/null)
    
    if echo "$group_info" | grep -q "topic-1"; then
        echo "$group_info" | grep "topic-1" | while IFS= read -r line; do
            if [[ $line == *"topic-1"* ]]; then
                # 解析每一行的信息
                partition=$(echo "$line" | awk '{print $3}')
                current_offset=$(echo "$line" | awk '{print $4}')
                log_end_offset=$(echo "$line" | awk '{print $5}')
                lag=$(echo "$line" | awk '{print $6}')
                consumer_id=$(echo "$line" | awk '{print $7}')
                
                if [[ "$consumer_id" == "-" ]]; then
                    status="🔴 非活跃"
                else
                    status="🟢 活跃"
                fi
                
                echo "  分区 $partition: 当前offset=$current_offset, 最新offset=$log_end_offset, 积压=$lag 条消息 [$status]"
            fi
        done
        
        # 计算该消费者组的总积压
        group_total_lag=$(echo "$group_info" | grep "topic-1" | awk '{sum += $6} END {print sum}')
        echo "  📈 消费者组 $group 总积压: $group_total_lag 条消息"
        
        # 检查是否有活跃消费者
        if echo "$group_info" | grep -q "console-consumer"; then
            echo "  ✅ 状态: 有活跃消费者"
            ((active_consumers++))
        else
            echo "  ⚠️  状态: 无活跃消费者"
            ((inactive_consumers++))
        fi
    else
        echo "  ℹ️  该消费者组未消费 topic-1"
    fi
    echo ""
done

echo "📋 汇总统计:"
echo "------------"
echo "活跃消费者组数量: $active_consumers"
echo "非活跃消费者组数量: $inactive_consumers"

# 获取topic-1的总消息数
total_messages=$(docker exec kafka kafka-run-class kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic topic-1 --time -1 | awk -F: '{sum += $3} END {print sum}')
echo "Topic-1 总消息数: $total_messages"

echo ""
echo "🚨 告警建议:"
echo "------------"
echo "- 积压超过50条消息的消费者组需要关注"
echo "- 非活跃消费者组可能需要重启"
echo "- 建议监控消费速率和生产速率的平衡"
