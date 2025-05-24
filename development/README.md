# 研发维度基准测试

本目录包含用于评估AI代码生成工具在软件研发方面能力的基准测试案例。

## 目录结构

```
development/
├── easy/                           # 低难度研发案例
│   ├── frontend/                   # 前端开发案例
│   │   └── android_ui_basic.md     # Android基础UI组件实现
│   ├── backend/                    # 后端开发案例
│   │   └── spring_boot_rest_api.md # Spring Boot RESTful API实现
│   ├── middleware/                 # 中间件案例
│   ├── database/                   # 数据库案例
│   │   └── mysql_query_optimization.md # MySQL基础查询优化
│   └── algorithm/                  # 算法案例
│       └── array_manipulation.md   # 数组操作基础算法
├── medium/                         # 中难度研发案例
│   ├── frontend/                   # 前端开发案例
│   │   └── react_state_management.md # React状态管理实现
│   ├── backend/                    # 后端开发案例
│   │   ├── design_patterns.md      # 设计模式应用
│   │   └── spring_cloud_microservices.md # Spring Cloud微服务架构实现
│   ├── middleware/                 # 中间件案例
│   │   └── redis_cache_strategy.md # Redis分布式缓存策略实现
│   ├── database/                   # 数据库案例
│   └── algorithm/                  # 算法案例
└── hard/                           # 高难度研发案例
    ├── frontend/                   # 前端开发案例
    │   └── micro_frontend_architecture.md # 微前端架构设计与实现
    ├── backend/                    # 后端开发案例
    │   ├── distributed_system.md   # 分布式系统设计与实现
    │   └── distributed_transaction.md # 分布式事务处理系统设计与实现
    ├── middleware/                 # 中间件案例
    ├── database/                   # 数据库案例
    │   └── sharding_solution.md    # 数据库分库分表方案设计与实现
    └── algorithm/                  # 算法案例
```

## 难度级别

### 低难度 (Easy)
基础编程能力测试，包括简单算法实现、数据结构操作和基本API开发。这些案例主要评估代码的语法准确性和基础编程能力。

### 中难度 (Medium)
进阶编程能力测试，包括设计模式应用、中等复杂度算法实现和并发编程。这些案例主要评估代码质量和架构设计能力。

### 高难度 (Hard)
高级系统设计能力测试，包括分布式系统设计、性能优化和复杂业务逻辑实现。这些案例主要评估系统设计能力和问题解决能力。

## 技术领域基准测试列表

### 前端开发

#### Android
- **低难度**：[基础UI组件实现](easy/frontend/android_ui_basic.md)、简单列表展示、SharedPreferences数据存储
- **中难度**：自定义View组件、RecyclerView复杂适配器、MVVM架构实现
- **高难度**：复杂动画效果、组件化架构设计、性能优化与内存泄漏处理

#### iOS
- **低难度**：基础UI控件使用、TableView实现、UserDefaults数据存储
- **中难度**：自定义UIView、复杂CollectionView布局、MVVM架构实现
- **高难度**：Core Animation高级动画、模块化架构设计、内存管理与性能优化

#### H5/Web
- **低难度**：响应式布局实现、基础表单验证、简单DOM操作
- **中难度**：[React状态管理实现](medium/frontend/react_state_management.md)、前端路由实现、复杂表单处理
- **高难度**：[微前端架构设计与实现](hard/frontend/micro_frontend_architecture.md)、大规模数据可视化、PWA离线应用实现

### 后端开发

#### Java
- **低难度**：[Spring Boot RESTful API实现](easy/backend/spring_boot_rest_api.md)、简单CRUD操作
- **中难度**：[设计模式应用](medium/backend/design_patterns.md)、[Spring Cloud微服务架构实现](medium/backend/spring_cloud_microservices.md)、并发编程
- **高难度**：[分布式系统设计与实现](hard/backend/distributed_system.md)、[分布式事务处理](hard/backend/distributed_transaction.md)、高并发系统设计

#### 中间件集成
- **低难度**：Redis缓存集成、RabbitMQ基础消息队列、Nginx简单配置
- **中难度**：[Redis分布式缓存策略实现](medium/middleware/redis_cache_strategy.md)、消息队列复杂场景应用、服务网关高级配置
- **高难度**：中间件集群方案、消息系统高可用设计、全链路监控实现

### 数据库

#### MySQL
- **低难度**：[MySQL基础查询优化](easy/database/mysql_query_optimization.md)、索引设计、简单存储过程
- **中难度**：复杂查询优化、分区表设计、主从复制配置
- **高难度**：[数据库分库分表方案设计与实现](hard/database/sharding_solution.md)、读写分离架构、高可用集群设计

#### ElasticSearch
- **低难度**：基础索引创建与查询、简单聚合分析、全文检索实现
- **中难度**：复杂查询DSL、索引优化策略、集群配置
- **高难度**：大规模数据检索优化、复杂数据建模、跨集群搜索实现

### 算法与数据结构
- **低难度**：[数组操作基础算法](easy/algorithm/array_manipulation.md)、链表操作、栈与队列实现
- **中难度**：树结构操作、图算法基础、动态规划入门
- **高难度**：复杂图算法、高级动态规划、机器学习算法实现

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