# Prometheus监控配置

## 描述
配置Prometheus监控系统，收集和分析应用程序和系统指标，实现基本的监控和告警功能。

## 要求
1. 配置Prometheus实现以下功能：
   - 目标发现和数据抓取
   - 基本的查询和过滤
   - 告警规则配置
   - 与Alertmanager集成
   - 数据可视化（使用Grafana）
   - 自定义指标导出器
   - 服务健康检查
   - 基本的数据存储配置
2. 监控不同类型的目标：
   - 主机系统（使用Node Exporter）
   - Web服务器（如Nginx或Apache）
   - 数据库（如MySQL或PostgreSQL）
   - 应用服务（如Java或Node.js应用）
3. 创建基本的告警规则
4. 配置Grafana仪表盘
5. 实现基本的高可用设置

## 输入
无特定输入，需要从头创建Prometheus配置。

## 期望输出
1. 完整的Prometheus配置文件
2. Alertmanager配置
3. 告警规则定义
4. 自定义指标导出器配置
5. Grafana仪表盘JSON
6. Docker Compose或类似的部署配置
7. 配置说明文档

## 评估标准
1. Prometheus配置的正确性
2. 监控覆盖的完整性
3. 告警规则的合理性
4. 可视化的有效性
5. 高可用性考虑
6. 配置的可维护性
7. 文档的清晰度和完整性