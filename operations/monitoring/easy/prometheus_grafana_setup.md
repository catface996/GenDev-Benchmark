# Prometheus和Grafana基础监控配置

## 描述

本案例要求配置基础的Prometheus和Grafana监控系统，用于监控一个简单的Web应用及其主机资源。

## 要求

1. 使用Docker Compose部署Prometheus和Grafana
2. 配置Prometheus监控以下指标:
   - 主机CPU、内存、磁盘和网络使用情况
   - Web应用的HTTP请求数、响应时间和错误率
3. 配置Grafana连接Prometheus数据源
4. 创建以下Grafana仪表板:
   - 主机资源监控仪表板
   - Web应用性能监控仪表板
5. 配置基本的告警规则:
   - 当CPU使用率超过80%时发出告警
   - 当内存使用率超过80%时发出告警
   - 当HTTP错误率超过5%时发出告警

## 输入

- 一个简单的Web应用，已经集成了Prometheus客户端库
- 应用暴露在`:8080/metrics`端点提供Prometheus格式的指标
- 主机可以使用Node Exporter收集系统指标

## 预期输出

1. 完整的Docker Compose配置文件
2. Prometheus配置文件，包括抓取配置和告警规则
3. Grafana数据源配置
4. Grafana仪表板JSON定义
5. 简要的部署和使用文档

## 评估标准

1. **配置正确性**: Prometheus和Grafana配置是否正确
2. **完整性**: 是否监控了所有要求的指标
3. **可视化质量**: Grafana仪表板是否清晰有效
4. **告警配置**: 告警规则是否合理
5. **可维护性**: 配置是否易于维护和扩展
6. **文档质量**: 部署和使用文档是否清晰完整

## 难度

低

## 技能点

- Prometheus基础
- Grafana基础
- Docker Compose
- 监控指标配置
- 可视化仪表板设计
- 基本告警配置