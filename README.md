# GenDev-Benchmark (Powered by Amazon Q)

GenDev-Benchmark是一个全面的基准测试集合，用于评估AI代码生成工具在不同场景下的性能和能力。本项目从运维、研发和测试三个维度，按照技术领域和难度级别组织案例，帮助评估和比较不同的AI代码生成工具。

## 文件目录

```
GenDev-Benchmark/
├── README.md                                 # 项目主文档
├── development/                              # Development相关案例
│   ├── README.md                             # Development维度说明
│   ├── middleware/                            # Middleware案例
│   │   ├── easy/                             # Easy难度middleware案例
│   │   │   └── kafka_basic_setup.md               # 示例案例
│   │   ├── hard/                             # Hard难度middleware案例
│   │   │   └── service_mesh_control_plane.md               # 示例案例
│   │   └── medium/                             # Medium难度middleware案例
│   │       └── envoy_service_mesh.md               # 示例案例
│   ├── database/                            # Database案例
│   │   ├── easy/                             # Easy难度database案例
│   │   │   └── mysql_query_optimization.md               # 示例案例
│   │   ├── hard/                             # Hard难度database案例
│   │   │   └── columnar_storage_engine.md               # 示例案例
│   │   └── medium/                             # Medium难度database案例
│   │       └── data_warehouse_design.md               # 示例案例
│   ├── frontend/                            # Frontend案例
│   │   ├── easy/                             # Easy难度frontend案例
│   │   │   └── svg_icon_animation.md               # 示例案例
│   │   ├── hard/                             # Hard难度frontend案例
│   │   │   └── graphql_client_framework.md               # 示例案例
│   │   └── medium/                             # Medium难度frontend案例
│   │       └── svelte_realtime_app.md               # 示例案例
│   ├── backend/                            # Backend案例
│   │   ├── easy/                             # Easy难度backend案例
│   │   │   └── python_fastapi.md               # 示例案例
│   │   ├── hard/                             # Hard难度backend案例
│   │   │   └── serverless_platform.md               # 示例案例
│   │   └── medium/                             # Medium难度backend案例
│   │       └── kotlin_coroutines.md               # 示例案例
│   └── algorithm/                            # Algorithm案例
│       ├── easy/                             # Easy难度algorithm案例
│       │   └── hash_table_implementation.md               # 示例案例
│       ├── hard/                             # Hard难度algorithm案例
│       │   └── parallel_distributed_algorithms.md               # 示例案例
│       └── medium/                             # Medium难度algorithm案例
│           └── divide_and_conquer.md               # 示例案例
├── testing/                              # Testing相关案例
│   ├── README.md                             # Testing维度说明
│   ├── unit/                            # Unit案例
│   │   ├── easy/                             # Easy难度unit案例
│   │   │   └── test_fixtures.md               # 示例案例
│   │   ├── hard/                             # Hard难度unit案例
│   │   │   └── fuzz_testing_framework.md               # 示例案例
│   │   └── medium/                             # Medium难度unit案例
│   │       └── concurrent_code_testing.md               # 示例案例
│   ├── integration/                            # Integration案例
│   │   ├── easy/                             # Easy难度integration案例
│   │   │   └── scheduled_tasks_testing.md               # 示例案例
│   │   ├── hard/                             # Hard难度integration案例
│   │   │   └── blockchain_testing_platform.md               # 示例案例
│   │   └── medium/                             # Medium难度integration案例
│   │       └── security_integration.md               # 示例案例
│   ├── performance/                            # Performance案例
│   │   ├── easy/                             # Easy难度performance案例
│   │   │   └── web_page_performance_testing.md               # 示例案例
│   │   ├── hard/                             # Hard难度performance案例
│   │   │   └── ai_model_performance_optimization.md               # 示例案例
│   │   └── medium/                             # Medium难度performance案例
│   │       └── database_optimization_testing.md               # 示例案例
│   └── e2e/                            # E2e案例
│       ├── easy/                             # Easy难度e2e案例
│       │   └── web_ui_testing.md               # 示例案例
│       ├── hard/                             # Hard难度e2e案例
│       │   └── distributed_system_e2e_framework.md               # 示例案例
│       └── medium/                             # Medium难度e2e案例
│           └── internationalization_testing.md               # 示例案例
└── operations/                              # Operations相关案例
    ├── README.md                             # Operations维度说明
    ├── security/                            # Security案例
    │   ├── easy/                             # Easy难度security案例
    │   │   └── user_access_management.md               # 示例案例
    │   ├── hard/                             # Hard难度security案例
    │   │   └── zero_trust_architecture.md               # 示例案例
    │   └── medium/                             # Medium难度security案例
    │       └── devsecops_pipeline.md               # 示例案例
    ├── cicd/                            # Cicd案例
    │   ├── easy/                             # Easy难度cicd案例
    │   │   └── github_actions_basic.md               # 示例案例
    │   ├── hard/                             # Hard难度cicd案例
    │   │   └── multi_environment_pipeline.md               # 示例案例
    │   └── medium/                             # Medium难度cicd案例
    │       └── cicd_pipeline_setup.md               # 示例案例
    ├── container/                            # Container案例
    │   ├── easy/                             # Easy难度container案例
    │   │   └── docker_volume_management.md               # 示例案例
    │   ├── hard/                             # Hard难度container案例
    │   │   └── kubernetes_operator_development.md               # 示例案例
    │   └── medium/                             # Medium难度container案例
    │       └── container_security_implementation.md               # 示例案例
    ├── monitoring/                            # Monitoring案例
    │   ├── easy/                             # Easy难度monitoring案例
    │   │   └── prometheus_grafana_setup.md               # 示例案例
    │   ├── hard/                             # Hard难度monitoring案例
    │   │   └── distributed_tracing_platform.md               # 示例案例
    │   └── medium/                             # Medium难度monitoring案例
    │       └── metrics_visualization_dashboard.md               # 示例案例
    └── infrastructure/                            # Infrastructure案例
        ├── easy/                             # Easy难度infrastructure案例
        │   └── ansible_automation.md               # 示例案例
        ├── hard/                             # Hard难度infrastructure案例
        │   └── multi_cloud_infrastructure.md               # 示例案例
        └── medium/                             # Medium难度infrastructure案例
            └── terraform_aws_infrastructure.md               # 示例案例
```

## 文档导航

### 维度说明文档
- [Development维度说明](development/README.md)
- [Testing维度说明](testing/README.md)
- [Operations维度说明](operations/README.md)

### Development维度案例

#### Middleware
- **Easy难度**：
  - [Consul服务发现配置](development/middleware/easy/consul_service_discovery.md)
  - [Docker Compose基础配置](development/middleware/easy/docker_compose_setup.md)
  - [Elasticsearch基础配置](development/middleware/easy/elasticsearch_setup.md)
  - [etcd分布式键值存储配置](development/middleware/easy/etcd_configuration.md)
  - [HAProxy负载均衡配置](development/middleware/easy/haproxy_load_balancer.md)
  - [Kafka基础配置](development/middleware/easy/kafka_basic_setup.md)
  - [Logstash日志处理配置](development/middleware/easy/logstash_config.md)
  - [Nginx基础配置](development/middleware/easy/nginx_config.md)
  - [Prometheus监控配置](development/middleware/easy/prometheus_monitoring.md)
  - [RabbitMQ消息队列集成](development/middleware/easy/rabbitmq_integration.md)
  - [Redis基础缓存实现](development/middleware/easy/redis_basic_cache.md)
  - [Traefik边缘路由器配置](development/middleware/easy/traefik_edge_router.md)
  - [ZooKeeper集群配置](development/middleware/easy/zookeeper_cluster.md)
- **Medium难度**：
  - [Elasticsearch高级功能实现](development/middleware/medium/elasticsearch_advanced.md)
  - [Envoy服务网格实现](development/middleware/medium/envoy_service_mesh.md)
  - [etcd分布式协调应用](development/middleware/medium/etcd_distributed_coordination.md)
  - [Kafka Streams数据处理](development/middleware/medium/kafka_streams_processing.md)
  - [Kong API网关实现](development/middleware/medium/kong_api_gateway.md)
  - [Nginx高级功能实现](development/middleware/medium/nginx_advanced.md)
  - [Prometheus与Grafana高级监控](development/middleware/medium/prometheus_grafana_advanced.md)
  - [Apache Pulsar消息系统](development/middleware/medium/pulsar_messaging.md)
  - [RabbitMQ高级模式实现](development/middleware/medium/rabbitmq_advanced.md)
  - [Redis分布式缓存策略实现](development/middleware/medium/redis_cache_strategy.md)
  - [Redis集群与哨兵配置](development/middleware/medium/redis_cluster_sentinel.md)
- **Hard难度**：
  - [API网关框架设计与实现](development/middleware/hard/api_gateway_framework.md)
  - [分布式缓存系统设计](development/middleware/hard/distributed_cache_system.md)
  - [分布式锁服务设计](development/middleware/hard/distributed_lock_service.md)
  - [分布式消息队列系统设计](development/middleware/hard/distributed_message_queue.md)
  - [分布式任务调度系统](development/middleware/hard/distributed_task_scheduler.md)
  - [分布式追踪系统设计](development/middleware/hard/distributed_tracing_system.md)
  - [服务网格控制平面设计](development/middleware/hard/service_mesh_control_plane.md)
  - [流处理引擎设计](development/middleware/hard/stream_processing_engine.md)
#### Database
- **Easy难度**：
  - [Cassandra NoSQL数据库应用](development/database/easy/cassandra_nosql.md)
  - [CouchDB文档数据库应用](development/database/easy/couchdb_document_db.md)
  - [DynamoDB无服务器数据库应用](development/database/easy/dynamodb_serverless.md)
  - [Elasticsearch基础应用](development/database/easy/elasticsearch_basic.md)
  - [InfluxDB时序数据应用](development/database/easy/influxdb_time_series.md)
  - [MongoDB CRUD操作](development/database/easy/mongodb_crud.md)
  - [MySQL基础查询优化](development/database/easy/mysql_query_optimization.md)
  - [Neo4j图数据库应用](development/database/easy/neo4j_graph_database.md)
  - [PostgreSQL基础操作](development/database/easy/postgresql_basic_operations.md)
  - [Redis数据结构应用](development/database/easy/redis_data_structures.md)
  - [SQLite嵌入式数据库应用](development/database/easy/sqlite_embedded_db.md)
- **Medium难度**：
  - [数据仓库设计与实现](development/database/medium/data_warehouse_design.md)
  - [数据库迁移与转换](development/database/medium/database_migration.md)
  - [数据库复制与同步](development/database/medium/database_replication.md)
  - [Elasticsearch高级搜索引擎](development/database/medium/elasticsearch_advanced_search.md)
  - [图数据库应用开发](development/database/medium/graph_database_application.md)
  - [MongoDB聚合管道开发](development/database/medium/mongodb_aggregation.md)
  - [多模型数据库应用](development/database/medium/multi_model_database.md)
  - [MySQL性能调优](development/database/medium/mysql_performance_tuning.md)
  - [PostgreSQL高级功能应用](development/database/medium/postgresql_advanced.md)
  - [Redis高级模式实现](development/database/medium/redis_advanced_patterns.md)
  - [时序数据库设计与应用](development/database/medium/time_series_database.md)
- **Hard难度**：
  - [列式存储引擎设计](development/database/hard/columnar_storage_engine.md)
  - [数据库查询优化器设计](development/database/hard/database_query_optimizer.md)
  - [分布式SQL查询引擎](development/database/hard/distributed_sql_engine.md)
  - [分布式事务系统设计](development/database/hard/distributed_transaction.md)
  - [图数据库引擎设计](development/database/hard/graph_database_engine.md)
  - [多模型数据库引擎设计](development/database/hard/multi_model_database_engine.md)
  - [数据库分库分表方案设计与实现](development/database/hard/sharding_solution.md)
  - [流式数据库系统设计](development/database/hard/streaming_database_system.md)
  - [时序数据库引擎设计](development/database/hard/time_series_database_engine.md)
  - [向量数据库实现](development/database/hard/vector_database_implementation.md)
#### Frontend
- **Easy难度**：
  - [Android基础UI组件实现](development/frontend/easy/android_ui_basic.md)
  - [CSS动画效果实现](development/frontend/easy/css_animation.md)
  - [Flutter UI组件实现](development/frontend/easy/flutter_ui_widgets.md)
  - [HTML5 Canvas绘图应用](development/frontend/easy/html5_canvas_drawing.md)
  - [iOS列表视图实现](development/frontend/easy/ios_list_view.md)
  - [JavaScript表单验证](development/frontend/easy/javascript_form_validation.md)
  - [React基础组件库开发](development/frontend/easy/react_component_library.md)
  - [HTML/CSS响应式布局实现](development/frontend/easy/responsive_layout.md)
  - [静态博客网站模板](development/frontend/easy/static_blog_template.md)
  - [SVG图标动画实现](development/frontend/easy/svg_icon_animation.md)
  - [Vue.js待办事项应用](development/frontend/easy/vue_todo_app.md)
  - [Web无障碍性优化](development/frontend/easy/web_accessibility.md)
- **Medium难度**：
  - [Angular数据仪表盘实现](development/frontend/medium/angular_dashboard.md)
  - [Electron大模型ChatBox应用](development/frontend/medium/electron_chatbox_app.md)
  - [Electron AWS S3管理工具](development/frontend/medium/electron_s3_manager.md)
  - [Flutter状态管理实现](development/frontend/medium/flutter_state_management.md)
  - [渐进式Web应用(PWA)实现](development/frontend/medium/progressive_web_app.md)
  - [React Hooks高级应用](development/frontend/medium/react_hooks_advanced.md)
  - [React Native社交应用](development/frontend/medium/react_native_social_app.md)
  - [React状态管理实现](development/frontend/medium/react_state_management.md)
  - [Svelte实时协作应用](development/frontend/medium/svelte_realtime_app.md)
  - [TypeScript设计模式实现](development/frontend/medium/typescript_design_patterns.md)
  - [Vue.js电商前端实现](development/frontend/medium/vue_ecommerce.md)
  - [Web动画库开发](development/frontend/medium/web_animation_library.md)
  - [WebGL 3D模型查看器](development/frontend/medium/webgl_3d_viewer.md)
- **Hard难度**：
  - [跨平台设计系统实现](development/frontend/hard/cross_platform_design_system.md)
  - [GraphQL客户端框架实现](development/frontend/hard/graphql_client_framework.md)
  - [微前端架构设计与实现](development/frontend/hard/micro_frontend_architecture.md)
  - [离线优先PWA应用框架](development/frontend/hard/offline_first_pwa.md)
  - [React应用性能优化](development/frontend/hard/react_performance_optimization.md)
  - [实时协作引擎实现](development/frontend/hard/realtime_collaboration_engine.md)
  - [虚拟DOM实现与渲染引擎](development/frontend/hard/virtual_dom_implementation.md)
  - [Web 3D游戏引擎开发](development/frontend/hard/web_3d_game_engine.md)
  - [Web无障碍性框架开发](development/frontend/hard/web_accessibility_framework.md)
  - [Web AR框架开发](development/frontend/hard/web_ar_framework.md)
  - [Web编译器/解释器实现](development/frontend/hard/web_compiler_interpreter.md)
  - [WebAssembly图像处理应用](development/frontend/hard/webassembly_image_processing.md)
#### Backend
- **Easy难度**：
  - [C# ASP.NET MVC应用](development/backend/easy/csharp_aspnet_mvc.md)
  - [Java开发环境搭建](development/backend/easy/dev_environment_setup.md)
  - [Go语言HTTP服务器](development/backend/easy/go_http_server.md)
  - [Java Servlet Web应用](development/backend/easy/java_servlet_app.md)
  - [Kotlin Spring Boot应用](development/backend/easy/kotlin_spring_boot.md)
  - [Node.js RESTful API实现](development/backend/easy/node_rest_api.md)
  - [PHP Laravel CRUD应用](development/backend/easy/php_laravel_crud.md)
  - [Python FastAPI服务](development/backend/easy/python_fastapi.md)
  - [Python Flask Web应用](development/backend/easy/python_flask_web.md)
  - [Ruby on Rails博客应用](development/backend/easy/ruby_rails_blog.md)
  - [Rust Actix Web API](development/backend/easy/rust_actix_api.md)
  - [Spring Boot RESTful API实现](development/backend/easy/spring_boot_rest_api.md)
- **Medium难度**：
  - [C# SignalR实时应用](development/backend/medium/csharp_signalr_realtime.md)
  - [设计模式应用](development/backend/medium/design_patterns.md)
  - [Go并发模式实现](development/backend/medium/go_concurrency_patterns.md)
  - [Go微服务开发](development/backend/medium/go_microservices.md)
  - [Java多线程并发应用](development/backend/medium/java_multithreading.md)
  - [Java响应式API实现](development/backend/medium/java_reactive_api.md)
  - [Kotlin协程应用](development/backend/medium/kotlin_coroutines.md)
  - [Node.js GraphQL API实现](development/backend/medium/node_graphql_api.md)
  - [Node.js WebSocket服务器](development/backend/medium/node_websocket_server.md)
  - [PHP API Platform实现](development/backend/medium/php_api_platform.md)
  - [Python Celery任务队列](development/backend/medium/python_celery_tasks.md)
  - [Python Django电商后端](development/backend/medium/python_django_ecommerce.md)
  - [Rust异步Web服务器](development/backend/medium/rust_async_server.md)
  - [Spring Cloud微服务架构实现](development/backend/medium/spring_cloud_microservices.md)
- **Hard难度**：
  - [区块链系统实现](development/backend/hard/blockchain_implementation.md)
  - [分布式数据库系统](development/backend/hard/distributed_database.md)
  - [分布式系统设计与实现](development/backend/hard/distributed_system.md)
  - [分布式事务处理系统设计与实现](development/backend/hard/distributed_transaction.md)
  - [事件溯源与CQRS架构](development/backend/hard/event_sourcing_cqrs.md)
  - [机器学习模型服务平台](development/backend/hard/ml_serving_platform.md)
  - [实时数据分析引擎](development/backend/hard/realtime_analytics_engine.md)
  - [Serverless计算平台](development/backend/hard/serverless_platform.md)
  - [服务网格实现](development/backend/hard/service_mesh_implementation.md)
  - [基于SkipList实现MySQL存储引擎](development/backend/hard/skiplist_storage_engine.md)
#### Algorithm
- **Easy难度**：
  - [数组操作基础算法](development/algorithm/easy/array_manipulation.md)
  - [二分查找算法](development/algorithm/easy/binary_search.md)
  - [二叉树遍历算法](development/algorithm/easy/binary_tree_traversal.md)
  - [动态规划基础](development/algorithm/easy/dynamic_programming_basics.md)
  - [图遍历算法](development/algorithm/easy/graph_traversal.md)
  - [贪心算法实现](development/algorithm/easy/greedy_algorithms.md)
  - [哈希表实现](development/algorithm/easy/hash_table_implementation.md)
  - [链表操作算法](development/algorithm/easy/linked_list_operations.md)
  - [递归与回溯算法](development/algorithm/easy/recursion_and_backtracking.md)
  - [排序算法实现](development/algorithm/easy/sorting_algorithms.md)
  - [栈和队列实现](development/algorithm/easy/stack_queue_implementation.md)
- **Medium难度**：
  - [高级数据结构实现](development/algorithm/medium/advanced_data_structures.md)
  - [高级动态规划](development/algorithm/medium/advanced_dynamic_programming.md)
  - [高级图算法](development/algorithm/medium/advanced_graph_algorithms.md)
  - [位运算算法](development/algorithm/medium/bit_manipulation.md)
  - [计算几何算法](development/algorithm/medium/computational_geometry.md)
  - [分治算法](development/algorithm/medium/divide_and_conquer.md)
  - [机器学习基础算法](development/algorithm/medium/machine_learning_algorithms.md)
  - [数论算法](development/algorithm/medium/number_theory_algorithms.md)
  - [优化算法](development/algorithm/medium/optimization_algorithms.md)
  - [随机化算法](development/algorithm/medium/randomized_algorithms.md)
  - [字符串算法](development/algorithm/medium/string_algorithms.md)
- **Hard难度**：
  - [高级图论算法](development/algorithm/hard/advanced_graph_theory.md)
  - [高级优化算法](development/algorithm/hard/advanced_optimization_algorithms.md)
  - [编译器设计算法](development/algorithm/hard/compiler_design_algorithms.md)
  - [数据压缩算法](development/algorithm/hard/compression_algorithms.md)
  - [高级计算几何算法](development/algorithm/hard/computational_geometry_advanced.md)
  - [计算机视觉算法](development/algorithm/hard/computer_vision_algorithms.md)
  - [密码学算法实现](development/algorithm/hard/cryptographic_algorithms.md)
  - [深度学习算法实现](development/algorithm/hard/deep_learning_algorithms.md)
  - [遗传与进化算法](development/algorithm/hard/genetic_evolutionary_algorithms.md)
  - [自然语言处理算法](development/algorithm/hard/natural_language_processing.md)
  - [并行与分布式算法](development/algorithm/hard/parallel_distributed_algorithms.md)
  - [概率图模型](development/algorithm/hard/probabilistic_graphical_models.md)
  - [量子计算算法](development/algorithm/hard/quantum_computing_algorithms.md)
  - [强化学习算法](development/algorithm/hard/reinforcement_learning.md)

### Testing维度案例

#### Unit
- **Easy难度**：
  - [断言技术与最佳实践](testing/unit/easy/assertion_techniques.md)
  - [边界值测试设计](testing/unit/easy/boundary_testing.md)
  - [代码覆盖率分析与提升](testing/unit/easy/code_coverage.md)
  - [异常测试技术](testing/unit/easy/exception_testing.md)
  - [模拟对象创建与使用](testing/unit/easy/mock_objects.md)
  - [参数化测试实现](testing/unit/easy/parameterized_tests.md)
  - [私有方法测试策略](testing/unit/easy/private_method_testing.md)
  - [测试替身类型与应用](testing/unit/easy/test_doubles.md)
  - [测试驱动开发实践](testing/unit/easy/test_driven_development.md)
  - [测试夹具设计与使用](testing/unit/easy/test_fixtures.md)
  - [测试命名约定与组织](testing/unit/easy/test_naming_conventions.md)
  - [基础单元测试编写](testing/unit/easy/unit_testing.md)
- **Medium难度**：
  - [行为驱动开发实践](testing/unit/medium/behavior_driven_development.md)
  - [并发代码测试技术](testing/unit/medium/concurrent_code_testing.md)
  - [依赖注入与可测试设计](testing/unit/medium/dependency_injection.md)
  - [遗留代码测试策略](testing/unit/medium/legacy_code_testing.md)
  - [变异测试实践](testing/unit/medium/mutation_testing.md)
  - [基于属性的测试](testing/unit/medium/property_based_testing.md)
  - [测试架构设计](testing/unit/medium/test_architecture.md)
  - [测试数据构建器模式](testing/unit/medium/test_data_builders.md)
  - [测试指标分析与改进](testing/unit/medium/test_metrics_analysis.md)
  - [单元测试模式与反模式](testing/unit/medium/test_patterns.md)
- **Hard难度**：
  - [高级模拟框架设计](testing/unit/hard/advanced_mocking_framework.md)
  - [组合测试引擎设计](testing/unit/hard/combinatorial_testing_engine.md)
  - [协同测试框架设计](testing/unit/hard/concolic_testing_framework.md)
  - [差异测试系统设计](testing/unit/hard/differential_testing_system.md)
  - [模糊测试框架设计](testing/unit/hard/fuzz_testing_framework.md)
  - [程序不变量检测系统](testing/unit/hard/invariant_detection_system.md)
  - [变质测试系统设计](testing/unit/hard/metamorphic_testing.md)
  - [基于模型的测试系统](testing/unit/hard/model_based_testing.md)
  - [基于搜索的测试框架](testing/unit/hard/search_based_testing.md)
  - [符号执行测试引擎](testing/unit/hard/symbolic_execution_engine.md)
  - [测试框架设计与实现](testing/unit/hard/test_framework_design.md)
  - [自动测试生成引擎](testing/unit/hard/test_generation_engine.md)
#### Integration
- **Easy难度**：
  - [API契约测试](testing/integration/easy/api_contract_testing.md)
  - [认证系统集成测试](testing/integration/easy/authentication_testing.md)
  - [缓存系统集成测试](testing/integration/easy/cache_integration.md)
  - [配置系统集成测试](testing/integration/easy/configuration_testing.md)
  - [数据库集成测试](testing/integration/easy/database_integration.md)
  - [邮件服务集成测试](testing/integration/easy/email_service_testing.md)
  - [外部API集成测试](testing/integration/easy/external_api_testing.md)
  - [文件系统集成测试](testing/integration/easy/file_system_integration.md)
  - [日志系统集成测试](testing/integration/easy/logging_integration.md)
  - [消息队列集成测试](testing/integration/easy/message_queue_testing.md)
  - [定时任务集成测试](testing/integration/easy/scheduled_tasks_testing.md)
  - [集成测试环境搭建](testing/integration/easy/test_environment_setup.md)
- **Medium难度**：
  - [API网关集成测试](testing/integration/medium/api_gateway_testing.md)
  - [API测试自动化](testing/integration/medium/api_testing.md)
  - [缓存策略集成测试](testing/integration/medium/caching_strategy_testing.md)
  - [云服务集成测试](testing/integration/medium/cloud_service_integration.md)
  - [数据管道集成测试](testing/integration/medium/data_pipeline_testing.md)
  - [数据库迁移测试](testing/integration/medium/database_migration_testing.md)
  - [分布式事务测试](testing/integration/medium/distributed_transaction.md)
  - [事件驱动架构测试](testing/integration/medium/event_driven_testing.md)
  - [微服务集成测试](testing/integration/medium/microservice_integration.md)
  - [安全集成测试](testing/integration/medium/security_integration.md)
  - [第三方系统集成测试](testing/integration/medium/third_party_integration.md)
- **Hard难度**：
  - [API测试自动化框架](testing/integration/hard/api_testing_framework.md)
  - [区块链系统测试平台](testing/integration/hard/blockchain_testing_platform.md)
  - [持续集成测试平台](testing/integration/hard/continuous_integration_platform.md)
  - [数据库测试平台](testing/integration/hard/database_testing_platform.md)
  - [分布式系统测试平台](testing/integration/hard/distributed_system_testing.md)
  - [事件溯源系统测试框架](testing/integration/hard/event_sourcing_testing.md)
  - [物联网系统测试框架](testing/integration/hard/iot_testing_framework.md)
  - [机器学习管道测试框架](testing/integration/hard/ml_pipeline_testing.md)
  - [实时系统测试框架](testing/integration/hard/real_time_system_testing.md)
  - [无服务器应用测试平台](testing/integration/hard/serverless_testing_platform.md)
  - [服务网格测试框架](testing/integration/hard/service_mesh_testing.md)
#### Performance
- **Easy难度**：
  - [API性能测试](testing/performance/easy/api_performance_testing.md)
  - [基准性能测试](testing/performance/easy/baseline_performance_testing.md)
  - [数据库性能测试](testing/performance/easy/database_performance_testing.md)
  - [负载测试基础](testing/performance/easy/load_testing_basics.md)
  - [内存使用测试](testing/performance/easy/memory_usage_testing.md)
  - [资源利用率测试](testing/performance/easy/resource_utilization_testing.md)
  - [响应时间测试](testing/performance/easy/response_time_testing.md)
  - [可扩展性测试](testing/performance/easy/scalability_testing.md)
  - [压力测试基础](testing/performance/easy/stress_testing_basics.md)
  - [吞吐量测试](testing/performance/easy/throughput_testing.md)
  - [Web页面性能测试](testing/performance/easy/web_page_performance_testing.md)
- **Medium难度**：
  - [API网关性能测试](testing/performance/medium/api_gateway_performance_testing.md)
  - [缓存策略测试](testing/performance/medium/caching_strategy_testing.md)
  - [容器性能测试](testing/performance/medium/container_performance_testing.md)
  - [数据库优化测试](testing/performance/medium/database_optimization_testing.md)
  - [分布式负载测试](testing/performance/medium/distributed_load_testing.md)
  - [前端性能测试](testing/performance/medium/frontend_performance_testing.md)
  - [消息队列性能测试](testing/performance/medium/message_queue_performance_testing.md)
  - [微服务性能测试](testing/performance/medium/microservices_performance_testing.md)
  - [移动应用性能测试](testing/performance/medium/mobile_app_performance_testing.md)
  - [性能剖析与分析](testing/performance/medium/performance_profiling.md)
  - [无服务器性能测试](testing/performance/medium/serverless_performance_testing.md)
- **Hard难度**：
  - [AI模型性能优化框架](testing/performance/hard/ai_model_performance_optimization.md)
  - [混沌工程测试平台](testing/performance/hard/chaos_engineering_platform.md)
  - [云成本性能优化系统](testing/performance/hard/cloud_cost_performance_optimization.md)
  - [数据库基准测试框架](testing/performance/hard/database_benchmark_framework.md)
  - [分布式系统性能建模](testing/performance/hard/distributed_system_performance_modeling.md)
  - [分布式追踪分析平台](testing/performance/hard/distributed_tracing_analysis_platform.md)
  - [游戏引擎性能测试框架](testing/performance/hard/game_engine_performance_framework.md)
  - [性能测试框架设计与实现](testing/performance/hard/performance_testing_framework.md)
  - [实时性能监控系统](testing/performance/hard/real_time_performance_monitoring.md)
  - [流数据处理系统基准测试](testing/performance/hard/streaming_data_processing_benchmark.md)
  - [Web前端性能实验室](testing/performance/hard/web_frontend_performance_lab.md)
#### E2e
- **Easy难度**：
  - [API工作流端到端测试](testing/e2e/easy/api_workflow_testing.md)
  - [数据库工作流端到端测试](testing/e2e/easy/database_workflow_testing.md)
  - [文件上传端到端测试](testing/e2e/easy/file_upload_testing.md)
  - [移动应用端到端测试](testing/e2e/easy/mobile_app_testing.md)
  - [通知系统端到端测试](testing/e2e/easy/notification_system_testing.md)
  - [支付处理端到端测试](testing/e2e/easy/payment_processing_testing.md)
  - [搜索功能端到端测试](testing/e2e/easy/search_functionality_testing.md)
  - [购物车端到端测试](testing/e2e/easy/shopping_cart_testing.md)
  - [用户资料端到端测试](testing/e2e/easy/user_profile_testing.md)
  - [用户注册端到端测试](testing/e2e/easy/user_registration_testing.md)
  - [Web UI端到端测试](testing/e2e/easy/web_ui_testing.md)
- **Medium难度**：
  - [无障碍性端到端测试](testing/e2e/medium/accessibility_testing.md)
  - [跨浏览器端到端测试](testing/e2e/medium/cross_browser_testing.md)
  - [数据驱动端到端测试](testing/e2e/medium/data_driven_testing.md)
  - [国际化端到端测试](testing/e2e/medium/internationalization_testing.md)
  - [多设备端到端测试](testing/e2e/medium/multi_device_testing.md)
  - [多租户端到端测试](testing/e2e/medium/multi_tenant_testing.md)
  - [离线模式端到端测试](testing/e2e/medium/offline_mode_testing.md)
  - [实时应用端到端测试](testing/e2e/medium/real_time_application_testing.md)
  - [安全工作流端到端测试](testing/e2e/medium/security_workflow_testing.md)
  - [视觉回归测试](testing/e2e/medium/visual_regression_testing.md)
  - [工作流自动化端到端测试](testing/e2e/medium/workflow_automation_testing.md)
- **Hard难度**：
  - [AI系统端到端测试框架](testing/e2e/hard/ai_system_testing_framework.md)
  - [AR/VR应用测试框架](testing/e2e/hard/ar_vr_testing_framework.md)
  - [自主系统测试平台](testing/e2e/hard/autonomous_system_testing_platform.md)
  - [区块链DApp测试框架](testing/e2e/hard/blockchain_dapp_testing_framework.md)
  - [云原生应用测试平台](testing/e2e/hard/cloud_native_testing_platform.md)
  - [数字孪生测试平台](testing/e2e/hard/digital_twin_testing_platform.md)
  - [分布式系统端到端测试框架](testing/e2e/hard/distributed_system_e2e_framework.md)
  - [端到端测试框架设计与实现](testing/e2e/hard/e2e_testing_framework.md)
  - [金融科技系统测试平台](testing/e2e/hard/fintech_system_testing_platform.md)
  - [物联网平台测试框架](testing/e2e/hard/iot_platform_testing_framework.md)
  - [微服务架构测试平台](testing/e2e/hard/microservices_testing_platform.md)
  - [SaaS平台测试框架](testing/e2e/hard/saas_platform_testing_framework.md)

### Operations维度案例

#### Security
- **Easy难度**：
  - [防火墙规则配置与管理](operations/security/easy/firewall_configuration.md)
  - [服务器安全加固配置](operations/security/easy/security_hardening.md)
  - [SSL证书管理与自动更新](operations/security/easy/ssl_certificate_management.md)
  - [用户访问管理与权限控制](operations/security/easy/user_access_management.md)
- **Medium难度**：
  - [DevSecOps流水线实现](operations/security/medium/devsecops_pipeline.md)
  - [安全监控系统设计与实现](operations/security/medium/security_monitoring_system.md)
  - [漏洞管理系统实现](operations/security/medium/vulnerability_management_system.md)
- **Hard难度**：
  - [零信任安全架构设计与实现](operations/security/hard/zero_trust_architecture.md)
#### Cicd
- **Easy难度**：
  - [GitHub Actions基础配置](operations/cicd/easy/github_actions_basic.md)
  - [Jenkins基础配置与使用](operations/cicd/easy/jenkins_basic_setup.md)
- **Medium难度**：
  - [制品管理系统配置与使用](operations/cicd/medium/artifact_management_system.md)
  - [CI/CD流水线配置](operations/cicd/medium/cicd_pipeline_setup.md)
  - [持续部署流水线实现](operations/cicd/medium/continuous_deployment_pipeline.md)
- **Hard难度**：
  - [多环境CI/CD流水线设计与实现](operations/cicd/hard/multi_environment_pipeline.md)
#### Container
- **Easy难度**：
  - [容器镜像仓库搭建与配置](operations/container/easy/container_registry_setup.md)
  - [Docker Compose基础应用部署](operations/container/easy/docker_compose_basics.md)
  - [Docker网络基础配置](operations/container/easy/docker_networking_basics.md)
  - [Docker数据卷管理与备份](operations/container/easy/docker_volume_management.md)
  - [简单Docker容器部署](operations/container/easy/simple_docker_deployment.md)
- **Medium难度**：
  - [容器安全实现与最佳实践](operations/container/medium/container_security_implementation.md)
  - [Docker Swarm集群编排与管理](operations/container/medium/docker_swarm_orchestration.md)
  - [Kubernetes基础部署与配置](operations/container/medium/kubernetes_deployment.md)
- **Hard难度**：
  - [Kubernetes Operator开发与部署](operations/container/hard/kubernetes_operator_development.md)
  - [微服务架构部署与管理](operations/container/hard/microservices_deployment.md)
  - [服务网格架构实现与管理](operations/container/hard/service_mesh_implementation.md)
#### Monitoring
- **Easy难度**：
  - [日志轮转与管理配置](operations/monitoring/easy/log_rotation_setup.md)
  - [Prometheus和Grafana基础监控配置](operations/monitoring/easy/prometheus_grafana_setup.md)
  - [系统监控基础配置](operations/monitoring/easy/system_monitoring_basics.md)
- **Medium难度**：
  - [告警系统设计与实现](operations/monitoring/medium/alerting_system_implementation.md)
  - [ELK Stack日志分析系统实现](operations/monitoring/medium/elk_stack_implementation.md)
  - [指标可视化仪表板设计](operations/monitoring/medium/metrics_visualization_dashboard.md)
- **Hard难度**：
  - [分布式追踪与可观测性平台设计](operations/monitoring/hard/distributed_tracing_platform.md)
#### Infrastructure
- **Easy难度**：
  - [Ansible基础自动化配置](operations/infrastructure/easy/ansible_automation.md)
  - [云存储服务配置与管理](operations/infrastructure/easy/cloud_storage_management.md)
  - [运维基础环境搭建](operations/infrastructure/easy/ops_environment_setup.md)
  - [Vagrant开发环境自动化配置](operations/infrastructure/easy/vagrant_dev_environment.md)
- **Medium难度**：
  - [配置管理系统实现](operations/infrastructure/medium/configuration_management.md)
  - [灾难恢复方案设计与实施](operations/infrastructure/medium/disaster_recovery_planning.md)
  - [Terraform AWS基础设施自动化](operations/infrastructure/medium/terraform_aws_infrastructure.md)
- **Hard难度**：
  - [多云环境基础设施设计与实现](operations/infrastructure/hard/multi_cloud_infrastructure.md)
### Development维度案例

#### Middleware
- **Easy难度**：
  - [Consul服务发现配置](development/middleware/easy/consul_service_discovery.md)
  - [Docker Compose基础配置](development/middleware/easy/docker_compose_setup.md)
  - [Elasticsearch基础配置](development/middleware/easy/elasticsearch_setup.md)
  - [etcd分布式键值存储配置](development/middleware/easy/etcd_configuration.md)
  - [HAProxy负载均衡配置](development/middleware/easy/haproxy_load_balancer.md)
  - [Kafka基础配置](development/middleware/easy/kafka_basic_setup.md)
  - [Logstash日志处理配置](development/middleware/easy/logstash_config.md)
  - [Nginx基础配置](development/middleware/easy/nginx_config.md)
  - [Prometheus监控配置](development/middleware/easy/prometheus_monitoring.md)
  - [RabbitMQ消息队列集成](development/middleware/easy/rabbitmq_integration.md)
  - [Redis基础缓存实现](development/middleware/easy/redis_basic_cache.md)
  - [Traefik边缘路由器配置](development/middleware/easy/traefik_edge_router.md)
  - [ZooKeeper集群配置](development/middleware/easy/zookeeper_cluster.md)
- **Medium难度**：
  - [Elasticsearch高级功能实现](development/middleware/medium/elasticsearch_advanced.md)
  - [Envoy服务网格实现](development/middleware/medium/envoy_service_mesh.md)
  - [etcd分布式协调应用](development/middleware/medium/etcd_distributed_coordination.md)
  - [Kafka Streams数据处理](development/middleware/medium/kafka_streams_processing.md)
  - [Kong API网关实现](development/middleware/medium/kong_api_gateway.md)
  - [Nginx高级功能实现](development/middleware/medium/nginx_advanced.md)
  - [Prometheus与Grafana高级监控](development/middleware/medium/prometheus_grafana_advanced.md)
  - [Apache Pulsar消息系统](development/middleware/medium/pulsar_messaging.md)
  - [RabbitMQ高级模式实现](development/middleware/medium/rabbitmq_advanced.md)
  - [Redis分布式缓存策略实现](development/middleware/medium/redis_cache_strategy.md)
  - [Redis集群与哨兵配置](development/middleware/medium/redis_cluster_sentinel.md)
- **Hard难度**：
  - [API网关框架设计与实现](development/middleware/hard/api_gateway_framework.md)
  - [分布式缓存系统设计](development/middleware/hard/distributed_cache_system.md)
  - [分布式锁服务设计](development/middleware/hard/distributed_lock_service.md)
  - [分布式消息队列系统设计](development/middleware/hard/distributed_message_queue.md)
  - [分布式任务调度系统](development/middleware/hard/distributed_task_scheduler.md)
  - [分布式追踪系统设计](development/middleware/hard/distributed_tracing_system.md)
  - [服务网格控制平面设计](development/middleware/hard/service_mesh_control_plane.md)
  - [流处理引擎设计](development/middleware/hard/stream_processing_engine.md)
#### Database
- **Easy难度**：
  - [Cassandra NoSQL数据库应用](development/database/easy/cassandra_nosql.md)
  - [CouchDB文档数据库应用](development/database/easy/couchdb_document_db.md)
  - [DynamoDB无服务器数据库应用](development/database/easy/dynamodb_serverless.md)
  - [Elasticsearch基础应用](development/database/easy/elasticsearch_basic.md)
  - [InfluxDB时序数据应用](development/database/easy/influxdb_time_series.md)
  - [MongoDB CRUD操作](development/database/easy/mongodb_crud.md)
  - [MySQL基础查询优化](development/database/easy/mysql_query_optimization.md)
  - [Neo4j图数据库应用](development/database/easy/neo4j_graph_database.md)
  - [PostgreSQL基础操作](development/database/easy/postgresql_basic_operations.md)
  - [Redis数据结构应用](development/database/easy/redis_data_structures.md)
  - [SQLite嵌入式数据库应用](development/database/easy/sqlite_embedded_db.md)
- **Medium难度**：
  - [数据仓库设计与实现](development/database/medium/data_warehouse_design.md)
  - [数据库迁移与转换](development/database/medium/database_migration.md)
  - [数据库复制与同步](development/database/medium/database_replication.md)
  - [Elasticsearch高级搜索引擎](development/database/medium/elasticsearch_advanced_search.md)
  - [图数据库应用开发](development/database/medium/graph_database_application.md)
  - [MongoDB聚合管道开发](development/database/medium/mongodb_aggregation.md)
  - [多模型数据库应用](development/database/medium/multi_model_database.md)
  - [MySQL性能调优](development/database/medium/mysql_performance_tuning.md)
  - [PostgreSQL高级功能应用](development/database/medium/postgresql_advanced.md)
  - [Redis高级模式实现](development/database/medium/redis_advanced_patterns.md)
  - [时序数据库设计与应用](development/database/medium/time_series_database.md)
- **Hard难度**：
  - [列式存储引擎设计](development/database/hard/columnar_storage_engine.md)
  - [数据库查询优化器设计](development/database/hard/database_query_optimizer.md)
  - [分布式SQL查询引擎](development/database/hard/distributed_sql_engine.md)
  - [分布式事务系统设计](development/database/hard/distributed_transaction.md)
  - [图数据库引擎设计](development/database/hard/graph_database_engine.md)
  - [多模型数据库引擎设计](development/database/hard/multi_model_database_engine.md)
  - [数据库分库分表方案设计与实现](development/database/hard/sharding_solution.md)
  - [流式数据库系统设计](development/database/hard/streaming_database_system.md)
  - [时序数据库引擎设计](development/database/hard/time_series_database_engine.md)
  - [向量数据库实现](development/database/hard/vector_database_implementation.md)
#### Frontend
- **Easy难度**：
  - [Android基础UI组件实现](development/frontend/easy/android_ui_basic.md)
  - [CSS动画效果实现](development/frontend/easy/css_animation.md)
  - [Flutter UI组件实现](development/frontend/easy/flutter_ui_widgets.md)
  - [HTML5 Canvas绘图应用](development/frontend/easy/html5_canvas_drawing.md)
  - [iOS列表视图实现](development/frontend/easy/ios_list_view.md)
  - [JavaScript表单验证](development/frontend/easy/javascript_form_validation.md)
  - [React基础组件库开发](development/frontend/easy/react_component_library.md)
  - [HTML/CSS响应式布局实现](development/frontend/easy/responsive_layout.md)
  - [静态博客网站模板](development/frontend/easy/static_blog_template.md)
  - [SVG图标动画实现](development/frontend/easy/svg_icon_animation.md)
  - [Vue.js待办事项应用](development/frontend/easy/vue_todo_app.md)
  - [Web无障碍性优化](development/frontend/easy/web_accessibility.md)
- **Medium难度**：
  - [Angular数据仪表盘实现](development/frontend/medium/angular_dashboard.md)
  - [Electron大模型ChatBox应用](development/frontend/medium/electron_chatbox_app.md)
  - [Electron AWS S3管理工具](development/frontend/medium/electron_s3_manager.md)
  - [Flutter状态管理实现](development/frontend/medium/flutter_state_management.md)
  - [渐进式Web应用(PWA)实现](development/frontend/medium/progressive_web_app.md)
  - [React Hooks高级应用](development/frontend/medium/react_hooks_advanced.md)
  - [React Native社交应用](development/frontend/medium/react_native_social_app.md)
  - [React状态管理实现](development/frontend/medium/react_state_management.md)
  - [Svelte实时协作应用](development/frontend/medium/svelte_realtime_app.md)
  - [TypeScript设计模式实现](development/frontend/medium/typescript_design_patterns.md)
  - [Vue.js电商前端实现](development/frontend/medium/vue_ecommerce.md)
  - [Web动画库开发](development/frontend/medium/web_animation_library.md)
  - [WebGL 3D模型查看器](development/frontend/medium/webgl_3d_viewer.md)
- **Hard难度**：
  - [跨平台设计系统实现](development/frontend/hard/cross_platform_design_system.md)
  - [GraphQL客户端框架实现](development/frontend/hard/graphql_client_framework.md)
  - [微前端架构设计与实现](development/frontend/hard/micro_frontend_architecture.md)
  - [离线优先PWA应用框架](development/frontend/hard/offline_first_pwa.md)
  - [React应用性能优化](development/frontend/hard/react_performance_optimization.md)
  - [实时协作引擎实现](development/frontend/hard/realtime_collaboration_engine.md)
  - [虚拟DOM实现与渲染引擎](development/frontend/hard/virtual_dom_implementation.md)
  - [Web 3D游戏引擎开发](development/frontend/hard/web_3d_game_engine.md)
  - [Web无障碍性框架开发](development/frontend/hard/web_accessibility_framework.md)
  - [Web AR框架开发](development/frontend/hard/web_ar_framework.md)
  - [Web编译器/解释器实现](development/frontend/hard/web_compiler_interpreter.md)
  - [WebAssembly图像处理应用](development/frontend/hard/webassembly_image_processing.md)
#### Backend
- **Easy难度**：
  - [C# ASP.NET MVC应用](development/backend/easy/csharp_aspnet_mvc.md)
  - [Java开发环境搭建](development/backend/easy/dev_environment_setup.md)
  - [Go语言HTTP服务器](development/backend/easy/go_http_server.md)
  - [Java Servlet Web应用](development/backend/easy/java_servlet_app.md)
  - [Kotlin Spring Boot应用](development/backend/easy/kotlin_spring_boot.md)
  - [Node.js RESTful API实现](development/backend/easy/node_rest_api.md)
  - [PHP Laravel CRUD应用](development/backend/easy/php_laravel_crud.md)
  - [Python FastAPI服务](development/backend/easy/python_fastapi.md)
  - [Python Flask Web应用](development/backend/easy/python_flask_web.md)
  - [Ruby on Rails博客应用](development/backend/easy/ruby_rails_blog.md)
  - [Rust Actix Web API](development/backend/easy/rust_actix_api.md)
  - [Spring Boot RESTful API实现](development/backend/easy/spring_boot_rest_api.md)
- **Medium难度**：
  - [C# SignalR实时应用](development/backend/medium/csharp_signalr_realtime.md)
  - [设计模式应用](development/backend/medium/design_patterns.md)
  - [Go并发模式实现](development/backend/medium/go_concurrency_patterns.md)
  - [Go微服务开发](development/backend/medium/go_microservices.md)
  - [Java多线程并发应用](development/backend/medium/java_multithreading.md)
  - [Java响应式API实现](development/backend/medium/java_reactive_api.md)
  - [Kotlin协程应用](development/backend/medium/kotlin_coroutines.md)
  - [Node.js GraphQL API实现](development/backend/medium/node_graphql_api.md)
  - [Node.js WebSocket服务器](development/backend/medium/node_websocket_server.md)
  - [PHP API Platform实现](development/backend/medium/php_api_platform.md)
  - [Python Celery任务队列](development/backend/medium/python_celery_tasks.md)
  - [Python Django电商后端](development/backend/medium/python_django_ecommerce.md)
  - [Rust异步Web服务器](development/backend/medium/rust_async_server.md)
  - [Spring Cloud微服务架构实现](development/backend/medium/spring_cloud_microservices.md)
- **Hard难度**：
  - [区块链系统实现](development/backend/hard/blockchain_implementation.md)
  - [分布式数据库系统](development/backend/hard/distributed_database.md)
  - [分布式系统设计与实现](development/backend/hard/distributed_system.md)
  - [分布式事务处理系统设计与实现](development/backend/hard/distributed_transaction.md)
  - [事件溯源与CQRS架构](development/backend/hard/event_sourcing_cqrs.md)
  - [机器学习模型服务平台](development/backend/hard/ml_serving_platform.md)
  - [实时数据分析引擎](development/backend/hard/realtime_analytics_engine.md)
  - [Serverless计算平台](development/backend/hard/serverless_platform.md)
  - [服务网格实现](development/backend/hard/service_mesh_implementation.md)
  - [基于SkipList实现MySQL存储引擎](development/backend/hard/skiplist_storage_engine.md)
#### Algorithm
- **Easy难度**：
  - [数组操作基础算法](development/algorithm/easy/array_manipulation.md)
  - [二分查找算法](development/algorithm/easy/binary_search.md)
  - [二叉树遍历算法](development/algorithm/easy/binary_tree_traversal.md)
  - [动态规划基础](development/algorithm/easy/dynamic_programming_basics.md)
  - [图遍历算法](development/algorithm/easy/graph_traversal.md)
  - [贪心算法实现](development/algorithm/easy/greedy_algorithms.md)
  - [哈希表实现](development/algorithm/easy/hash_table_implementation.md)
  - [链表操作算法](development/algorithm/easy/linked_list_operations.md)
  - [递归与回溯算法](development/algorithm/easy/recursion_and_backtracking.md)
  - [排序算法实现](development/algorithm/easy/sorting_algorithms.md)
  - [栈和队列实现](development/algorithm/easy/stack_queue_implementation.md)
- **Medium难度**：
  - [高级数据结构实现](development/algorithm/medium/advanced_data_structures.md)
  - [高级动态规划](development/algorithm/medium/advanced_dynamic_programming.md)
  - [高级图算法](development/algorithm/medium/advanced_graph_algorithms.md)
  - [位运算算法](development/algorithm/medium/bit_manipulation.md)
  - [计算几何算法](development/algorithm/medium/computational_geometry.md)
  - [分治算法](development/algorithm/medium/divide_and_conquer.md)
  - [机器学习基础算法](development/algorithm/medium/machine_learning_algorithms.md)
  - [数论算法](development/algorithm/medium/number_theory_algorithms.md)
  - [优化算法](development/algorithm/medium/optimization_algorithms.md)
  - [随机化算法](development/algorithm/medium/randomized_algorithms.md)
  - [字符串算法](development/algorithm/medium/string_algorithms.md)
- **Hard难度**：
  - [高级图论算法](development/algorithm/hard/advanced_graph_theory.md)
  - [高级优化算法](development/algorithm/hard/advanced_optimization_algorithms.md)
  - [编译器设计算法](development/algorithm/hard/compiler_design_algorithms.md)
  - [数据压缩算法](development/algorithm/hard/compression_algorithms.md)
  - [高级计算几何算法](development/algorithm/hard/computational_geometry_advanced.md)
  - [计算机视觉算法](development/algorithm/hard/computer_vision_algorithms.md)
  - [密码学算法实现](development/algorithm/hard/cryptographic_algorithms.md)
  - [深度学习算法实现](development/algorithm/hard/deep_learning_algorithms.md)
  - [遗传与进化算法](development/algorithm/hard/genetic_evolutionary_algorithms.md)
  - [自然语言处理算法](development/algorithm/hard/natural_language_processing.md)
  - [并行与分布式算法](development/algorithm/hard/parallel_distributed_algorithms.md)
  - [概率图模型](development/algorithm/hard/probabilistic_graphical_models.md)
  - [量子计算算法](development/algorithm/hard/quantum_computing_algorithms.md)
  - [强化学习算法](development/algorithm/hard/reinforcement_learning.md)

### Testing维度案例

#### Unit
- **Easy难度**：
  - [断言技术与最佳实践](testing/unit/easy/assertion_techniques.md)
  - [边界值测试设计](testing/unit/easy/boundary_testing.md)
  - [代码覆盖率分析与提升](testing/unit/easy/code_coverage.md)
  - [异常测试技术](testing/unit/easy/exception_testing.md)
  - [模拟对象创建与使用](testing/unit/easy/mock_objects.md)
  - [参数化测试实现](testing/unit/easy/parameterized_tests.md)
  - [私有方法测试策略](testing/unit/easy/private_method_testing.md)
  - [测试替身类型与应用](testing/unit/easy/test_doubles.md)
  - [测试驱动开发实践](testing/unit/easy/test_driven_development.md)
  - [测试夹具设计与使用](testing/unit/easy/test_fixtures.md)
  - [测试命名约定与组织](testing/unit/easy/test_naming_conventions.md)
  - [基础单元测试编写](testing/unit/easy/unit_testing.md)
- **Medium难度**：
  - [行为驱动开发实践](testing/unit/medium/behavior_driven_development.md)
  - [并发代码测试技术](testing/unit/medium/concurrent_code_testing.md)
  - [依赖注入与可测试设计](testing/unit/medium/dependency_injection.md)
  - [遗留代码测试策略](testing/unit/medium/legacy_code_testing.md)
  - [变异测试实践](testing/unit/medium/mutation_testing.md)
  - [基于属性的测试](testing/unit/medium/property_based_testing.md)
  - [测试架构设计](testing/unit/medium/test_architecture.md)
  - [测试数据构建器模式](testing/unit/medium/test_data_builders.md)
  - [测试指标分析与改进](testing/unit/medium/test_metrics_analysis.md)
  - [单元测试模式与反模式](testing/unit/medium/test_patterns.md)
- **Hard难度**：
  - [高级模拟框架设计](testing/unit/hard/advanced_mocking_framework.md)
  - [组合测试引擎设计](testing/unit/hard/combinatorial_testing_engine.md)
  - [协同测试框架设计](testing/unit/hard/concolic_testing_framework.md)
  - [差异测试系统设计](testing/unit/hard/differential_testing_system.md)
  - [模糊测试框架设计](testing/unit/hard/fuzz_testing_framework.md)
  - [程序不变量检测系统](testing/unit/hard/invariant_detection_system.md)
  - [变质测试系统设计](testing/unit/hard/metamorphic_testing.md)
  - [基于模型的测试系统](testing/unit/hard/model_based_testing.md)
  - [基于搜索的测试框架](testing/unit/hard/search_based_testing.md)
  - [符号执行测试引擎](testing/unit/hard/symbolic_execution_engine.md)
  - [测试框架设计与实现](testing/unit/hard/test_framework_design.md)
  - [自动测试生成引擎](testing/unit/hard/test_generation_engine.md)
#### Integration
- **Easy难度**：
  - [API契约测试](testing/integration/easy/api_contract_testing.md)
  - [认证系统集成测试](testing/integration/easy/authentication_testing.md)
  - [缓存系统集成测试](testing/integration/easy/cache_integration.md)
  - [配置系统集成测试](testing/integration/easy/configuration_testing.md)
  - [数据库集成测试](testing/integration/easy/database_integration.md)
  - [邮件服务集成测试](testing/integration/easy/email_service_testing.md)
  - [外部API集成测试](testing/integration/easy/external_api_testing.md)
  - [文件系统集成测试](testing/integration/easy/file_system_integration.md)
  - [日志系统集成测试](testing/integration/easy/logging_integration.md)
  - [消息队列集成测试](testing/integration/easy/message_queue_testing.md)
  - [定时任务集成测试](testing/integration/easy/scheduled_tasks_testing.md)
  - [集成测试环境搭建](testing/integration/easy/test_environment_setup.md)
- **Medium难度**：
  - [API网关集成测试](testing/integration/medium/api_gateway_testing.md)
  - [API测试自动化](testing/integration/medium/api_testing.md)
  - [缓存策略集成测试](testing/integration/medium/caching_strategy_testing.md)
  - [云服务集成测试](testing/integration/medium/cloud_service_integration.md)
  - [数据管道集成测试](testing/integration/medium/data_pipeline_testing.md)
  - [数据库迁移测试](testing/integration/medium/database_migration_testing.md)
  - [分布式事务测试](testing/integration/medium/distributed_transaction.md)
  - [事件驱动架构测试](testing/integration/medium/event_driven_testing.md)
  - [微服务集成测试](testing/integration/medium/microservice_integration.md)
  - [安全集成测试](testing/integration/medium/security_integration.md)
  - [第三方系统集成测试](testing/integration/medium/third_party_integration.md)
- **Hard难度**：
  - [API测试自动化框架](testing/integration/hard/api_testing_framework.md)
  - [区块链系统测试平台](testing/integration/hard/blockchain_testing_platform.md)
  - [持续集成测试平台](testing/integration/hard/continuous_integration_platform.md)
  - [数据库测试平台](testing/integration/hard/database_testing_platform.md)
  - [分布式系统测试平台](testing/integration/hard/distributed_system_testing.md)
  - [事件溯源系统测试框架](testing/integration/hard/event_sourcing_testing.md)
  - [物联网系统测试框架](testing/integration/hard/iot_testing_framework.md)
  - [机器学习管道测试框架](testing/integration/hard/ml_pipeline_testing.md)
  - [实时系统测试框架](testing/integration/hard/real_time_system_testing.md)
  - [无服务器应用测试平台](testing/integration/hard/serverless_testing_platform.md)
  - [服务网格测试框架](testing/integration/hard/service_mesh_testing.md)
#### Performance
- **Easy难度**：
  - [API性能测试](testing/performance/easy/api_performance_testing.md)
  - [基准性能测试](testing/performance/easy/baseline_performance_testing.md)
  - [数据库性能测试](testing/performance/easy/database_performance_testing.md)
  - [负载测试基础](testing/performance/easy/load_testing_basics.md)
  - [内存使用测试](testing/performance/easy/memory_usage_testing.md)
  - [资源利用率测试](testing/performance/easy/resource_utilization_testing.md)
  - [响应时间测试](testing/performance/easy/response_time_testing.md)
  - [可扩展性测试](testing/performance/easy/scalability_testing.md)
  - [压力测试基础](testing/performance/easy/stress_testing_basics.md)
  - [吞吐量测试](testing/performance/easy/throughput_testing.md)
  - [Web页面性能测试](testing/performance/easy/web_page_performance_testing.md)
- **Medium难度**：
  - [API网关性能测试](testing/performance/medium/api_gateway_performance_testing.md)
  - [缓存策略测试](testing/performance/medium/caching_strategy_testing.md)
  - [容器性能测试](testing/performance/medium/container_performance_testing.md)
  - [数据库优化测试](testing/performance/medium/database_optimization_testing.md)
  - [分布式负载测试](testing/performance/medium/distributed_load_testing.md)
  - [前端性能测试](testing/performance/medium/frontend_performance_testing.md)
  - [消息队列性能测试](testing/performance/medium/message_queue_performance_testing.md)
  - [微服务性能测试](testing/performance/medium/microservices_performance_testing.md)
  - [移动应用性能测试](testing/performance/medium/mobile_app_performance_testing.md)
  - [性能剖析与分析](testing/performance/medium/performance_profiling.md)
  - [无服务器性能测试](testing/performance/medium/serverless_performance_testing.md)
- **Hard难度**：
  - [AI模型性能优化框架](testing/performance/hard/ai_model_performance_optimization.md)
  - [混沌工程测试平台](testing/performance/hard/chaos_engineering_platform.md)
  - [云成本性能优化系统](testing/performance/hard/cloud_cost_performance_optimization.md)
  - [数据库基准测试框架](testing/performance/hard/database_benchmark_framework.md)
  - [分布式系统性能建模](testing/performance/hard/distributed_system_performance_modeling.md)
  - [分布式追踪分析平台](testing/performance/hard/distributed_tracing_analysis_platform.md)
  - [游戏引擎性能测试框架](testing/performance/hard/game_engine_performance_framework.md)
  - [性能测试框架设计与实现](testing/performance/hard/performance_testing_framework.md)
  - [实时性能监控系统](testing/performance/hard/real_time_performance_monitoring.md)
  - [流数据处理系统基准测试](testing/performance/hard/streaming_data_processing_benchmark.md)
  - [Web前端性能实验室](testing/performance/hard/web_frontend_performance_lab.md)
#### E2e
- **Easy难度**：
  - [API工作流端到端测试](testing/e2e/easy/api_workflow_testing.md)
  - [数据库工作流端到端测试](testing/e2e/easy/database_workflow_testing.md)
  - [文件上传端到端测试](testing/e2e/easy/file_upload_testing.md)
  - [移动应用端到端测试](testing/e2e/easy/mobile_app_testing.md)
  - [通知系统端到端测试](testing/e2e/easy/notification_system_testing.md)
  - [支付处理端到端测试](testing/e2e/easy/payment_processing_testing.md)
  - [搜索功能端到端测试](testing/e2e/easy/search_functionality_testing.md)
  - [购物车端到端测试](testing/e2e/easy/shopping_cart_testing.md)
  - [用户资料端到端测试](testing/e2e/easy/user_profile_testing.md)
  - [用户注册端到端测试](testing/e2e/easy/user_registration_testing.md)
  - [Web UI端到端测试](testing/e2e/easy/web_ui_testing.md)
- **Medium难度**：
  - [无障碍性端到端测试](testing/e2e/medium/accessibility_testing.md)
  - [跨浏览器端到端测试](testing/e2e/medium/cross_browser_testing.md)
  - [数据驱动端到端测试](testing/e2e/medium/data_driven_testing.md)
  - [国际化端到端测试](testing/e2e/medium/internationalization_testing.md)
  - [多设备端到端测试](testing/e2e/medium/multi_device_testing.md)
  - [多租户端到端测试](testing/e2e/medium/multi_tenant_testing.md)
  - [离线模式端到端测试](testing/e2e/medium/offline_mode_testing.md)
  - [实时应用端到端测试](testing/e2e/medium/real_time_application_testing.md)
  - [安全工作流端到端测试](testing/e2e/medium/security_workflow_testing.md)
  - [视觉回归测试](testing/e2e/medium/visual_regression_testing.md)
  - [工作流自动化端到端测试](testing/e2e/medium/workflow_automation_testing.md)
- **Hard难度**：
  - [AI系统端到端测试框架](testing/e2e/hard/ai_system_testing_framework.md)
  - [AR/VR应用测试框架](testing/e2e/hard/ar_vr_testing_framework.md)
  - [自主系统测试平台](testing/e2e/hard/autonomous_system_testing_platform.md)
  - [区块链DApp测试框架](testing/e2e/hard/blockchain_dapp_testing_framework.md)
  - [云原生应用测试平台](testing/e2e/hard/cloud_native_testing_platform.md)
  - [数字孪生测试平台](testing/e2e/hard/digital_twin_testing_platform.md)
  - [分布式系统端到端测试框架](testing/e2e/hard/distributed_system_e2e_framework.md)
  - [端到端测试框架设计与实现](testing/e2e/hard/e2e_testing_framework.md)
  - [金融科技系统测试平台](testing/e2e/hard/fintech_system_testing_platform.md)
  - [物联网平台测试框架](testing/e2e/hard/iot_platform_testing_framework.md)
  - [微服务架构测试平台](testing/e2e/hard/microservices_testing_platform.md)
  - [SaaS平台测试框架](testing/e2e/hard/saas_platform_testing_framework.md)

### Operations维度案例

#### Cicd
- **Medium难度**：
  - [CI/CD流水线配置](operations/cicd/medium/cicd_pipeline_setup.md)
#### Container
- **Easy难度**：
  - [简单Docker容器部署](operations/container/easy/simple_docker_deployment.md)
- **Hard难度**：
  - [微服务架构部署与管理](operations/container/hard/microservices_deployment.md)
#### Infrastructure
- **Easy难度**：
  - [运维基础环境搭建](operations/infrastructure/easy/ops_environment_setup.md)
### Development维度案例

#### Middleware
- **Easy难度**：
  - [Consul服务发现配置](development/middleware/easy/consul_service_discovery.md)
  - [Docker Compose基础配置](development/middleware/easy/docker_compose_setup.md)
  - [Elasticsearch基础配置](development/middleware/easy/elasticsearch_setup.md)
  - [etcd分布式键值存储配置](development/middleware/easy/etcd_configuration.md)
  - [HAProxy负载均衡配置](development/middleware/easy/haproxy_load_balancer.md)
  - [Kafka基础配置](development/middleware/easy/kafka_basic_setup.md)
  - [Logstash日志处理配置](development/middleware/easy/logstash_config.md)
  - [Nginx基础配置](development/middleware/easy/nginx_config.md)
  - [Prometheus监控配置](development/middleware/easy/prometheus_monitoring.md)
  - [RabbitMQ消息队列集成](development/middleware/easy/rabbitmq_integration.md)
  - [Redis基础缓存实现](development/middleware/easy/redis_basic_cache.md)
  - [Traefik边缘路由器配置](development/middleware/easy/traefik_edge_router.md)
  - [ZooKeeper集群配置](development/middleware/easy/zookeeper_cluster.md)
- **Medium难度**：
  - [Elasticsearch高级功能实现](development/middleware/medium/elasticsearch_advanced.md)
  - [Envoy服务网格实现](development/middleware/medium/envoy_service_mesh.md)
  - [etcd分布式协调应用](development/middleware/medium/etcd_distributed_coordination.md)
  - [Kafka Streams数据处理](development/middleware/medium/kafka_streams_processing.md)
  - [Kong API网关实现](development/middleware/medium/kong_api_gateway.md)
  - [Nginx高级功能实现](development/middleware/medium/nginx_advanced.md)
  - [Prometheus与Grafana高级监控](development/middleware/medium/prometheus_grafana_advanced.md)
  - [Apache Pulsar消息系统](development/middleware/medium/pulsar_messaging.md)
  - [RabbitMQ高级模式实现](development/middleware/medium/rabbitmq_advanced.md)
  - [Redis分布式缓存策略实现](development/middleware/medium/redis_cache_strategy.md)
  - [Redis集群与哨兵配置](development/middleware/medium/redis_cluster_sentinel.md)
- **Hard难度**：
  - [API网关框架设计与实现](development/middleware/hard/api_gateway_framework.md)
  - [分布式缓存系统设计](development/middleware/hard/distributed_cache_system.md)
  - [分布式锁服务设计](development/middleware/hard/distributed_lock_service.md)
  - [分布式消息队列系统设计](development/middleware/hard/distributed_message_queue.md)
  - [分布式任务调度系统](development/middleware/hard/distributed_task_scheduler.md)
  - [分布式追踪系统设计](development/middleware/hard/distributed_tracing_system.md)
  - [服务网格控制平面设计](development/middleware/hard/service_mesh_control_plane.md)
  - [流处理引擎设计](development/middleware/hard/stream_processing_engine.md)
#### Database
- **Easy难度**：
  - [Cassandra NoSQL数据库应用](development/database/easy/cassandra_nosql.md)
  - [CouchDB文档数据库应用](development/database/easy/couchdb_document_db.md)
  - [DynamoDB无服务器数据库应用](development/database/easy/dynamodb_serverless.md)
  - [Elasticsearch基础应用](development/database/easy/elasticsearch_basic.md)
  - [InfluxDB时序数据应用](development/database/easy/influxdb_time_series.md)
  - [MongoDB CRUD操作](development/database/easy/mongodb_crud.md)
  - [MySQL基础查询优化](development/database/easy/mysql_query_optimization.md)
  - [Neo4j图数据库应用](development/database/easy/neo4j_graph_database.md)
  - [PostgreSQL基础操作](development/database/easy/postgresql_basic_operations.md)
  - [Redis数据结构应用](development/database/easy/redis_data_structures.md)
  - [SQLite嵌入式数据库应用](development/database/easy/sqlite_embedded_db.md)
- **Medium难度**：
  - [数据仓库设计与实现](development/database/medium/data_warehouse_design.md)
  - [数据库迁移与转换](development/database/medium/database_migration.md)
  - [数据库复制与同步](development/database/medium/database_replication.md)
  - [Elasticsearch高级搜索引擎](development/database/medium/elasticsearch_advanced_search.md)
  - [图数据库应用开发](development/database/medium/graph_database_application.md)
  - [MongoDB聚合管道开发](development/database/medium/mongodb_aggregation.md)
  - [多模型数据库应用](development/database/medium/multi_model_database.md)
  - [MySQL性能调优](development/database/medium/mysql_performance_tuning.md)
  - [PostgreSQL高级功能应用](development/database/medium/postgresql_advanced.md)
  - [Redis高级模式实现](development/database/medium/redis_advanced_patterns.md)
  - [时序数据库设计与应用](development/database/medium/time_series_database.md)
- **Hard难度**：
  - [列式存储引擎设计](development/database/hard/columnar_storage_engine.md)
  - [数据库查询优化器设计](development/database/hard/database_query_optimizer.md)
  - [分布式SQL查询引擎](development/database/hard/distributed_sql_engine.md)
  - [分布式事务系统设计](development/database/hard/distributed_transaction.md)
  - [图数据库引擎设计](development/database/hard/graph_database_engine.md)
  - [多模型数据库引擎设计](development/database/hard/multi_model_database_engine.md)
  - [数据库分库分表方案设计与实现](development/database/hard/sharding_solution.md)
  - [流式数据库系统设计](development/database/hard/streaming_database_system.md)
  - [时序数据库引擎设计](development/database/hard/time_series_database_engine.md)
  - [向量数据库实现](development/database/hard/vector_database_implementation.md)
#### Frontend
- **Easy难度**：
  - [Android基础UI组件实现](development/frontend/easy/android_ui_basic.md)
  - [CSS动画效果实现](development/frontend/easy/css_animation.md)
  - [Flutter UI组件实现](development/frontend/easy/flutter_ui_widgets.md)
  - [HTML5 Canvas绘图应用](development/frontend/easy/html5_canvas_drawing.md)
  - [iOS列表视图实现](development/frontend/easy/ios_list_view.md)
  - [JavaScript表单验证](development/frontend/easy/javascript_form_validation.md)
  - [React基础组件库开发](development/frontend/easy/react_component_library.md)
  - [HTML/CSS响应式布局实现](development/frontend/easy/responsive_layout.md)
  - [静态博客网站模板](development/frontend/easy/static_blog_template.md)
  - [SVG图标动画实现](development/frontend/easy/svg_icon_animation.md)
  - [Vue.js待办事项应用](development/frontend/easy/vue_todo_app.md)
  - [Web无障碍性优化](development/frontend/easy/web_accessibility.md)
- **Medium难度**：
  - [Angular数据仪表盘实现](development/frontend/medium/angular_dashboard.md)
  - [Electron大模型ChatBox应用](development/frontend/medium/electron_chatbox_app.md)
  - [Electron AWS S3管理工具](development/frontend/medium/electron_s3_manager.md)
  - [Flutter状态管理实现](development/frontend/medium/flutter_state_management.md)
  - [渐进式Web应用(PWA)实现](development/frontend/medium/progressive_web_app.md)
  - [React Hooks高级应用](development/frontend/medium/react_hooks_advanced.md)
  - [React Native社交应用](development/frontend/medium/react_native_social_app.md)
  - [React状态管理实现](development/frontend/medium/react_state_management.md)
  - [Svelte实时协作应用](development/frontend/medium/svelte_realtime_app.md)
  - [TypeScript设计模式实现](development/frontend/medium/typescript_design_patterns.md)
  - [Vue.js电商前端实现](development/frontend/medium/vue_ecommerce.md)
  - [Web动画库开发](development/frontend/medium/web_animation_library.md)
  - [WebGL 3D模型查看器](development/frontend/medium/webgl_3d_viewer.md)
- **Hard难度**：
  - [跨平台设计系统实现](development/frontend/hard/cross_platform_design_system.md)
  - [GraphQL客户端框架实现](development/frontend/hard/graphql_client_framework.md)
  - [微前端架构设计与实现](development/frontend/hard/micro_frontend_architecture.md)
  - [离线优先PWA应用框架](development/frontend/hard/offline_first_pwa.md)
  - [React应用性能优化](development/frontend/hard/react_performance_optimization.md)
  - [实时协作引擎实现](development/frontend/hard/realtime_collaboration_engine.md)
  - [虚拟DOM实现与渲染引擎](development/frontend/hard/virtual_dom_implementation.md)
  - [Web 3D游戏引擎开发](development/frontend/hard/web_3d_game_engine.md)
  - [Web无障碍性框架开发](development/frontend/hard/web_accessibility_framework.md)
  - [Web AR框架开发](development/frontend/hard/web_ar_framework.md)
  - [Web编译器/解释器实现](development/frontend/hard/web_compiler_interpreter.md)
  - [WebAssembly图像处理应用](development/frontend/hard/webassembly_image_processing.md)
#### Backend
- **Easy难度**：
  - [C# ASP.NET MVC应用](development/backend/easy/csharp_aspnet_mvc.md)
  - [Java开发环境搭建](development/backend/easy/dev_environment_setup.md)
  - [Go语言HTTP服务器](development/backend/easy/go_http_server.md)
  - [Java Servlet Web应用](development/backend/easy/java_servlet_app.md)
  - [Kotlin Spring Boot应用](development/backend/easy/kotlin_spring_boot.md)
  - [Node.js RESTful API实现](development/backend/easy/node_rest_api.md)
  - [PHP Laravel CRUD应用](development/backend/easy/php_laravel_crud.md)
  - [Python FastAPI服务](development/backend/easy/python_fastapi.md)
  - [Python Flask Web应用](development/backend/easy/python_flask_web.md)
  - [Ruby on Rails博客应用](development/backend/easy/ruby_rails_blog.md)
  - [Rust Actix Web API](development/backend/easy/rust_actix_api.md)
  - [Spring Boot RESTful API实现](development/backend/easy/spring_boot_rest_api.md)
- **Medium难度**：
  - [C# SignalR实时应用](development/backend/medium/csharp_signalr_realtime.md)
  - [设计模式应用](development/backend/medium/design_patterns.md)
  - [Go并发模式实现](development/backend/medium/go_concurrency_patterns.md)
  - [Go微服务开发](development/backend/medium/go_microservices.md)
  - [Java多线程并发应用](development/backend/medium/java_multithreading.md)
  - [Java响应式API实现](development/backend/medium/java_reactive_api.md)
  - [Kotlin协程应用](development/backend/medium/kotlin_coroutines.md)
  - [Node.js GraphQL API实现](development/backend/medium/node_graphql_api.md)
  - [Node.js WebSocket服务器](development/backend/medium/node_websocket_server.md)
  - [PHP API Platform实现](development/backend/medium/php_api_platform.md)
  - [Python Celery任务队列](development/backend/medium/python_celery_tasks.md)
  - [Python Django电商后端](development/backend/medium/python_django_ecommerce.md)
  - [Rust异步Web服务器](development/backend/medium/rust_async_server.md)
  - [Spring Cloud微服务架构实现](development/backend/medium/spring_cloud_microservices.md)
- **Hard难度**：
  - [区块链系统实现](development/backend/hard/blockchain_implementation.md)
  - [分布式数据库系统](development/backend/hard/distributed_database.md)
  - [分布式系统设计与实现](development/backend/hard/distributed_system.md)
  - [分布式事务处理系统设计与实现](development/backend/hard/distributed_transaction.md)
  - [事件溯源与CQRS架构](development/backend/hard/event_sourcing_cqrs.md)
  - [机器学习模型服务平台](development/backend/hard/ml_serving_platform.md)
  - [实时数据分析引擎](development/backend/hard/realtime_analytics_engine.md)
  - [Serverless计算平台](development/backend/hard/serverless_platform.md)
  - [服务网格实现](development/backend/hard/service_mesh_implementation.md)
  - [基于SkipList实现MySQL存储引擎](development/backend/hard/skiplist_storage_engine.md)
#### Algorithm
- **Easy难度**：
  - [数组操作基础算法](development/algorithm/easy/array_manipulation.md)
  - [二分查找算法](development/algorithm/easy/binary_search.md)
  - [二叉树遍历算法](development/algorithm/easy/binary_tree_traversal.md)
  - [动态规划基础](development/algorithm/easy/dynamic_programming_basics.md)
  - [图遍历算法](development/algorithm/easy/graph_traversal.md)
  - [贪心算法实现](development/algorithm/easy/greedy_algorithms.md)
  - [哈希表实现](development/algorithm/easy/hash_table_implementation.md)
  - [链表操作算法](development/algorithm/easy/linked_list_operations.md)
  - [递归与回溯算法](development/algorithm/easy/recursion_and_backtracking.md)
  - [排序算法实现](development/algorithm/easy/sorting_algorithms.md)
  - [栈和队列实现](development/algorithm/easy/stack_queue_implementation.md)
- **Medium难度**：
  - [高级数据结构实现](development/algorithm/medium/advanced_data_structures.md)
  - [高级动态规划](development/algorithm/medium/advanced_dynamic_programming.md)
  - [高级图算法](development/algorithm/medium/advanced_graph_algorithms.md)
  - [位运算算法](development/algorithm/medium/bit_manipulation.md)
  - [计算几何算法](development/algorithm/medium/computational_geometry.md)
  - [分治算法](development/algorithm/medium/divide_and_conquer.md)
  - [机器学习基础算法](development/algorithm/medium/machine_learning_algorithms.md)
  - [数论算法](development/algorithm/medium/number_theory_algorithms.md)
  - [优化算法](development/algorithm/medium/optimization_algorithms.md)
  - [随机化算法](development/algorithm/medium/randomized_algorithms.md)
  - [字符串算法](development/algorithm/medium/string_algorithms.md)
- **Hard难度**：
  - [高级图论算法](development/algorithm/hard/advanced_graph_theory.md)
  - [高级优化算法](development/algorithm/hard/advanced_optimization_algorithms.md)
  - [编译器设计算法](development/algorithm/hard/compiler_design_algorithms.md)
  - [数据压缩算法](development/algorithm/hard/compression_algorithms.md)
  - [高级计算几何算法](development/algorithm/hard/computational_geometry_advanced.md)
  - [计算机视觉算法](development/algorithm/hard/computer_vision_algorithms.md)
  - [密码学算法实现](development/algorithm/hard/cryptographic_algorithms.md)
  - [深度学习算法实现](development/algorithm/hard/deep_learning_algorithms.md)
  - [遗传与进化算法](development/algorithm/hard/genetic_evolutionary_algorithms.md)
  - [自然语言处理算法](development/algorithm/hard/natural_language_processing.md)
  - [并行与分布式算法](development/algorithm/hard/parallel_distributed_algorithms.md)
  - [概率图模型](development/algorithm/hard/probabilistic_graphical_models.md)
  - [量子计算算法](development/algorithm/hard/quantum_computing_algorithms.md)
  - [强化学习算法](development/algorithm/hard/reinforcement_learning.md)

### Testing维度案例

#### Unit
- **Easy难度**：
  - [断言技术与最佳实践](testing/unit/easy/assertion_techniques.md)
  - [边界值测试设计](testing/unit/easy/boundary_testing.md)
  - [代码覆盖率分析与提升](testing/unit/easy/code_coverage.md)
  - [异常测试技术](testing/unit/easy/exception_testing.md)
  - [模拟对象创建与使用](testing/unit/easy/mock_objects.md)
  - [参数化测试实现](testing/unit/easy/parameterized_tests.md)
  - [私有方法测试策略](testing/unit/easy/private_method_testing.md)
  - [测试替身类型与应用](testing/unit/easy/test_doubles.md)
  - [测试驱动开发实践](testing/unit/easy/test_driven_development.md)
  - [测试夹具设计与使用](testing/unit/easy/test_fixtures.md)
  - [测试命名约定与组织](testing/unit/easy/test_naming_conventions.md)
  - [基础单元测试编写](testing/unit/easy/unit_testing.md)
- **Medium难度**：
  - [行为驱动开发实践](testing/unit/medium/behavior_driven_development.md)
  - [并发代码测试技术](testing/unit/medium/concurrent_code_testing.md)
  - [依赖注入与可测试设计](testing/unit/medium/dependency_injection.md)
  - [遗留代码测试策略](testing/unit/medium/legacy_code_testing.md)
  - [变异测试实践](testing/unit/medium/mutation_testing.md)
  - [基于属性的测试](testing/unit/medium/property_based_testing.md)
  - [测试架构设计](testing/unit/medium/test_architecture.md)
  - [测试数据构建器模式](testing/unit/medium/test_data_builders.md)
  - [测试指标分析与改进](testing/unit/medium/test_metrics_analysis.md)
  - [单元测试模式与反模式](testing/unit/medium/test_patterns.md)
- **Hard难度**：
  - [高级模拟框架设计](testing/unit/hard/advanced_mocking_framework.md)
  - [组合测试引擎设计](testing/unit/hard/combinatorial_testing_engine.md)
  - [协同测试框架设计](testing/unit/hard/concolic_testing_framework.md)
  - [差异测试系统设计](testing/unit/hard/differential_testing_system.md)
  - [模糊测试框架设计](testing/unit/hard/fuzz_testing_framework.md)
  - [程序不变量检测系统](testing/unit/hard/invariant_detection_system.md)
  - [变质测试系统设计](testing/unit/hard/metamorphic_testing.md)
  - [基于模型的测试系统](testing/unit/hard/model_based_testing.md)
  - [基于搜索的测试框架](testing/unit/hard/search_based_testing.md)
  - [符号执行测试引擎](testing/unit/hard/symbolic_execution_engine.md)
  - [测试框架设计与实现](testing/unit/hard/test_framework_design.md)
  - [自动测试生成引擎](testing/unit/hard/test_generation_engine.md)
#### Integration
- **Easy难度**：
  - [API契约测试](testing/integration/easy/api_contract_testing.md)
  - [认证系统集成测试](testing/integration/easy/authentication_testing.md)
  - [缓存系统集成测试](testing/integration/easy/cache_integration.md)
  - [配置系统集成测试](testing/integration/easy/configuration_testing.md)
  - [数据库集成测试](testing/integration/easy/database_integration.md)
  - [邮件服务集成测试](testing/integration/easy/email_service_testing.md)
  - [外部API集成测试](testing/integration/easy/external_api_testing.md)
  - [文件系统集成测试](testing/integration/easy/file_system_integration.md)
  - [日志系统集成测试](testing/integration/easy/logging_integration.md)
  - [消息队列集成测试](testing/integration/easy/message_queue_testing.md)
  - [定时任务集成测试](testing/integration/easy/scheduled_tasks_testing.md)
  - [集成测试环境搭建](testing/integration/easy/test_environment_setup.md)
- **Medium难度**：
  - [API网关集成测试](testing/integration/medium/api_gateway_testing.md)
  - [API测试自动化](testing/integration/medium/api_testing.md)
  - [缓存策略集成测试](testing/integration/medium/caching_strategy_testing.md)
  - [云服务集成测试](testing/integration/medium/cloud_service_integration.md)
  - [数据管道集成测试](testing/integration/medium/data_pipeline_testing.md)
  - [数据库迁移测试](testing/integration/medium/database_migration_testing.md)
  - [分布式事务测试](testing/integration/medium/distributed_transaction.md)
  - [事件驱动架构测试](testing/integration/medium/event_driven_testing.md)
  - [微服务集成测试](testing/integration/medium/microservice_integration.md)
  - [安全集成测试](testing/integration/medium/security_integration.md)
  - [第三方系统集成测试](testing/integration/medium/third_party_integration.md)
- **Hard难度**：
  - [API测试自动化框架](testing/integration/hard/api_testing_framework.md)
  - [区块链系统测试平台](testing/integration/hard/blockchain_testing_platform.md)
  - [持续集成测试平台](testing/integration/hard/continuous_integration_platform.md)
  - [数据库测试平台](testing/integration/hard/database_testing_platform.md)
  - [分布式系统测试平台](testing/integration/hard/distributed_system_testing.md)
  - [事件溯源系统测试框架](testing/integration/hard/event_sourcing_testing.md)
  - [物联网系统测试框架](testing/integration/hard/iot_testing_framework.md)
  - [机器学习管道测试框架](testing/integration/hard/ml_pipeline_testing.md)
  - [实时系统测试框架](testing/integration/hard/real_time_system_testing.md)
  - [无服务器应用测试平台](testing/integration/hard/serverless_testing_platform.md)
  - [服务网格测试框架](testing/integration/hard/service_mesh_testing.md)
#### Performance
- **Easy难度**：
  - [API性能测试](testing/performance/easy/api_performance_testing.md)
  - [基准性能测试](testing/performance/easy/baseline_performance_testing.md)
  - [数据库性能测试](testing/performance/easy/database_performance_testing.md)
  - [负载测试基础](testing/performance/easy/load_testing_basics.md)
  - [内存使用测试](testing/performance/easy/memory_usage_testing.md)
  - [资源利用率测试](testing/performance/easy/resource_utilization_testing.md)
  - [响应时间测试](testing/performance/easy/response_time_testing.md)
  - [可扩展性测试](testing/performance/easy/scalability_testing.md)
  - [压力测试基础](testing/performance/easy/stress_testing_basics.md)
  - [吞吐量测试](testing/performance/easy/throughput_testing.md)
  - [Web页面性能测试](testing/performance/easy/web_page_performance_testing.md)
- **Medium难度**：
  - [API网关性能测试](testing/performance/medium/api_gateway_performance_testing.md)
  - [缓存策略测试](testing/performance/medium/caching_strategy_testing.md)
  - [容器性能测试](testing/performance/medium/container_performance_testing.md)
  - [数据库优化测试](testing/performance/medium/database_optimization_testing.md)
  - [分布式负载测试](testing/performance/medium/distributed_load_testing.md)
  - [前端性能测试](testing/performance/medium/frontend_performance_testing.md)
  - [消息队列性能测试](testing/performance/medium/message_queue_performance_testing.md)
  - [微服务性能测试](testing/performance/medium/microservices_performance_testing.md)
  - [移动应用性能测试](testing/performance/medium/mobile_app_performance_testing.md)
  - [性能剖析与分析](testing/performance/medium/performance_profiling.md)
  - [无服务器性能测试](testing/performance/medium/serverless_performance_testing.md)
- **Hard难度**：
  - [AI模型性能优化框架](testing/performance/hard/ai_model_performance_optimization.md)
  - [混沌工程测试平台](testing/performance/hard/chaos_engineering_platform.md)
  - [云成本性能优化系统](testing/performance/hard/cloud_cost_performance_optimization.md)
  - [数据库基准测试框架](testing/performance/hard/database_benchmark_framework.md)
  - [分布式系统性能建模](testing/performance/hard/distributed_system_performance_modeling.md)
  - [分布式追踪分析平台](testing/performance/hard/distributed_tracing_analysis_platform.md)
  - [游戏引擎性能测试框架](testing/performance/hard/game_engine_performance_framework.md)
  - [性能测试框架设计与实现](testing/performance/hard/performance_testing_framework.md)
  - [实时性能监控系统](testing/performance/hard/real_time_performance_monitoring.md)
  - [流数据处理系统基准测试](testing/performance/hard/streaming_data_processing_benchmark.md)
  - [Web前端性能实验室](testing/performance/hard/web_frontend_performance_lab.md)
#### E2e
- **Easy难度**：
  - [API工作流端到端测试](testing/e2e/easy/api_workflow_testing.md)
  - [数据库工作流端到端测试](testing/e2e/easy/database_workflow_testing.md)
  - [文件上传端到端测试](testing/e2e/easy/file_upload_testing.md)
  - [移动应用端到端测试](testing/e2e/easy/mobile_app_testing.md)
  - [通知系统端到端测试](testing/e2e/easy/notification_system_testing.md)
  - [支付处理端到端测试](testing/e2e/easy/payment_processing_testing.md)
  - [搜索功能端到端测试](testing/e2e/easy/search_functionality_testing.md)
  - [购物车端到端测试](testing/e2e/easy/shopping_cart_testing.md)
  - [用户资料端到端测试](testing/e2e/easy/user_profile_testing.md)
  - [用户注册端到端测试](testing/e2e/easy/user_registration_testing.md)
  - [Web UI端到端测试](testing/e2e/easy/web_ui_testing.md)
- **Medium难度**：
  - [无障碍性端到端测试](testing/e2e/medium/accessibility_testing.md)
  - [跨浏览器端到端测试](testing/e2e/medium/cross_browser_testing.md)
  - [数据驱动端到端测试](testing/e2e/medium/data_driven_testing.md)
  - [国际化端到端测试](testing/e2e/medium/internationalization_testing.md)
  - [多设备端到端测试](testing/e2e/medium/multi_device_testing.md)
  - [多租户端到端测试](testing/e2e/medium/multi_tenant_testing.md)
  - [离线模式端到端测试](testing/e2e/medium/offline_mode_testing.md)
  - [实时应用端到端测试](testing/e2e/medium/real_time_application_testing.md)
  - [安全工作流端到端测试](testing/e2e/medium/security_workflow_testing.md)
  - [视觉回归测试](testing/e2e/medium/visual_regression_testing.md)
  - [工作流自动化端到端测试](testing/e2e/medium/workflow_automation_testing.md)
- **Hard难度**：
  - [AI系统端到端测试框架](testing/e2e/hard/ai_system_testing_framework.md)
  - [AR/VR应用测试框架](testing/e2e/hard/ar_vr_testing_framework.md)
  - [自主系统测试平台](testing/e2e/hard/autonomous_system_testing_platform.md)
  - [区块链DApp测试框架](testing/e2e/hard/blockchain_dapp_testing_framework.md)
  - [云原生应用测试平台](testing/e2e/hard/cloud_native_testing_platform.md)
  - [数字孪生测试平台](testing/e2e/hard/digital_twin_testing_platform.md)
  - [分布式系统端到端测试框架](testing/e2e/hard/distributed_system_e2e_framework.md)
  - [端到端测试框架设计与实现](testing/e2e/hard/e2e_testing_framework.md)
  - [金融科技系统测试平台](testing/e2e/hard/fintech_system_testing_platform.md)
  - [物联网平台测试框架](testing/e2e/hard/iot_platform_testing_framework.md)
  - [微服务架构测试平台](testing/e2e/hard/microservices_testing_platform.md)
  - [SaaS平台测试框架](testing/e2e/hard/saas_platform_testing_framework.md)

### Operations维度案例

#### Cicd
- **Medium难度**：
  - [CI/CD流水线配置](operations/cicd/medium/cicd_pipeline_setup.md)
#### Container
- **Easy难度**：
  - [简单Docker容器部署](operations/container/easy/simple_docker_deployment.md)
- **Hard难度**：
  - [微服务架构部署与管理](operations/container/hard/microservices_deployment.md)
#### Infrastructure
- **Easy难度**：
  - [运维基础环境搭建](operations/infrastructure/easy/ops_environment_setup.md)
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