# Kafka监控环境 - 新主机部署包

## 📦 部署包内容
```
kafka-monitoring-deployment/
├── configs/                           # 配置文件
│   ├── docker-compose-new-host.yml    # 新主机Docker Compose配置
│   ├── prometheus-new-host.yml        # 新主机Prometheus配置
│   ├── docker-compose.yml             # 原始配置 (参考)
│   └── prometheus.yml                 # 原始配置 (参考)
├── scripts/                           # 脚本文件
│   ├── kafka_consumer_lag_monitor.py  # 消费者积压监控
│   └── simple_message_generator.sh    # 消息生成器
├── dashboards/                        # Grafana Dashboard
│   ├── kafka-dashboard-fixed.json     # 修复版Dashboard (推荐)
│   ├── kafka-cluster-dashboard.json   # 集群监控Dashboard
│   └── kafka-topic-dashboard.json     # Topic监控Dashboard
├── docs/                              # 文档
├── deploy.sh                          # 一键部署脚本
└── DEPLOYMENT-README.md               # 本文件
```

## 🚀 快速部署

### 前提条件
- Docker 和 Docker Compose 已安装
- Python3 已安装 (可选，用于消费者积压监控)
- 网络端口开放: 2181, 9092, 9090, 3000, 9308, 9309

### 一键部署
```bash
./deploy.sh
```

### 手动部署
1. 编辑配置文件，替换 YOUR_HOST_IP 为实际IP地址
2. 启动服务: `docker-compose -f configs/docker-compose-new-host.yml up -d`
3. 启动积压监控: `python3 scripts/kafka_consumer_lag_monitor.py &`

## 📊 导入Dashboard
1. 访问 Grafana: http://YOUR_HOST_IP:3000
2. 登录: admin/admin
3. 导入 dashboards/ 目录中的JSON文件

## 🎯 验证部署
- Kafka: telnet YOUR_HOST_IP 9092
- Prometheus: http://YOUR_HOST_IP:9090
- Grafana: http://YOUR_HOST_IP:3000

## 📚 详细文档
参考 docs/ 目录中的文档获取更多信息。
