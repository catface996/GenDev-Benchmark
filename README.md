# GenDev-Benchmark (Powered by Amazon Q)

GenDev-Benchmark是一个全面的基准测试集合，用于评估AI代码生成工具在不同场景下的性能和能力。本项目从运维、研发和测试三个维度，按照技术领域和难度级别组织案例，帮助评估和比较不同的AI代码生成工具。

## 文件目录

```
GenDev-Benchmark/
├── README.md                                 # 项目主文档
├── development/                              # 研发相关案例
│   ├── README.md                             # 研发维度说明
│   ├── algorithm/                            # 算法案例
│   │   ├── easy/                             # 低难度算法案例
│   │   ├── medium/                           # 中难度算法案例
│   │   └── hard/                             # 高难度算法案例
│   ├── backend/                              # 后端开发案例
│   │   ├── easy/                             # 低难度后端案例
│   │   ├── medium/                           # 中难度后端案例
│   │   └── hard/                             # 高难度后端案例
│   ├── database/                             # 数据库案例
│   │   ├── easy/                             # 低难度数据库案例
│   │   ├── medium/                           # 中难度数据库案例
│   │   └── hard/                             # 高难度数据库案例
│   ├── frontend/                             # 前端开发案例
│   │   ├── easy/                             # 低难度前端案例
│   │   ├── medium/                           # 中难度前端案例
│   │   └── hard/                             # 高难度前端案例
│   └── middleware/                           # 中间件案例
│       ├── easy/                             # 低难度中间件案例
│       ├── medium/                           # 中难度中间件案例
│       └── hard/                             # 高难度中间件案例
├── testing/                                  # 测试相关案例
│   ├── README.md                             # 测试维度说明
│   ├── e2e/                                  # 端到端测试案例
│   │   ├── easy/                             # 低难度端到端测试案例
│   │   ├── medium/                           # 中难度端到端测试案例
│   │   └── hard/                             # 高难度端到端测试案例
│   ├── integration/                          # 集成测试案例
│   │   ├── easy/                             # 低难度集成测试案例
│   │   ├── medium/                           # 中难度集成测试案例
│   │   └── hard/                             # 高难度集成测试案例
│   ├── performance/                          # 性能测试案例
│   │   ├── easy/                             # 低难度性能测试案例
│   │   ├── medium/                           # 中难度性能测试案例
│   │   └── hard/                             # 高难度性能测试案例
│   └── unit/                                 # 单元测试案例
│       ├── easy/                             # 低难度单元测试案例
│       ├── medium/                           # 中难度单元测试案例
│       └── hard/                             # 高难度单元测试案例
└── operations/                               # 运维相关案例
    ├── README.md                             # 运维维度说明
    ├── cicd/                                 # CI/CD流水线案例
    │   ├── easy/                             # 低难度CI/CD案例
    │   ├── medium/                           # 中难度CI/CD案例
    │   └── hard/                             # 高难度CI/CD案例
    ├── container/                            # 容器化技术案例
    │   ├── easy/                             # 低难度容器案例
    │   ├── medium/                           # 中难度容器案例
    │   └── hard/                             # 高难度容器案例
    ├── infrastructure/                       # 基础设施即代码案例
    │   ├── easy/                             # 低难度基础设施案例
    │   ├── medium/                           # 中难度基础设施案例
    │   └── hard/                             # 高难度基础设施案例
    ├── monitoring/                           # 监控和日志案例
    │   ├── easy/                             # 低难度监控案例
    │   ├── medium/                           # 中难度监控案例
    │   └── hard/                             # 高难度监控案例
    └── security/                             # 安全运维案例
        ├── easy/                             # 低难度安全运维案例
        ├── medium/                           # 中难度安全运维案例
        └── hard/                             # 高难度安全运维案例
```

## 文档导航

### 维度说明文档
- [研发维度说明](development/README.md)
- [测试维度说明](testing/README.md)
- [运维维度说明](operations/README.md)

### 运维维度案例

#### 容器化技术
- **低难度**：
  - [简单Docker容器部署](operations/container/easy/simple_docker_deployment.md)
  - [Docker Compose基础应用部署](operations/container/easy/docker_compose_basics.md)
  - [Docker数据卷管理与备份](operations/container/easy/docker_volume_management.md)
  - [Docker网络基础配置](operations/container/easy/docker_networking_basics.md)
  - [容器镜像仓库搭建与配置](operations/container/easy/container_registry_setup.md)
- **中难度**：
  - [Kubernetes基础部署与配置](operations/container/medium/kubernetes_deployment.md)
  - [Docker Swarm集群编排与管理](operations/container/medium/docker_swarm_orchestration.md)
  - [容器安全实现与最佳实践](operations/container/medium/container_security_implementation.md)
- **高难度**：
  - [微服务架构部署与管理](operations/container/hard/microservices_deployment.md)
  - [Kubernetes Operator开发与部署](operations/container/hard/kubernetes_operator_development.md)
  - [服务网格架构实现与管理](operations/container/hard/service_mesh_implementation.md)

#### CI/CD流水线
- **低难度**：
  - [GitHub Actions基础配置](operations/cicd/easy/github_actions_basic.md)
  - [Jenkins基础配置与使用](operations/cicd/easy/jenkins_basic_setup.md)
- **中难度**：
  - [CI/CD流水线配置](operations/cicd/medium/cicd_pipeline_setup.md)
  - [持续部署流水线实现](operations/cicd/medium/continuous_deployment_pipeline.md)
  - [制品管理系统配置与使用](operations/cicd/medium/artifact_management_system.md)
- **高难度**：
  - [多环境CI/CD流水线设计与实现](operations/cicd/hard/multi_environment_pipeline.md)

#### 基础设施即代码
- **低难度**：
  - [运维基础环境搭建](operations/infrastructure/easy/ops_environment_setup.md)
  - [Ansible基础自动化配置](operations/infrastructure/easy/ansible_automation.md)
  - [Vagrant开发环境自动化配置](operations/infrastructure/easy/vagrant_dev_environment.md)
  - [云存储服务配置与管理](operations/infrastructure/easy/cloud_storage_management.md)
- **中难度**：
  - [Terraform AWS基础设施自动化](operations/infrastructure/medium/terraform_aws_infrastructure.md)
  - [配置管理系统实现](operations/infrastructure/medium/configuration_management.md)
  - [灾难恢复方案设计与实施](operations/infrastructure/medium/disaster_recovery_planning.md)
- **高难度**：
  - [多云环境基础设施设计与实现](operations/infrastructure/hard/multi_cloud_infrastructure.md)

#### 监控和日志
- **低难度**：
  - [Prometheus和Grafana基础监控配置](operations/monitoring/easy/prometheus_grafana_setup.md)
  - [系统监控基础配置](operations/monitoring/easy/system_monitoring_basics.md)
  - [日志轮转与管理配置](operations/monitoring/easy/log_rotation_setup.md)
- **中难度**：
  - [ELK Stack日志分析系统实现](operations/monitoring/medium/elk_stack_implementation.md)
  - [指标可视化仪表板设计](operations/monitoring/medium/metrics_visualization_dashboard.md)
  - [告警系统设计与实现](operations/monitoring/medium/alerting_system_implementation.md)
- **高难度**：
  - [分布式追踪与可观测性平台设计](operations/monitoring/hard/distributed_tracing_platform.md)

#### 安全运维
- **低难度**：
  - [服务器安全加固配置](operations/security/easy/security_hardening.md)
  - [防火墙规则配置与管理](operations/security/easy/firewall_configuration.md)
  - [SSL证书管理与自动更新](operations/security/easy/ssl_certificate_management.md)
  - [用户访问管理与权限控制](operations/security/easy/user_access_management.md)
- **中难度**：
  - [DevSecOps流水线实现](operations/security/medium/devsecops_pipeline.md)
  - [漏洞管理系统实现](operations/security/medium/vulnerability_management_system.md)
  - [安全监控系统设计与实现](operations/security/medium/security_monitoring_system.md)
- **高难度**：
  - [零信任安全架构设计与实现](operations/security/hard/zero_trust_architecture.md)

## 项目概述

GenDev-Benchmark项目旨在提供一套全面的基准测试案例，用于评估AI代码生成工具在不同场景下的性能和能力。项目从三个维度组织案例：

1. **研发维度**：评估AI工具在前端、后端、中间件、数据库和算法等领域的代码生成能力
2. **测试维度**：评估AI工具在单元测试、集成测试、端到端测试等领域的测试代码生成能力
3. **运维维度**：评估AI工具在容器化、CI/CD、监控等DevOps领域的配置和脚本生成能力

每个维度下，案例按照技术领域和难度级别（低、中、高）进行分类，帮助用户全面评估不同AI工具的能力。

## 评估标准

每个案例将从以下几个方面进行评估：

1. **正确性**：生成代码的功能正确性
2. **完整性**：解决方案的完整程度
3. **效率**：代码执行效率和资源利用
4. **可维护性**：代码结构、命名和文档
5. **创新性**：解决问题的创新方法和思路

## 使用方法

1. 选择要评估的维度、技术领域和难度级别
2. 查看对应目录下的案例描述和要求
3. 使用AI代码生成工具生成解决方案
4. 根据评估标准对生成的代码进行评分
5. 比较不同工具在各个维度的表现

## 贡献指南

欢迎贡献新的基准测试案例！请遵循以下步骤：

1. Fork本仓库
2. 创建新的分支
3. 添加您的案例到相应的目录
4. 提交Pull Request

## 许可证

MIT