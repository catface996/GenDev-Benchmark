# 研发维度基准测试

本目录包含用于评估AI代码生成工具在软件研发方面能力的基准测试案例。

## 目录结构

```
development/
├── frontend/                        # 前端开发案例
│   ├── easy/                        # 低难度前端案例
│   │   └── android_ui_basic.md      # Android基础UI组件实现
│   ├── medium/                      # 中难度前端案例
│   │   ├── react_state_management.md # React状态管理实现
│   │   ├── electron_chatbox_app.md  # Electron大模型ChatBox应用
│   │   └── electron_s3_manager.md   # Electron AWS S3管理工具
│   └── hard/                        # 高难度前端案例
│       └── micro_frontend_architecture.md # 微前端架构设计与实现
├── backend/                         # 后端开发案例
│   ├── easy/                        # 低难度后端案例
│   │   ├── spring_boot_rest_api.md  # Spring Boot RESTful API实现
│   │   └── dev_environment_setup.md # Java开发环境搭建
│   ├── medium/                      # 中难度后端案例
│   │   ├── design_patterns.md       # 设计模式应用
│   │   └── spring_cloud_microservices.md # Spring Cloud微服务架构实现
│   └── hard/                        # 高难度后端案例
│       ├── distributed_system.md    # 分布式系统设计与实现
│       ├── distributed_transaction.md # 分布式事务处理系统设计与实现
│       └── skiplist_storage_engine.md # 基于SkipList实现MySQL存储引擎
├── middleware/                      # 中间件案例
│   ├── easy/                        # 低难度中间件案例
│   ├── medium/                      # 中难度中间件案例
│   │   └── redis_cache_strategy.md  # Redis分布式缓存策略实现
│   └── hard/                        # 高难度中间件案例
├── database/                        # 数据库案例
│   ├── easy/                        # 低难度数据库案例
│   │   └── mysql_query_optimization.md # MySQL基础查询优化
│   ├── medium/                      # 中难度数据库案例
│   └── hard/                        # 高难度数据库案例
│       └── sharding_solution.md     # 数据库分库分表方案设计与实现
└── algorithm/                       # 算法案例
    ├── easy/                        # 低难度算法案例
    │   └── array_manipulation.md    # 数组操作基础算法
    ├── medium/                      # 中难度算法案例
    └── hard/                        # 高难度算法案例
```

## 技术领域

### 前端开发
前端开发案例涵盖了从基础UI组件实现到复杂的微前端架构设计，包括Android、iOS和Web前端技术。

#### 案例列表
- **低难度**：[Android基础UI组件实现](frontend/easy/android_ui_basic.md)
- **中难度**：
  - [React状态管理实现](frontend/medium/react_state_management.md)
  - [Electron大模型ChatBox应用](frontend/medium/electron_chatbox_app.md)
  - [Electron AWS S3管理工具](frontend/medium/electron_s3_manager.md)
- **高难度**：[微前端架构设计与实现](frontend/hard/micro_frontend_architecture.md)

### 后端开发
后端开发案例涵盖了从简单API实现到复杂分布式系统设计，主要基于Java技术栈。

#### 案例列表
- **低难度**：
  - [Spring Boot RESTful API实现](backend/easy/spring_boot_rest_api.md)
  - [Java开发环境搭建](backend/easy/dev_environment_setup.md)
- **中难度**：
  - [设计模式应用](backend/medium/design_patterns.md)
  - [Spring Cloud微服务架构实现](backend/medium/spring_cloud_microservices.md)
- **高难度**：
  - [分布式系统设计与实现](backend/hard/distributed_system.md)
  - [分布式事务处理系统设计与实现](backend/hard/distributed_transaction.md)
  - [基于SkipList实现MySQL存储引擎](backend/hard/skiplist_storage_engine.md)

### 中间件
中间件案例涵盖了缓存、消息队列、服务网关等技术的应用和优化。

#### 案例列表
- **中难度**：[Redis分布式缓存策略实现](middleware/medium/redis_cache_strategy.md)

### 数据库
数据库案例涵盖了从基础查询优化到复杂的分库分表方案设计，包括MySQL和ElasticSearch等技术。

#### 案例列表
- **低难度**：[MySQL基础查询优化](database/easy/mysql_query_optimization.md)
- **高难度**：[数据库分库分表方案设计与实现](database/hard/sharding_solution.md)

### 算法与数据结构
算法案例涵盖了从基础数组操作到复杂图算法和机器学习算法的实现。

#### 案例列表
- **低难度**：[数组操作基础算法](algorithm/easy/array_manipulation.md)

## 难度级别

### 低难度 (Easy)
基础编程能力测试，包括简单算法实现、数据结构操作和基本API开发。这些案例主要评估代码的语法准确性和基础编程能力。

### 中难度 (Medium)
进阶编程能力测试，包括设计模式应用、中等复杂度算法实现和并发编程。这些案例主要评估代码质量和架构设计能力。

### 高难度 (Hard)
高级系统设计能力测试，包括分布式系统设计、性能优化和复杂业务逻辑实现。这些案例主要评估系统设计能力和问题解决能力。

## 评估标准

1. **正确性**：生成的代码是否能正确实现所需功能
2. **效率**：算法和数据结构的选择是否高效
3. **可读性**：代码是否清晰、易于理解
4. **可维护性**：代码结构、命名和文档是否有助于长期维护
5. **可扩展性**：设计是否考虑了未来的扩展需求
6. **最佳实践**：是否遵循行业最佳实践和设计原则

## 使用方法

1. 选择适合的技术领域和难度级别
2. 查看对应目录下的案例描述
3. 使用AI代码生成工具生成解决方案
4. 根据评估标准对生成的代码进行评分