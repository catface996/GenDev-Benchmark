#!/usr/bin/env python3
"""
合并相似文件的脚本
将功能相似的Dashboard和配置文件进行合并
"""

import json
import os
import shutil

def merge_dashboards():
    """合并相似的Dashboard文件"""
    print("📊 合并Dashboard文件...")
    
    # 保留的主要Dashboard文件
    main_dashboards = {
        "kafka-cluster-dashboard.json": "集群级监控Dashboard",
        "kafka-topic-dashboard.json": "Topic级监控Dashboard (带选择器)",
        "kafka-dashboard-fixed.json": "修复版Dashboard (推荐使用)"
    }
    
    # 移除重复或过时的Dashboard
    redundant_dashboards = [
        "kafka-dashboard.json",  # 被修复版替代
        "kafka-current-dashboard.json",  # 被修复版替代
        "kafka-enhanced-dashboard.json",  # 功能重复
        "kafka-enhanced-system-dashboard.json",  # 功能重复
        "kafka-topic-dashboard-part1.json"  # 不完整版本
    ]
    
    dashboard_dir = "dashboards"
    archive_dir = "dashboards/archive"
    os.makedirs(archive_dir, exist_ok=True)
    
    for dashboard in redundant_dashboards:
        src = os.path.join(dashboard_dir, dashboard)
        dst = os.path.join(archive_dir, dashboard)
        if os.path.exists(src):
            shutil.move(src, dst)
            print(f"   归档: {dashboard}")
    
    print(f"✅ 保留 {len(main_dashboards)} 个主要Dashboard")
    for dashboard, desc in main_dashboards.items():
        print(f"   📊 {dashboard} - {desc}")

def merge_configs():
    """合并配置文件"""
    print("\n⚙️  合并配置文件...")
    
    # 保留的主要配置文件
    main_configs = {
        "docker-compose.yml": "当前使用的Docker Compose配置",
        "prometheus.yml": "当前使用的Prometheus配置"
    }
    
    # 移除重复的配置文件
    redundant_configs = [
        "docker-compose-fixed.yml",  # 与主配置重复
        "kafka-monitoring-compose.yml",  # 旧版本
        "kafka-enhanced-compose.yml",  # 功能重复
        "prometheus-config.yml",  # 与主配置重复
        "prometheus-enhanced.yml"  # 功能重复
    ]
    
    config_dir = "configs"
    archive_dir = "configs/archive"
    os.makedirs(archive_dir, exist_ok=True)
    
    for config in redundant_configs:
        src = os.path.join(config_dir, config)
        dst = os.path.join(archive_dir, config)
        if os.path.exists(src):
            shutil.move(src, dst)
            print(f"   归档: {config}")
    
    print(f"✅ 保留 {len(main_configs)} 个主要配置文件")
    for config, desc in main_configs.items():
        print(f"   ⚙️  {config} - {desc}")

def merge_generators():
    """合并生成器脚本"""
    print("\n🐍 合并生成器脚本...")
    
    # 保留的主要生成器
    main_generators = {
        "simulate_kafka_load.py": "Kafka负载模拟器",
        "test_dashboard_metrics.py": "Dashboard指标测试工具"
    }
    
    # 移除重复的生成器
    redundant_generators = [
        "generate_enhanced_kafka_dashboard.py",
        "generate_enhanced_dashboard.py", 
        "generate_topic_dashboard.py",
        "create_fixed_dashboard.py",
        "enhance_kafka_dashboard.py",
        "add_system_panels.py",
        "fix_network_io_dashboard.py"
    ]
    
    generator_dir = "generators"
    archive_dir = "generators/archive"
    os.makedirs(archive_dir, exist_ok=True)
    
    for generator in redundant_generators:
        src = os.path.join(generator_dir, generator)
        dst = os.path.join(archive_dir, generator)
        if os.path.exists(src):
            shutil.move(src, dst)
            print(f"   归档: {generator}")
    
    print(f"✅ 保留 {len(main_generators)} 个主要生成器")
    for generator, desc in main_generators.items():
        print(f"   🐍 {generator} - {desc}")

def merge_docs():
    """合并文档文件"""
    print("\n📚 合并文档文件...")
    
    # 保留的主要文档
    main_docs = {
        "README.md": "主要使用说明",
        "DASHBOARD-GUIDE.md": "Dashboard使用指南"
    }
    
    # 移除重复的文档
    redundant_docs = [
        "ENHANCED-MONITORING-GUIDE.md",  # 内容重复
        "grafana-setup-guide.md",  # 内容重复
        "consumption_report.md",  # 临时报告
        "topic1_consumer_lag_queries.md"  # 特定查询
    ]
    
    doc_dir = "docs"
    archive_dir = "docs/archive"
    os.makedirs(archive_dir, exist_ok=True)
    
    for doc in redundant_docs:
        src = os.path.join(doc_dir, doc)
        dst = os.path.join(archive_dir, doc)
        if os.path.exists(src):
            shutil.move(src, dst)
            print(f"   归档: {doc}")
    
    print(f"✅ 保留 {len(main_docs)} 个主要文档")
    for doc, desc in main_docs.items():
        print(f"   📚 {doc} - {desc}")

def create_main_readme():
    """创建主要的README文件"""
    print("\n📝 创建主要README文件...")
    
    readme_content = """# Kafka监控环境

## 🎯 概述
这是一个完整的Kafka监控解决方案，包含Dashboard、配置文件、脚本和文档。

## 📁 目录结构
```
~/Desktop/Kafka/
├── dashboards/          # Grafana Dashboard文件
│   ├── kafka-cluster-dashboard.json      # 集群级监控
│   ├── kafka-topic-dashboard.json        # Topic级监控 (推荐)
│   └── kafka-dashboard-fixed.json        # 修复版Dashboard
├── configs/             # 配置文件
│   ├── docker-compose.yml               # Docker Compose配置
│   ├── prometheus.yml                   # Prometheus配置
│   └── jmx-exporter/                   # JMX Exporter配置
├── scripts/             # 脚本文件
│   ├── deploy-enhanced-monitoring.sh    # 部署脚本
│   ├── simple_message_generator.sh      # 消息生成器
│   └── kafka_consumer_lag_monitor.py    # 积压监控器
├── generators/          # 工具生成器
│   ├── simulate_kafka_load.py           # 负载模拟器
│   └── test_dashboard_metrics.py        # 指标测试工具
├── docs/               # 文档
│   ├── README.md                        # 主要说明
│   ├── DASHBOARD-GUIDE.md               # Dashboard指南
│   └── kafka_prometheus_queries.md      # Prometheus查询
├── logs/               # 日志文件
└── backups/            # 备份文件
```

## 🚀 快速开始

### 1. 启动监控环境
```bash
cd ~/Desktop/Kafka
docker-compose -f configs/docker-compose.yml up -d
```

### 2. 启动消费者积压监控
```bash
python3 scripts/kafka_consumer_lag_monitor.py &
```

### 3. 生成测试数据
```bash
./scripts/simple_message_generator.sh
```

### 4. 导入Dashboard
1. 访问Grafana: http://localhost:3000 (admin/admin)
2. 导入Dashboard文件:
   - `dashboards/kafka-cluster-dashboard.json` (集群监控)
   - `dashboards/kafka-topic-dashboard.json` (Topic监控)
   - `dashboards/kafka-dashboard-fixed.json` (修复版)

## 📊 推荐的Dashboard使用顺序

1. **kafka-cluster-dashboard.json** - 查看集群整体状况
2. **kafka-topic-dashboard.json** - 深入分析特定Topic
3. **kafka-dashboard-fixed.json** - 查看网络IO和系统指标

## 🔗 访问地址
- Grafana: http://localhost:3000
- Prometheus: http://localhost:9090
- Kafka: localhost:9092

## 📚 详细文档
- [Dashboard使用指南](docs/DASHBOARD-GUIDE.md)
- [Prometheus查询](docs/kafka_prometheus_queries.md)

## 🛠️ 工具脚本
- `generators/simulate_kafka_load.py` - 生成各种类型的Kafka负载
- `generators/test_dashboard_metrics.py` - 验证Dashboard指标
- `scripts/simple_message_generator.sh` - 简单消息生成器

## 📋 注意事项
- 确保Docker和Docker Compose已安装
- 默认端口: Kafka(9092), Prometheus(9090), Grafana(3000)
- 消费者积压监控端口: 9309

## 🎉 开始监控
环境启动后，即可在Grafana中查看实时的Kafka监控数据！
"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print("✅ 主要README文件已创建")

if __name__ == "__main__":
    print("🗂️  开始合并相似文件...")
    print("=" * 40)
    
    merge_dashboards()
    merge_configs()
    merge_generators()
    merge_docs()
    create_main_readme()
    
    print("\n" + "=" * 40)
    print("✅ 文件合并完成！")
    print("\n📊 最终保留的主要文件:")
    print("• 3个Dashboard文件 (集群、Topic、修复版)")
    print("• 2个配置文件 (Docker Compose、Prometheus)")
    print("• 2个生成器工具 (负载模拟、指标测试)")
    print("• 2个主要文档 (README、Dashboard指南)")
    print("\n🗃️  重复文件已归档到各自的archive目录")
    print("💡 建议使用修复版Dashboard获得最佳监控体验")
