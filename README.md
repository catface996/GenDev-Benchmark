# GenDev-Benchmark (Powered by Amazon Q)

GenDev-Benchmark是一个全面的基准测试集合，用于评估AI代码生成工具在不同场景下的性能和能力。本项目从运维、研发和测试三个维度，按照技术领域和难度级别组织案例，帮助评估和比较不同的AI代码生成工具。

## 文件目录

```
GenDev-Benchmark/
├── README.md                                 # 项目主文档
├── development/                              # 研发相关案例
│   ├── README.md                             # 研发维度说明
│   ├── frontend/                             # 前端开发案例
│   │   ├── easy/                             # 低难度前端案例
│   │   ├── medium/                           # 中难度前端案例
│   │   └── hard/                             # 高难度前端案例
│   ├── backend/                              # 后端开发案例
│   │   ├── easy/                             # 低难度后端案例
│   │   ├── medium/                           # 中难度后端案例
│   │   └── hard/                             # 高难度后端案例
│   ├── middleware/                           # 中间件案例
│   │   ├── easy/                             # 低难度中间件案例
│   │   ├── medium/                           # 中难度中间件案例
│   │   └── hard/                             # 高难度中间件案例
│   ├── database/                             # 数据库案例
│   │   ├── easy/                             # 低难度数据库案例
│   │   ├── medium/                           # 中难度数据库案例
│   │   └── hard/                             # 高难度数据库案例
│   └── algorithm/                            # 算法案例
│       ├── easy/                             # 低难度算法案例
│       ├── medium/                           # 中难度算法案例
│       └── hard/                             # 高难度算法案例
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
- **低难度**：
  - [Android基础UI组件实现](development/frontend/easy/android_ui_basic.md)
  - [HTML/CSS响应式布局实现](development/frontend/easy/responsive_layout.md)
  - [Vue.js待办事项应用](development/frontend/easy/vue_todo_app.md)
  - [iOS列表视图实现](development/frontend/easy/ios_list_view.md)
  - [JavaScript表单验证](development/frontend/easy/javascript_form_validation.md)
  - [CSS动画效果实现](development/frontend/easy/css_animation.md)
  - [React基础组件库开发](development/frontend/easy/react_component_library.md)
  - [Flutter UI组件实现](development/frontend/easy/flutter_ui_widgets.md)
  - [HTML5 Canvas绘图应用](development/frontend/easy/html5_canvas_drawing.md)
  - [静态博客网站模板](development/frontend/easy/static_blog_template.md)
  - [SVG图标动画实现](development/frontend/easy/svg_icon_animation.md)
  - [Web无障碍性基础](development/frontend/easy/web_accessibility.md)
- **中难度**：
  - [React状态管理实现](development/frontend/medium/react_state_management.md)
  - [Electron大模型ChatBox应用](development/frontend/medium/electron_chatbox_app.md)
  - [Electron AWS S3管理工具](development/frontend/medium/electron_s3_manager.md)
  - [React Hooks高级应用](development/frontend/medium/react_hooks_advanced.md)
  - [Vue.js电商前端实现](development/frontend/medium/vue_ecommerce.md)
  - [Flutter状态管理实现](development/frontend/medium/flutter_state_management.md)
  - [TypeScript设计模式实现](development/frontend/medium/typescript_design_patterns.md)
  - [渐进式Web应用(PWA)实现](development/frontend/medium/progressive_web_app.md)
  - [Angular数据仪表盘实现](development/frontend/medium/angular_dashboard.md)
  - [React Native社交应用](development/frontend/medium/react_native_social_app.md)
  - [Web动画库开发](development/frontend/medium/web_animation_library.md)
  - [WebGL 3D模型查看器](development/frontend/medium/webgl_3d_viewer.md)
  - [Svelte实时协作应用](development/frontend/medium/svelte_realtime_app.md)
- **高难度**：
  - [微前端架构设计与实现](development/frontend/hard/micro_frontend_architecture.md)
  - [React应用性能优化](development/frontend/hard/react_performance_optimization.md)
  - [WebAssembly图像处理应用](development/frontend/hard/webassembly_image_processing.md)
  - [GraphQL客户端框架实现](development/frontend/hard/graphql_client_framework.md)
  - [虚拟DOM实现与渲染引擎](development/frontend/hard/virtual_dom_implementation.md)
  - [Web 3D游戏引擎开发](development/frontend/hard/web_3d_game_engine.md)
  - [跨平台设计系统实现](development/frontend/hard/cross_platform_design_system.md)
  - [Web编译器/解释器实现](development/frontend/hard/web_compiler_interpreter.md)
  - [离线优先PWA应用框架](development/frontend/hard/offline_first_pwa.md)
  - [Web无障碍性框架开发](development/frontend/hard/web_accessibility_framework.md)
  - [实时协作引擎实现](development/frontend/hard/realtime_collaboration_engine.md)
  - [Web AR框架](development/frontend/hard/web_ar_framework.md)

#### 后端开发
- **低难度**：
  - [Spring Boot RESTful API实现](development/backend/easy/spring_boot_rest_api.md)
  - [Java开发环境搭建](development/backend/easy/dev_environment_setup.md)
  - [Node.js RESTful API实现](development/backend/easy/node_rest_api.md)
  - [Python Flask Web应用](development/backend/easy/python_flask_web.md)
  - [Go语言HTTP服务器](development/backend/easy/go_http_server.md)
  - [Java Servlet Web应用](development/backend/easy/java_servlet_app.md)
  - [C# ASP.NET MVC应用](development/backend/easy/csharp_aspnet_mvc.md)
  - [PHP Laravel CRUD应用](development/backend/easy/php_laravel_crud.md)
  - [Ruby on Rails博客应用](development/backend/easy/ruby_rails_blog.md)
  - [Python FastAPI服务](development/backend/easy/python_fastapi.md)
  - [Rust Actix Web API](development/backend/easy/rust_actix_api.md)
  - [Kotlin Spring Boot应用](development/backend/easy/kotlin_spring_boot.md)
- **中难度**：
  - [设计模式应用](development/backend/medium/design_patterns.md)
  - [Spring Cloud微服务架构实现](development/backend/medium/spring_cloud_microservices.md)
  - [Node.js GraphQL API实现](development/backend/medium/node_graphql_api.md)
  - [Go微服务实现](development/backend/medium/go_microservices.md)
  - [Go并发模式](development/backend/medium/go_concurrency_patterns.md)
  - [Java多线程编程](development/backend/medium/java_multithreading.md)
  - [Java响应式API](development/backend/medium/java_reactive_api.md)
  - [Kotlin协程应用](development/backend/medium/kotlin_coroutines.md)
  - [Node.js WebSocket服务器](development/backend/medium/node_websocket_server.md)
  - [PHP API平台](development/backend/medium/php_api_platform.md)
  - [Python Celery任务队列](development/backend/medium/python_celery_tasks.md)
  - [Python Django电商平台](development/backend/medium/python_django_ecommerce.md)
  - [Rust异步服务器](development/backend/medium/rust_async_server.md)
  - [C# SignalR实时通信](development/backend/medium/csharp_signalr_realtime.md)
- **高难度**：
  - [分布式系统设计与实现](development/backend/hard/distributed_system.md)
  - [分布式事务处理系统设计与实现](development/backend/hard/distributed_transaction.md)
  - [基于SkipList实现MySQL存储引擎](development/backend/hard/skiplist_storage_engine.md)
  - [区块链实现](development/backend/hard/blockchain_implementation.md)
  - [分布式数据库](development/backend/hard/distributed_database.md)
  - [事件溯源与CQRS](development/backend/hard/event_sourcing_cqrs.md)
  - [机器学习服务平台](development/backend/hard/ml_serving_platform.md)
  - [实时分析引擎](development/backend/hard/realtime_analytics_engine.md)
  - [Serverless平台](development/backend/hard/serverless_platform.md)
  - [服务网格实现](development/backend/hard/service_mesh_implementation.md)

#### 中间件
- **低难度**：
  - [Nginx配置](development/middleware/easy/nginx_config.md)
  - [RabbitMQ集成](development/middleware/easy/rabbitmq_integration.md)
  - [Redis基础缓存](development/middleware/easy/redis_basic_cache.md)
  - [Docker Compose配置](development/middleware/easy/docker_compose_setup.md)
  - [Logstash配置](development/middleware/easy/logstash_config.md)
  - [HAProxy负载均衡](development/middleware/easy/haproxy_load_balancer.md)
  - [Prometheus监控](development/middleware/easy/prometheus_monitoring.md)
  - [Consul服务发现](development/middleware/easy/consul_service_discovery.md)
  - [Traefik边缘路由器](development/middleware/easy/traefik_edge_router.md)
  - [etcd配置](development/middleware/easy/etcd_configuration.md)
  - [Elasticsearch配置](development/middleware/easy/elasticsearch_setup.md)
  - [Kafka基础配置](development/middleware/easy/kafka_basic_setup.md)
  - [ZooKeeper集群](development/middleware/easy/zookeeper_cluster.md)
- **中难度**：
  - [Redis分布式缓存策略实现](development/middleware/medium/redis_cache_strategy.md)
  - [Kafka Streams处理](development/middleware/medium/kafka_streams_processing.md)
  - [Elasticsearch高级功能](development/middleware/medium/elasticsearch_advanced.md)
  - [RabbitMQ高级模式](development/middleware/medium/rabbitmq_advanced.md)
  - [Nginx高级功能](development/middleware/medium/nginx_advanced.md)
  - [Kong API网关](development/middleware/medium/kong_api_gateway.md)
  - [Prometheus与Grafana高级监控](development/middleware/medium/prometheus_grafana_advanced.md)
  - [etcd分布式协调](development/middleware/medium/etcd_distributed_coordination.md)
  - [Envoy服务网格](development/middleware/medium/envoy_service_mesh.md)
  - [Redis集群与哨兵](development/middleware/medium/redis_cluster_sentinel.md)
  - [Apache Pulsar消息系统](development/middleware/medium/pulsar_messaging.md)
- **高难度**：
  - [分布式消息队列系统设计](development/middleware/hard/distributed_message_queue.md)
  - [API网关框架设计](development/middleware/hard/api_gateway_framework.md)
  - [分布式缓存系统设计](development/middleware/hard/distributed_cache_system.md)
  - [服务网格控制平面设计](development/middleware/hard/service_mesh_control_plane.md)
  - [分布式任务调度系统](development/middleware/hard/distributed_task_scheduler.md)
  - [分布式追踪系统设计](development/middleware/hard/distributed_tracing_system.md)
  - [流处理引擎设计](development/middleware/hard/stream_processing_engine.md)
  - [分布式锁服务设计](development/middleware/hard/distributed_lock_service.md)

#### 数据库
- **低难度**：
  - [MySQL基础查询优化](development/database/easy/mysql_query_optimization.md)
  - [PostgreSQL基础操作](development/database/easy/postgresql_basic_operations.md)
  - [MongoDB CRUD操作](development/database/easy/mongodb_crud.md)
  - [Redis数据结构应用](development/database/easy/redis_data_structures.md)
  - [SQLite嵌入式数据库应用](development/database/easy/sqlite_embedded_db.md)
  - [Elasticsearch基础应用](development/database/easy/elasticsearch_basic.md)
  - [InfluxDB时序数据应用](development/database/easy/influxdb_time_series.md)
  - [Neo4j图数据库应用](development/database/easy/neo4j_graph_database.md)
  - [Cassandra NoSQL数据库应用](development/database/easy/cassandra_nosql.md)
  - [DynamoDB无服务器数据库应用](development/database/easy/dynamodb_serverless.md)
  - [CouchDB文档数据库应用](development/database/easy/couchdb_document_db.md)
- **中难度**：
  - [MySQL性能调优](development/database/medium/mysql_performance_tuning.md)
  - [PostgreSQL高级功能应用](development/database/medium/postgresql_advanced.md)
  - [Elasticsearch高级搜索引擎](development/database/medium/elasticsearch_advanced_search.md)
  - [MongoDB聚合管道开发](development/database/medium/mongodb_aggregation.md)
  - [Redis高级模式实现](development/database/medium/redis_advanced_patterns.md)
  - [时序数据库设计与应用](development/database/medium/time_series_database.md)
  - [图数据库应用开发](development/database/medium/graph_database_application.md)
  - [数据库迁移与转换](development/database/medium/database_migration.md)
  - [数据仓库设计与实现](development/database/medium/data_warehouse_design.md)
  - [多模型数据库应用](development/database/medium/multi_model_database.md)
  - [数据库复制与同步](development/database/medium/database_replication.md)
- **高难度**：
  - [数据库分库分表方案设计与实现](development/database/hard/sharding_solution.md)
  - [分布式SQL查询引擎](development/database/hard/distributed_sql_engine.md)
  - [时序数据库引擎设计](development/database/hard/time_series_database_engine.md)
  - [分布式事务系统设计](development/database/hard/distributed_transaction.md)
  - [列式存储引擎设计](development/database/hard/columnar_storage_engine.md)
  - [数据库查询优化器设计](development/database/hard/database_query_optimizer.md)
  - [多模型数据库引擎设计](development/database/hard/multi_model_database_engine.md)
  - [流式数据库系统设计](development/database/hard/streaming_database_system.md)
  - [向量数据库实现](development/database/hard/vector_database_implementation.md)
  - [图数据库引擎设计](development/database/hard/graph_database_engine.md)

#### 算法
- **低难度**：
  - [数组操作基础算法](development/algorithm/easy/array_manipulation.md)
  - [排序算法实现](development/algorithm/easy/sorting_algorithms.md)
  - [二分查找算法](development/algorithm/easy/binary_search.md)
  - [链表操作算法](development/algorithm/easy/linked_list_operations.md)
  - [栈和队列实现](development/algorithm/easy/stack_queue_implementation.md)
  - [二叉树遍历算法](development/algorithm/easy/binary_tree_traversal.md)
  - [哈希表实现](development/algorithm/easy/hash_table_implementation.md)
  - [动态规划基础](development/algorithm/easy/dynamic_programming_basics.md)
  - [贪心算法实现](development/algorithm/easy/greedy_algorithms.md)
  - [递归与回溯算法](development/algorithm/easy/recursion_and_backtracking.md)
  - [图遍历算法](development/algorithm/easy/graph_traversal.md)
- **中难度**：
  - [高级图算法](development/algorithm/medium/advanced_graph_algorithms.md)
  - [高级数据结构实现](development/algorithm/medium/advanced_data_structures.md)
  - [字符串算法](development/algorithm/medium/string_algorithms.md)
  - [高级动态规划](development/algorithm/medium/advanced_dynamic_programming.md)
  - [计算几何算法](development/algorithm/medium/computational_geometry.md)
  - [数论算法](development/algorithm/medium/number_theory_algorithms.md)
  - [随机化算法](development/algorithm/medium/randomized_algorithms.md)
  - [位运算算法](development/algorithm/medium/bit_manipulation.md)
  - [分治算法](development/algorithm/medium/divide_and_conquer.md)
  - [优化算法](development/algorithm/medium/optimization_algorithms.md)
  - [机器学习基础算法](development/algorithm/medium/machine_learning_algorithms.md)
- **高难度**：
  - [高级优化算法](development/algorithm/hard/advanced_optimization_algorithms.md)
  - [高级图论算法](development/algorithm/hard/advanced_graph_theory.md)
  - [高级计算几何算法](development/algorithm/hard/computational_geometry_advanced.md)
  - [计算机视觉算法](development/algorithm/hard/computer_vision_algorithms.md)
  - [密码学算法实现](development/algorithm/hard/cryptographic_algorithms.md)
  - [并行与分布式算法](development/algorithm/hard/parallel_distributed_algorithms.md)
  - [自然语言处理算法](development/algorithm/hard/natural_language_processing.md)
  - [深度学习算法实现](development/algorithm/hard/deep_learning_algorithms.md)
  - [强化学习算法](development/algorithm/hard/reinforcement_learning.md)
  - [遗传与进化算法](development/algorithm/hard/genetic_evolutionary_algorithms.md)
  - [概率图模型](development/algorithm/hard/probabilistic_graphical_models.md)
  - [数据压缩算法](development/algorithm/hard/compression_algorithms.md)
  - [编译器设计算法](development/algorithm/hard/compiler_design_algorithms.md)
  - [量子计算算法](development/algorithm/hard/quantum_computing_algorithms.md)

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