# GenDev-Benchmark

GenDev-Benchmark是一个全面的基准测试集合，用于评估AI代码生成工具在不同场景下的性能和能力。本项目从运维、研发和测试三个维度，按照难度级别（低、中、高）组织案例，帮助评估和比较不同的AI代码生成工具。

## 文件目录

```
GenDev-Benchmark/
├── README.md                                 # 项目主文档
├── development/                              # 研发相关案例
│   ├── README.md                             # 研发维度说明
│   ├── easy/                                 # 低难度研发案例
│   │   ├── frontend/                         # 前端开发案例
│   │   │   └── android_ui_basic.md           # Android基础UI组件实现
│   │   ├── backend/                          # 后端开发案例
│   │   │   └── spring_boot_rest_api.md       # Spring Boot RESTful API实现
│   │   ├── middleware/                       # 中间件案例
│   │   ├── database/                         # 数据库案例
│   │   │   └── mysql_query_optimization.md   # MySQL基础查询优化
│   │   └── algorithm/                        # 算法案例
│   │       └── array_manipulation.md         # 数组操作基础算法
│   ├── medium/                               # 中难度研发案例
│   │   ├── frontend/                         # 前端开发案例
│   │   │   └── react_state_management.md     # React状态管理实现
│   │   ├── backend/                          # 后端开发案例
│   │   │   ├── design_patterns.md            # 设计模式应用
│   │   │   └── spring_cloud_microservices.md # Spring Cloud微服务架构实现
│   │   ├── middleware/                       # 中间件案例
│   │   │   └── redis_cache_strategy.md       # Redis分布式缓存策略实现
│   │   ├── database/                         # 数据库案例
│   │   └── algorithm/                        # 算法案例
│   └── hard/                                 # 高难度研发案例
│       ├── frontend/                         # 前端开发案例
│       │   └── micro_frontend_architecture.md # 微前端架构设计与实现
│       ├── backend/                          # 后端开发案例
│       │   ├── distributed_system.md         # 分布式系统设计与实现
│       │   └── distributed_transaction.md    # 分布式事务处理系统设计与实现
│       ├── middleware/                       # 中间件案例
│       ├── database/                         # 数据库案例
│       │   └── sharding_solution.md          # 数据库分库分表方案设计与实现
│       └── algorithm/                        # 算法案例
├── operations/                               # 运维相关案例
│   ├── README.md                             # 运维维度说明
│   ├── easy/                                 # 低难度运维案例
│   │   └── simple_docker_deployment.md       # 简单Docker容器部署
│   ├── medium/                               # 中难度运维案例
│   │   └── cicd_pipeline_setup.md            # CI/CD流水线配置
│   └── hard/                                 # 高难度运维案例
│       └── microservices_deployment.md       # 微服务架构部署与管理
└── testing/                                  # 测试相关案例
    ├── README.md                             # 测试维度说明
    ├── easy/                                 # 低难度测试案例
    │   └── unit_testing.md                   # 基础单元测试编写
    ├── medium/                               # 中难度测试案例
    │   └── api_testing.md                    # API测试自动化
    └── hard/                                 # 高难度测试案例
        └── e2e_testing_framework.md          # 端到端测试框架设计与实现
```

## 文档导航

### 维度说明文档
- [研发维度说明](development/README.md)
- [运维维度说明](operations/README.md)
- [测试维度说明](testing/README.md)

### 研发维度案例

#### 前端开发
- **低难度**
  - [Android基础UI组件实现](development/easy/frontend/android_ui_basic.md)
- **中难度**
  - [React状态管理实现](development/medium/frontend/react_state_management.md)
- **高难度**
  - [微前端架构设计与实现](development/hard/frontend/micro_frontend_architecture.md)

#### 后端开发
- **低难度**
  - [Spring Boot RESTful API实现](development/easy/backend/spring_boot_rest_api.md)
- **中难度**
  - [设计模式应用](development/medium/backend/design_patterns.md)
  - [Spring Cloud微服务架构实现](development/medium/backend/spring_cloud_microservices.md)
- **高难度**
  - [分布式系统设计与实现](development/hard/backend/distributed_system.md)
  - [分布式事务处理系统设计与实现](development/hard/backend/distributed_transaction.md)

#### 中间件
- **中难度**
  - [Redis分布式缓存策略实现](development/medium/middleware/redis_cache_strategy.md)

#### 数据库
- **低难度**
  - [MySQL基础查询优化](development/easy/database/mysql_query_optimization.md)
- **高难度**
  - [数据库分库分表方案设计与实现](development/hard/database/sharding_solution.md)

#### 算法
- **低难度**
  - [数组操作基础算法](development/easy/algorithm/array_manipulation.md)

### 运维维度案例
- **低难度**
  - [简单Docker容器部署](operations/easy/simple_docker_deployment.md)
- **中难度**
  - [CI/CD流水线配置](operations/medium/cicd_pipeline_setup.md)
- **高难度**
  - [微服务架构部署与管理](operations/hard/microservices_deployment.md)

### 测试维度案例
- **低难度**
  - [基础单元测试编写](testing/easy/unit_testing.md)
- **中难度**
  - [API测试自动化](testing/medium/api_testing.md)
- **高难度**
  - [端到端测试框架设计与实现](testing/hard/e2e_testing_framework.md)

## 案例概述

### 运维维度

| 难度 | 案例描述 | 评估重点 |
|------|---------|---------|
| 低   | 基础服务器配置、简单Docker容器部署 | 基础命令、配置文件编写能力 |
| 中   | CI/CD流水线配置、多容器编排、监控系统设置 | 工具集成、自动化流程设计 |
| 高   | 多云环境管理、复杂微服务架构部署、灾备方案实现 | 系统架构理解、复杂环境协调能力 |

### 研发维度

| 难度 | 案例描述 | 评估重点 |
|------|---------|---------|
| 低   | 基础算法实现、简单API开发、数据结构操作 | 语法准确性、基础编程能力 |
| 中   | 设计模式应用、中等复杂度算法、并发编程 | 代码质量、架构设计能力 |
| 高   | 分布式系统设计、性能优化、复杂业务逻辑实现 | 系统设计能力、问题解决能力 |

### 测试维度

| 难度 | 案例描述 | 评估重点 |
|------|---------|---------|
| 低   | 单元测试编写、基础测试用例设计 | 测试覆盖率、基础测试概念理解 |
| 中   | 集成测试、API测试、性能测试脚本 | 测试策略、测试自动化能力 |
| 高   | 端到端测试框架、复杂场景测试、安全测试 | 全面测试方案、测试架构设计 |

## 评估标准

每个案例将从以下几个方面进行评估：

1. **正确性**：生成代码的功能正确性
2. **完整性**：解决方案的完整程度
3. **效率**：代码执行效率和资源利用
4. **可维护性**：代码结构、命名和文档
5. **创新性**：解决问题的创新方法和思路

## 使用方法

1. 选择要评估的维度和难度级别
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