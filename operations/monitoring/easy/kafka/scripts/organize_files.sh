#!/bin/bash

# Kafka目录文件整理脚本
# 将相似文件合并，按功能分类组织

echo "🗂️  开始整理Kafka目录文件..."
echo "================================"

# 创建分类目录
mkdir -p {dashboards,configs,scripts,docs,logs,backups,generators}

echo "📁 创建目录结构完成"

# 1. 整理Dashboard文件
echo "📊 整理Dashboard文件..."
mv kafka-cluster-dashboard.json dashboards/
mv kafka-topic-dashboard.json dashboards/
mv kafka-enhanced-dashboard.json dashboards/
mv kafka-enhanced-system-dashboard.json dashboards/
mv kafka-dashboard-fixed.json dashboards/
mv kafka-current-dashboard.json dashboards/
mv kafka-dashboard.json dashboards/
mv kafka-topic-dashboard-part1.json dashboards/

# 2. 整理配置文件
echo "⚙️  整理配置文件..."
mv docker-compose.yml configs/
mv docker-compose-fixed.yml configs/
mv kafka-monitoring-compose.yml configs/
mv kafka-enhanced-compose.yml configs/
mv prometheus.yml configs/
mv prometheus-config.yml configs/
mv prometheus-enhanced.yml configs/
mv -r jmx-exporter configs/ 2>/dev/null || true

# 3. 整理脚本文件
echo "🔧 整理脚本文件..."
mv setup-kafka-monitoring.sh scripts/
mv deploy-enhanced-monitoring.sh scripts/
mv generate_kafka_data.sh scripts/
mv simple_message_generator.sh scripts/
mv realtime_lag_monitor.sh scripts/
mv monitor_consumer_lag.sh scripts/
mv organize_files.sh scripts/

# 4. 整理Python生成器和工具
echo "🐍 整理Python文件..."
mv kafka_consumer_lag_monitor.py scripts/
mv kafka_consumer_lag_exporter.py scripts/
mv simulate_kafka_load.py generators/
mv generate_enhanced_kafka_dashboard.py generators/
mv generate_enhanced_dashboard.py generators/
mv generate_topic_dashboard.py generators/
mv create_fixed_dashboard.py generators/
mv enhance_kafka_dashboard.py generators/
mv add_system_panels.py generators/
mv fix_network_io_dashboard.py generators/
mv test_dashboard_metrics.py generators/

# 5. 整理文档文件
echo "📚 整理文档文件..."
mv README.md docs/
mv DASHBOARD-GUIDE.md docs/
mv ENHANCED-MONITORING-GUIDE.md docs/
mv grafana-setup-guide.md docs/
mv kafka_prometheus_queries.md docs/
mv topic1_consumer_lag_queries.md docs/
mv consumption_report.md docs/

# 6. 整理日志和PID文件
echo "📋 整理日志文件..."
mv *.log logs/ 2>/dev/null || true
mv *.pid logs/ 2>/dev/null || true

# 7. 整理备份文件
echo "💾 整理备份文件..."
mv *.backup backups/ 2>/dev/null || true

echo ""
echo "✅ 文件整理完成！"
echo "=================="

# 显示整理后的目录结构
echo "📁 整理后的目录结构:"
echo ""
for dir in dashboards configs scripts generators docs logs backups; do
    if [ -d "$dir" ]; then
        echo "📂 $dir/"
        ls -1 "$dir" | sed 's/^/   ├── /'
        echo ""
    fi
done

echo "🎯 目录说明:"
echo "============"
echo "📊 dashboards/  - Grafana Dashboard JSON文件"
echo "⚙️  configs/     - Docker Compose和配置文件"
echo "🔧 scripts/     - Shell脚本和监控工具"
echo "🐍 generators/  - Python生成器和工具脚本"
echo "📚 docs/        - 文档和使用指南"
echo "📋 logs/        - 日志文件和PID文件"
echo "💾 backups/     - 备份文件"
