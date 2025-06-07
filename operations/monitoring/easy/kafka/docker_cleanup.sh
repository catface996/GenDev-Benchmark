#!/bin/bash

# Docker环境清理脚本
# 提供多种清理选项，从温和到彻底

echo "🧹 Docker环境清理工具"
echo "===================="

# 显示当前状态
show_current_status() {
    echo "📊 当前Docker环境状态:"
    echo "======================"
    echo "运行中的容器: $(docker ps -q | wc -l)"
    echo "所有容器: $(docker ps -aq | wc -l)"
    echo "镜像数量: $(docker images -q | wc -l)"
    echo "数据卷: $(docker volume ls -q | wc -l)"
    echo "网络: $(docker network ls -q | wc -l)"
    echo ""
    docker system df
    echo ""
}

# 选项1: 温和清理 - 只清理停止的容器和未使用的镜像
gentle_cleanup() {
    echo "🧽 执行温和清理..."
    echo "=================="
    
    echo "1. 清理停止的容器:"
    docker container prune -f
    
    echo ""
    echo "2. 清理未使用的镜像:"
    docker image prune -f
    
    echo ""
    echo "3. 清理未使用的网络:"
    docker network prune -f
    
    echo ""
    echo "✅ 温和清理完成"
}

# 选项2: 标准清理 - 清理所有未使用的资源
standard_cleanup() {
    echo "🧼 执行标准清理..."
    echo "=================="
    
    echo "1. 清理所有未使用的资源:"
    docker system prune -f
    
    echo ""
    echo "2. 清理未使用的数据卷:"
    docker volume prune -f
    
    echo ""
    echo "✅ 标准清理完成"
}

# 选项3: 深度清理 - 包括未使用的镜像
deep_cleanup() {
    echo "🧽 执行深度清理..."
    echo "=================="
    
    echo "1. 清理所有未使用的资源 (包括镜像):"
    docker system prune -a -f
    
    echo ""
    echo "2. 清理所有未使用的数据卷:"
    docker volume prune -f
    
    echo ""
    echo "✅ 深度清理完成"
}

# 选项4: 完全清理 - 停止所有容器并清理一切
complete_cleanup() {
    echo "🗑️  执行完全清理..."
    echo "=================="
    
    echo "⚠️  警告: 这将停止所有容器并删除所有Docker资源!"
    read -p "确定要继续吗? (输入 'YES' 确认): " confirm
    
    if [ "$confirm" = "YES" ]; then
        echo ""
        echo "1. 停止所有运行的容器:"
        docker stop $(docker ps -q) 2>/dev/null || echo "没有运行的容器"
        
        echo ""
        echo "2. 删除所有容器:"
        docker rm $(docker ps -aq) 2>/dev/null || echo "没有容器需要删除"
        
        echo ""
        echo "3. 删除所有镜像:"
        docker rmi $(docker images -q) 2>/dev/null || echo "没有镜像需要删除"
        
        echo ""
        echo "4. 删除所有数据卷:"
        docker volume rm $(docker volume ls -q) 2>/dev/null || echo "没有数据卷需要删除"
        
        echo ""
        echo "5. 删除所有网络 (除了默认网络):"
        docker network rm $(docker network ls -q) 2>/dev/null || echo "没有自定义网络需要删除"
        
        echo ""
        echo "6. 清理系统:"
        docker system prune -a -f --volumes
        
        echo ""
        echo "✅ 完全清理完成"
    else
        echo "❌ 完全清理已取消"
    fi
}

# 选项5: 选择性清理Kafka相关容器
kafka_cleanup() {
    echo "☕ 清理Kafka相关容器..."
    echo "====================="
    
    echo "当前Kafka相关容器:"
    docker ps -a --filter "name=kafka" --filter "name=zookeeper" --filter "name=prometheus" --filter "name=grafana" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
    
    echo ""
    read -p "是否停止并删除这些容器? (y/n): " confirm
    
    if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
        echo ""
        echo "停止Kafka相关容器:"
        docker stop kafka zookeeper prometheus grafana kafka-exporter 2>/dev/null || echo "部分容器可能已停止"
        
        echo ""
        echo "删除Kafka相关容器:"
        docker rm kafka zookeeper prometheus grafana kafka-exporter 2>/dev/null || echo "部分容器可能已删除"
        
        echo ""
        echo "删除Kafka相关镜像 (可选):"
        read -p "是否也删除相关镜像? (y/n): " img_confirm
        if [ "$img_confirm" = "y" ] || [ "$img_confirm" = "Y" ]; then
            docker rmi confluentinc/cp-kafka:7.4.0 confluentinc/cp-zookeeper:7.4.0 prom/prometheus:latest grafana/grafana:latest danielqsj/kafka-exporter:latest 2>/dev/null || echo "部分镜像可能已删除"
        fi
        
        echo ""
        echo "✅ Kafka环境清理完成"
    else
        echo "❌ Kafka清理已取消"
    fi
}

# 主菜单
main_menu() {
    show_current_status
    
    echo "🛠️  清理选项:"
    echo "============"
    echo "1. 温和清理 - 只清理停止的容器和未使用的镜像"
    echo "2. 标准清理 - 清理所有未使用的资源"
    echo "3. 深度清理 - 包括未使用的镜像"
    echo "4. 完全清理 - 停止所有容器并清理一切 (危险)"
    echo "5. Kafka清理 - 只清理Kafka相关容器"
    echo "6. 查看状态 - 重新显示当前状态"
    echo "0. 退出"
    echo ""
    
    read -p "请选择清理选项 (0-6): " choice
    
    case $choice in
        1)
            gentle_cleanup
            ;;
        2)
            standard_cleanup
            ;;
        3)
            deep_cleanup
            ;;
        4)
            complete_cleanup
            ;;
        5)
            kafka_cleanup
            ;;
        6)
            main_menu
            ;;
        0)
            echo "👋 退出清理工具"
            exit 0
            ;;
        *)
            echo "❌ 无效选项，请重新选择"
            main_menu
            ;;
    esac
    
    echo ""
    echo "📊 清理后状态:"
    show_current_status
    
    read -p "是否继续其他清理操作? (y/n): " continue_choice
    if [ "$continue_choice" = "y" ] || [ "$continue_choice" = "Y" ]; then
        main_menu
    else
        echo "👋 清理完成，退出工具"
    fi
}

# 运行主菜单
main_menu
