#!/bin/bash

# 创建新主机部署包脚本
# 将必要文件打包，用于在另一台主机上部署Kafka监控环境

echo "📦 创建Kafka监控环境部署包..."
echo "================================"

# 创建部署包目录
DEPLOY_DIR="kafka-monitoring-deployment"
rm -rf $DEPLOY_DIR
mkdir -p $DEPLOY_DIR/{configs,scripts,dashboards,docs}

echo "📁 创建部署包目录结构..."

# 1. 复制配置文件
echo "⚙️  复制配置文件..."
cp configs/docker-compose.yml $DEPLOY_DIR/configs/
cp configs/prometheus.yml $DEPLOY_DIR/configs/
cp -r jmx-exporter $DEPLOY_DIR/configs/ 2>/dev/null || echo "   JMX Exporter目录不存在，跳过"

# 2. 复制关键脚本
echo "🔧 复制脚本文件..."
cp scripts/kafka_consumer_lag_monitor.py $DEPLOY_DIR/scripts/
cp scripts/simple_message_generator.sh $DEPLOY_DIR/scripts/
cp scripts/deploy-enhanced-monitoring.sh $DEPLOY_DIR/scripts/ 2>/dev/null || echo "   部署脚本不存在，跳过"

# 3. 复制Dashboard文件
echo "📊 复制Dashboard文件..."
cp dashboards/kafka-dashboard-fixed.json $DEPLOY_DIR/dashboards/
cp dashboards/kafka-cluster-dashboard.json $DEPLOY_DIR/dashboards/
cp dashboards/kafka-topic-dashboard.json $DEPLOY_DIR/dashboards/

# 4. 复制文档
echo "📚 复制文档文件..."
cp README.md $DEPLOY_DIR/
cp QUICK-START.md $DEPLOY_DIR/
cp docs/DASHBOARD-GUIDE.md $DEPLOY_DIR/docs/
cp deployment-analysis.md $DEPLOY_DIR/docs/

# 5. 创建新主机专用的配置文件
echo "🔧 创建新主机专用配置..."

# 创建适用于新主机的docker-compose.yml
cat > $DEPLOY_DIR/configs/docker-compose-new-host.yml << 'EOF'
networks:
  kafka-network:
    driver: bridge

services:
  zookeeper:
    image: confluentinc/cp-zookeeper:7.4.0
    hostname: zookeeper
    container_name: zookeeper
    ports:
      - "2181:2181"
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    networks:
      - kafka-network
    restart: unless-stopped

  kafka:
    image: confluentinc/cp-kafka:7.4.0
    hostname: kafka
    container_name: kafka
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
      - "9101:9101"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: 'zookeeper:2181'
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
      # 注意: 需要将 localhost 替换为实际的主机IP地址
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:29092,PLAINTEXT_HOST://YOUR_HOST_IP:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1
      KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS: 0
      KAFKA_JMX_PORT: 9101
      KAFKA_JMX_HOSTNAME: YOUR_HOST_IP
    networks:
      - kafka-network
    restart: unless-stopped

  kafka-exporter:
    image: danielqsj/kafka-exporter:latest
    container_name: kafka-exporter
    depends_on:
      - kafka
    ports:
      - "9308:9308"
    command:
      - --kafka.server=kafka:29092
      - --kafka.version=2.6.0
      - --log.level=info
      - --web.listen-address=:9308
    networks:
      - kafka-network
    restart: unless-stopped

  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus-new-host.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
      - '--storage.tsdb.retention.time=200h'
      - '--web.enable-lifecycle'
    networks:
      - kafka-network
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana
    networks:
      - kafka-network
    restart: unless-stopped

volumes:
  prometheus_data:
  grafana_data:
EOF

# 创建适用于新主机的prometheus配置
cat > $DEPLOY_DIR/configs/prometheus-new-host.yml << 'EOF'
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'kafka-exporter'
    static_configs:
      - targets: ['kafka-exporter:9308']
    scrape_interval: 30s

  - job_name: 'kafka-jmx'
    static_configs:
      - targets: ['kafka:8080']
    scrape_interval: 30s

  # 消费者积压监控 - 需要根据实际情况调整
  - job_name: 'kafka-consumer-lag'
    static_configs:
      - targets: ['YOUR_HOST_IP:9309']
    scrape_interval: 30s
EOF

# 6. 创建部署脚本
echo "🚀 创建部署脚本..."

cat > $DEPLOY_DIR/deploy.sh << 'EOF'
#!/bin/bash

# Kafka监控环境新主机部署脚本

echo "🚀 Kafka监控环境部署脚本"
echo "========================"

# 检查Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker未安装，请先安装Docker"
    exit 1
fi

if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose未安装，请先安装Docker Compose"
    exit 1
fi

# 获取主机IP
HOST_IP=$(hostname -I | awk '{print $1}' 2>/dev/null || ip route get 1 | awk '{print $7}' | head -1 2>/dev/null || echo "localhost")
echo "🔍 检测到主机IP: $HOST_IP"

# 询问是否使用检测到的IP
read -p "是否使用检测到的IP地址 $HOST_IP? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    read -p "请输入正确的主机IP地址: " HOST_IP
fi

echo "✅ 使用主机IP: $HOST_IP"

# 替换配置文件中的占位符
echo "⚙️  配置网络地址..."
sed -i.bak "s/YOUR_HOST_IP/$HOST_IP/g" configs/docker-compose-new-host.yml
sed -i.bak "s/YOUR_HOST_IP/$HOST_IP/g" configs/prometheus-new-host.yml

# 启动服务
echo "🚀 启动Kafka监控服务..."
docker-compose -f configs/docker-compose-new-host.yml up -d

echo "⏳ 等待服务启动..."
sleep 20

# 检查服务状态
echo "🔍 检查服务状态:"
docker-compose -f configs/docker-compose-new-host.yml ps

# 启动消费者积压监控
if [ -f "scripts/kafka_consumer_lag_monitor.py" ]; then
    echo "🔄 启动消费者积压监控..."
    if command -v python3 &> /dev/null; then
        nohup python3 scripts/kafka_consumer_lag_monitor.py > consumer_lag_monitor.log 2>&1 &
        echo $! > consumer_lag_monitor.pid
        echo "✅ 消费者积压监控已启动"
    else
        echo "⚠️  Python3未安装，跳过消费者积压监控"
    fi
fi

echo ""
echo "🎉 Kafka监控环境部署完成！"
echo "=========================="
echo ""
echo "🔗 访问地址:"
echo "• Kafka: $HOST_IP:9092"
echo "• Prometheus: http://$HOST_IP:9090"
echo "• Grafana: http://$HOST_IP:3000 (admin/admin)"
echo ""
echo "📊 下一步:"
echo "1. 访问Grafana导入Dashboard文件"
echo "2. 运行测试脚本生成数据: ./scripts/simple_message_generator.sh"
echo "3. 查看监控数据"
echo ""
echo "🛑 停止服务: docker-compose -f configs/docker-compose-new-host.yml down"
EOF

chmod +x $DEPLOY_DIR/deploy.sh

# 7. 创建README文件
cat > $DEPLOY_DIR/DEPLOYMENT-README.md << 'EOF'
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
EOF

echo ""
echo "✅ 部署包创建完成！"
echo "==================="
echo "📦 部署包位置: $DEPLOY_DIR/"
echo "📋 包含文件:"
find $DEPLOY_DIR -type f | sort

echo ""
echo "🚀 使用方法:"
echo "1. 将整个 $DEPLOY_DIR 目录复制到新主机"
echo "2. 在新主机上运行: cd $DEPLOY_DIR && ./deploy.sh"
echo "3. 按提示输入主机IP地址"
echo "4. 等待部署完成"
echo ""
echo "📊 预计部署时间: 5-10分钟"
