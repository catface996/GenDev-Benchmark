# GenDev-Benchmark

GenDev-Benchmark是一个全面的基准测试集合，用于评估AI代码生成工具在不同场景下的性能和能力。本项目从运维、研发和测试三个维度，按照技术领域和难度级别组织案例，帮助评估和比较不同的AI代码生成工具。

## 文件目录

```
GenDev-Benchmark/
├── README.md                                 # 项目主文档
├── development/                              # 研发相关案例
│   ├── README.md                             # 研发维度说明
│   ├── frontend/                             # 前端开发案例
│   │   ├── easy/                             # 低难度前端案例
│   │   │   └── android_ui_basic.md           # Android基础UI组件实现
│   │   ├── medium/                           # 中难度前端案例
│   │   │   ├── react_state_management.md     # React状态管理实现
│   │   │   ├── electron_chatbox_app.md       # Electron大模型ChatBox应用
│   │   │   └── electron_s3_manager.md        # Electron AWS S3管理工具
│   │   └── hard/                             # 高难度前端案例
│   │       └── micro_frontend_architecture.md # 微前端架构设计与实现
│   ├── backend/                              # 后端开发案例
│   │   ├── easy/                             # 低难度后端案例
│   │   │   ├── spring_boot_rest_api.md       # Spring Boot RESTful API实现
│   │   │   └── dev_environment_setup.md      # Java开发环境搭建
│   │   ├── medium/                           # 中难度后端案例
│   │   │   ├── design_patterns.md            # 设计模式应用
│   │   │   └── spring_cloud_microservices.md # Spring Cloud微服务架构实现
│   │   └── hard/                             # 高难度后端案例
│   │       ├── distributed_system.md         # 分布式系统设计与实现
│   │       ├── distributed_transaction.md    # 分布式事务处理系统设计与实现
│   │       └── skiplist_storage_engine.md    # 基于SkipList实现MySQL存储引擎
│   ├── middleware/                           # 中间件案例
│   │   └── medium/                           # 中难度中间件案例
│   │       └── redis_cache_strategy.md       # Redis分布式缓存策略实现
│   ├── database/                             # 数据库案例
│   │   ├── easy/                             # 低难度数据库案例
│   │   │   └── mysql_query_optimization.md   # MySQL基础查询优化
│   │   └── hard/                             # 高难度数据库案例
│   │       └── sharding_solution.md          # 数据库分库分表方案设计与实现
│   └── algorithm/                            # 算法案例
│       └── easy/                             # 低难度算法案例
│           └── array_manipulation.md         # 数组操作基础算法
├── testing/                                  # 测试相关案例
│   ├── README.md                             # 测试维度说明
│   ├── unit/                                 # 单元测试案例
│   │   └── easy/                             # 低难度单元测试案例
│   │       └── unit_testing.md               # 基础单元测试编写
│   ├── integration/                          # 集成测试案例
│   │   ├── easy/                             # 低难度集成测试案例
│   │   │   └── test_environment_setup.md     # 集成测试环境搭建
│   │   └── medium/                           # 中难度集成测试案例
│   │       └── api_testing.md                # API测试自动化
│   └── e2e/                                  # 端到端测试案例
│       └── hard/                             # 高难度端到端测试案例
│           └── e2e_testing_framework.md      # 端到端测试框架设计与实现
└── operations/                               # 运维相关案例
    ├── README.md                             # 运维维度说明
    ├── container/                            # 容器化技术案例
    │   ├── easy/                             # 低难度容器案例
    │   │   └── simple_docker_deployment.md   # 简单Docker容器部署
    │   └── hard/                             # 高难度容器案例
    │       └── microservices_deployment.md   # 微服务架构部署与管理
    ├── cicd/                                 # CI/CD流水线案例
    │   └── medium/                           # 中难度CI/CD案例
    │       └── cicd_pipeline_setup.md        # CI/CD流水线配置
    └── infrastructure/                       # 基础设施即代码案例
        └── easy/                             # 低难度基础设施案例
            └── ops_environment_setup.md      # 运维基础环境搭建
```

## 文档导航

### 维度说明文档
- [研发维度说明](development/README.md)
- [测试维度说明](testing/README.md)
- [运维维度说明](operations/README.md)

### 研发维度案例

#### 前端开发
- **低难度**：[Android基础UI组件实现](development/frontend/easy/android_ui_basic.md)
- **中难度**：
  - [React状态管理实现](development/frontend/medium/react_state_management.md)
  - [Electron大模型ChatBox应用](development/frontend/medium/electron_chatbox_app.md)
  - [Electron AWS S3管理工具](development/frontend/medium/electron_s3_manager.md)
- **高难度**：[微前端架构设计与实现](development/frontend/hard/micro_frontend_architecture.md)

#### 后端开发
- **低难度**：
  - [Spring Boot RESTful API实现](development/backend/easy/spring_boot_rest_api.md)
  - [Java开发环境搭建](development/backend/easy/dev_environment_setup.md)
- **中难度**：
  - [设计模式应用](development/backend/medium/design_patterns.md)
  - [Spring Cloud微服务架构实现](development/backend/medium/spring_cloud_microservices.md)
- **高难度**：
  - [分布式系统设计与实现](development/backend/hard/distributed_system.md)
  - [分布式事务处理系统设计与实现](development/backend/hard/distributed_transaction.md)
  - [基于SkipList实现MySQL存储引擎](development/backend/hard/skiplist_storage_engine.md)

#### 中间件
- **中难度**：[Redis分布式缓存策略实现](development/middleware/medium/redis_cache_strategy.md)

#### 数据库
- **低难度**：[MySQL基础查询优化](development/database/easy/mysql_query_optimization.md)
- **高难度**：[数据库分库分表方案设计与实现](development/database/hard/sharding_solution.md)

#### 算法
- **低难度**：[数组操作基础算法](development/algorithm/easy/array_manipulation.md)

### 测试维度案例

#### 单元测试
- **低难度**：[基础单元测试编写](testing/unit/easy/unit_testing.md)

#### 集成测试
- **低难度**：[集成测试环境搭建](testing/integration/easy/test_environment_setup.md)
- **中难度**：[API测试自动化](testing/integration/medium/api_testing.md)

#### 端到端测试
- **高难度**：[端到端测试框架设计与实现](testing/e2e/hard/e2e_testing_framework.md)

### 运维维度案例

#### 容器化技术
- **低难度**：[简单Docker容器部署](operations/container/easy/simple_docker_deployment.md)
- **高难度**：[微服务架构部署与管理](operations/container/hard/microservices_deployment.md)

#### CI/CD流水线
- **中难度**：[CI/CD流水线配置](operations/cicd/medium/cicd_pipeline_setup.md)

#### 基础设施
- **低难度**：[运维基础环境搭建](operations/infrastructure/easy/ops_environment_setup.md)

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