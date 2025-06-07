# Ubuntu虚拟机Kafka监控环境部署指南

## 🎯 部署概览
在Ubuntu虚拟机 (172.16.12.130) 上部署完整的Kafka监控环境

## ✅ 当前状态
- ✅ 免密SSH登录已设置
- ✅ 部署包已传输到虚拟机
- ⚠️  需要安装Docker和Docker Compose
- ⚠️  需要配置网络设置

## 🚀 部署步骤

### 步骤1: 安装Docker (在虚拟机上执行)
```bash
# SSH到虚拟机
ssh catface@172.16.12.130

# 执行Docker安装脚本
chmod +x /tmp/install_docker.sh
/tmp/install_docker.sh

# 重新登录以使docker组权限生效
exit
ssh catface@172.16.12.130

# 验证Docker安装
docker --version
docker compose version
```

### 步骤2: 部署Kafka监控环境
```bash
# 进入部署目录
cd kafka-monitoring-deployment/

# 执行一键部署脚本
./deploy.sh

# 脚本会自动:
# 1. 检测主机IP (172.16.12.130)
# 2. 配置网络设置
# 3. 启动所有服务
# 4. 启动消费者积压监控
```

### 步骤3: 验证部署
```bash
# 运行验证脚本
./verify-deployment.sh

# 手动检查服务状态
docker compose -f configs/docker-compose-new-host.yml ps
```

### 步骤4: 访问监控界面
- **Grafana**: http://172.16.12.130:3000 (admin/admin)
- **Prometheus**: http://172.16.12.130:9090
- **Kafka**: 172.16.12.130:9092

### 步骤5: 导入Dashboard
1. 访问Grafana: http://172.16.12.130:3000
2. 登录: admin/admin
3. 导入Dashboard文件:
   - `dashboards/kafka-dashboard-fixed.json` (推荐)
   - `dashboards/kafka-cluster-dashboard.json`
   - `dashboards/kafka-topic-dashboard.json`

### 步骤6: 生成测试数据
```bash
# 运行消息生成器
./scripts/simple_message_generator.sh
```

## 🔧 故障排除

### Docker权限问题
```bash
# 如果遇到权限问题，重新登录
exit
ssh catface@172.16.12.130
```

### 端口占用问题
```bash
# 检查端口占用
sudo netstat -tlnp | grep -E ':(2181|9092|9090|3000|9308|9309)'

# 停止冲突服务
sudo systemctl stop <service-name>
```

### 服务启动失败
```bash
# 查看日志
docker compose -f configs/docker-compose-new-host.yml logs

# 重启服务
docker compose -f configs/docker-compose-new-host.yml restart
```

## 📊 预期结果
- ✅ Kafka集群运行在 172.16.12.130:9092
- ✅ Prometheus监控运行在 172.16.12.130:9090
- ✅ Grafana界面运行在 172.16.12.130:3000
- ✅ 3个专业Dashboard可用
- ✅ 消费者积压监控正常
- ✅ 测试数据生成正常

## 🎉 完成后的验证
1. 访问Grafana查看Dashboard
2. 在Prometheus中查询Kafka指标
3. 使用Kafka客户端连接测试
4. 观察消费者积压监控数据

## 📞 支持
如遇问题，可以查看:
- 部署日志: `docker compose logs`
- 系统日志: `journalctl -u docker`
- 网络状态: `netstat -tlnp`
