#!/bin/bash

echo "🔄 Topic-1 消费者积压实时监控"
echo "================================"
echo "按 Ctrl+C 停止监控"
echo ""

while true; do
    clear
    echo "🔄 Topic-1 消费者积压实时监控 - $(date '+%Y-%m-%d %H:%M:%S')"
    echo "================================================================"
    
    # 获取总积压情况
    echo "📊 消费者组总积压:"
    echo "-------------------"
    curl -s "http://localhost:9090/api/v1/query?query=sum%20by%20(consumer_group)%20(kafka_consumer_lag_messages%7Btopic%3D%22topic-1%22%7D)" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    for result in data['data']['result']:
        consumer_group = result['metric']['consumer_group']
        total_lag = int(float(result['value'][1]))
        if total_lag == 0:
            status = '🟢 正常'
        elif total_lag < 50:
            status = '🟡 轻微积压'
        elif total_lag < 100:
            status = '🟠 中等积压'
        else:
            status = '🔴 严重积压'
        print(f'{consumer_group:18} | {total_lag:3} 条 | {status}')
except:
    print('获取数据失败')
"
    
    echo ""
    echo "🚨 告警状态:"
    echo "-------------"
    
    # 检查严重积压
    severe_lag=$(curl -s "http://localhost:9090/api/v1/query?query=sum%20by%20(consumer_group)%20(kafka_consumer_lag_messages%7Btopic%3D%22topic-1%22%7D)%20%3E%2080" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    print(len(data['data']['result']))
except:
    print('0')
")
    
    # 检查中等积压
    medium_lag=$(curl -s "http://localhost:9090/api/v1/query?query=sum%20by%20(consumer_group)%20(kafka_consumer_lag_messages%7Btopic%3D%22topic-1%22%7D)%20%3E%2050" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    print(len(data['data']['result']))
except:
    print('0')
")
    
    if [ "$severe_lag" -gt 0 ]; then
        echo "🔴 严重告警: $severe_lag 个消费者组积压超过80条消息"
    elif [ "$medium_lag" -gt 0 ]; then
        echo "🟠 中等告警: $medium_lag 个消费者组积压超过50条消息"
    else
        echo "✅ 系统正常: 所有消费者组积压在可接受范围内"
    fi
    
    echo ""
    echo "📈 详细分区积压:"
    echo "----------------"
    curl -s "http://localhost:9090/api/v1/query?query=kafka_consumer_lag_messages%7Btopic%3D%22topic-1%22%7D" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    current_group = ''
    for result in data['data']['result']:
        consumer_group = result['metric']['consumer_group']
        partition = result['metric']['partition']
        lag = int(float(result['value'][1]))
        
        if consumer_group != current_group:
            if current_group != '':
                print()
            print(f'{consumer_group}:')
            current_group = consumer_group
        
        print(f'  分区{partition}: {lag:2} 条')
except:
    print('获取详细数据失败')
"
    
    echo ""
    echo "⏱️  下次更新: 10秒后 (按 Ctrl+C 停止)"
    sleep 10
done
