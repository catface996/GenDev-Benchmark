#!/bin/bash

# 为不同的topic生成不同数量的消息
topics=(
    "topic-1:50"
    "topic-2:100" 
    "topic-3:25"
    "topic-4:200"
    "topic-5:75"
    "topic-6:150"
    "topic-7:30"
    "topic-8:300"
    "topic-9:80"
    "topic-10:120"
)

echo "开始为各个topic生成测试数据..."

for topic_config in "${topics[@]}"; do
    IFS=':' read -r topic_name message_count <<< "$topic_config"
    echo "正在为 $topic_name 生成 $message_count 条消息..."
    
    for ((i=1; i<=message_count; i++)); do
        message="Message $i for $topic_name - $(date '+%Y-%m-%d %H:%M:%S')"
        echo "$message" | docker exec -i kafka kafka-console-producer --topic "$topic_name" --bootstrap-server localhost:9092 > /dev/null 2>&1
        
        # 每10条消息显示一次进度
        if [ $((i % 10)) -eq 0 ]; then
            echo "  已发送 $i/$message_count 条消息到 $topic_name"
        fi
    done
    
    echo "✅ 完成 $topic_name: $message_count 条消息"
    echo ""
done

echo "🎉 所有测试数据生成完成！"
