# Kafka监控环境

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
