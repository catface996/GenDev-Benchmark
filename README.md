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
│   ├── security/                             # 安全测试案例
│   │   ├── easy/                             # 低难度安全测试案例
│   │   ├── medium/                           # 中难度安全测试案例
│   │   └── hard/                             # 高难度安全测试案例
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
- **高难度**：
  - [分布式系统设计与实现](development/backend/hard/distributed_system.md)
  - [分布式事务处理系统设计与实现](development/backend/hard/distributed_transaction.md)
  - [基于SkipList实现MySQL存储引擎](development/backend/hard/skiplist_storage_engine.md)

#### 中间件
- **中难度**：
  - [Redis分布式缓存策略实现](development/middleware/medium/redis_cache_strategy.md)

#### 数据库
- **低难度**：
  - [MySQL基础查询优化](development/database/easy/mysql_query_optimization.md)
- **高难度**：
  - [数据库分库分表方案设计与实现](development/database/hard/sharding_solution.md)

#### 算法与数据结构
- **低难度**：
  - [数组操作基础算法](development/algorithm/easy/array_manipulation.md)

### 测试维度案例

#### 单元测试
- **低难度**：
  - [基础单元测试编写](testing/unit/easy/unit_testing.md)
  - [函数单元测试](testing/unit/easy/function_unit_testing.md)
  - [类单元测试](testing/unit/easy/class_unit_testing.md)
  - [参数化测试](testing/unit/easy/parameterized_testing.md)
  - [模拟对象测试](testing/unit/easy/mock_object_testing.md)
  - [异常测试](testing/unit/easy/exception_testing.md)
  - [测试驱动开发](testing/unit/easy/test_driven_development.md)
  - [代码覆盖率测试](testing/unit/easy/code_coverage_testing.md)
  - [断言测试](testing/unit/easy/assertion_testing.md)
  - [测试夹具设置](testing/unit/easy/test_fixture_setup.md)
  - [边界值测试](testing/unit/easy/boundary_value_testing.md)
  - [测试组织与管理](testing/unit/easy/test_organization.md)
- **中难度**：
  - [集成单元测试](testing/unit/medium/integration_unit_testing.md)
  - [行为驱动开发](testing/unit/medium/behavior_driven_development.md)
  - [基于属性的测试](testing/unit/medium/property_based_testing.md)
  - [变异测试](testing/unit/medium/mutation_testing.md)
  - [并发代码测试](testing/unit/medium/concurrent_code_testing.md)
  - [复杂对象测试](testing/unit/medium/complex_object_testing.md)
  - [数据库单元测试](testing/unit/medium/database_unit_testing.md)
  - [遗留代码测试](testing/unit/medium/legacy_code_testing.md)
  - [依赖注入测试](testing/unit/medium/dependency_injection_testing.md)
  - [API契约测试](testing/unit/medium/api_contract_testing.md)
  - [事件驱动架构测试](testing/unit/medium/event_driven_testing.md)
- **高难度**：
  - [性能单元测试框架](testing/unit/hard/performance_unit_testing.md)
  - [内存泄漏测试框架](testing/unit/hard/memory_leak_testing_framework.md)
  - [复杂算法测试框架](testing/unit/hard/complex_algorithm_testing.md)
  - [自动测试生成框架](testing/unit/hard/test_generation_framework.md)
  - [蜕变测试框架](testing/unit/hard/metamorphic_testing_framework.md)
  - [符号执行测试框架](testing/unit/hard/symbolic_execution_testing.md)
  - [模糊测试框架](testing/unit/hard/fuzz_testing_framework.md)
  - [具符结合测试框架](testing/unit/hard/concolic_testing_framework.md)
  - [基于模型的测试框架](testing/unit/hard/model_based_testing_framework.md)
  - [组合测试框架](testing/unit/hard/combinatorial_testing_framework.md)
  - [契约验证测试框架](testing/unit/hard/contract_verification_framework.md)
  - [量子算法测试框架](testing/unit/hard/quantum_algorithm_testing.md)

#### 集成测试
- **低难度**：
  - [集成测试环境搭建](testing/integration/easy/test_environment_setup.md)
  - [API契约测试](testing/integration/easy/api_contract_testing.md)
  - [认证测试](testing/integration/easy/authentication_testing.md)
  - [缓存集成测试](testing/integration/easy/cache_integration.md)
  - [配置测试](testing/integration/easy/configuration_testing.md)
  - [数据库集成测试](testing/integration/easy/database_integration.md)
  - [邮件服务测试](testing/integration/easy/email_service_testing.md)
  - [外部API测试](testing/integration/easy/external_api_testing.md)
  - [文件系统集成测试](testing/integration/easy/file_system_integration.md)
  - [日志集成测试](testing/integration/easy/logging_integration.md)
  - [消息队列测试](testing/integration/easy/message_queue_testing.md)
  - [定时任务测试](testing/integration/easy/scheduled_tasks_testing.md)
- **中难度**：
  - [API测试自动化](testing/integration/medium/api_testing.md)
  - [API网关测试](testing/integration/medium/api_gateway_testing.md)
  - [缓存策略测试](testing/integration/medium/caching_strategy_testing.md)
  - [云服务集成测试](testing/integration/medium/cloud_service_integration.md)
  - [数据管道测试](testing/integration/medium/data_pipeline_testing.md)
  - [数据库迁移测试](testing/integration/medium/database_migration_testing.md)
  - [分布式事务测试](testing/integration/medium/distributed_transaction.md)
  - [事件驱动测试](testing/integration/medium/event_driven_testing.md)
  - [微服务集成测试](testing/integration/medium/microservice_integration.md)
  - [安全集成测试](testing/integration/medium/security_integration.md)
  - [第三方集成测试](testing/integration/medium/third_party_integration.md)
- **高难度**：
  - [API测试框架](testing/integration/hard/api_testing_framework.md)
  - [区块链测试平台](testing/integration/hard/blockchain_testing_platform.md)
  - [持续集成平台](testing/integration/hard/continuous_integration_platform.md)
  - [数据库测试平台](testing/integration/hard/database_testing_platform.md)
  - [分布式系统测试](testing/integration/hard/distributed_system_testing.md)
  - [事件溯源测试](testing/integration/hard/event_sourcing_testing.md)
  - [IoT测试框架](testing/integration/hard/iot_testing_framework.md)
  - [机器学习管道测试](testing/integration/hard/ml_pipeline_testing.md)
  - [实时系统测试](testing/integration/hard/real_time_system_testing.md)
  - [无服务器测试平台](testing/integration/hard/serverless_testing_platform.md)
  - [服务网格测试](testing/integration/hard/service_mesh_testing.md)

#### 端到端测试
- **低难度**：
  - [API工作流测试](testing/e2e/easy/api_workflow_testing.md)
  - [数据库工作流测试](testing/e2e/easy/database_workflow_testing.md)
  - [文件上传测试](testing/e2e/easy/file_upload_testing.md)
  - [移动应用测试](testing/e2e/easy/mobile_app_testing.md)
  - [通知系统测试](testing/e2e/easy/notification_system_testing.md)
  - [支付处理测试](testing/e2e/easy/payment_processing_testing.md)
  - [搜索功能测试](testing/e2e/easy/search_functionality_testing.md)
  - [购物车测试](testing/e2e/easy/shopping_cart_testing.md)
  - [用户资料测试](testing/e2e/easy/user_profile_testing.md)
  - [用户注册测试](testing/e2e/easy/user_registration_testing.md)
  - [Web UI测试](testing/e2e/easy/web_ui_testing.md)
- **中难度**：
  - [无障碍测试](testing/e2e/medium/accessibility_testing.md)
  - [跨浏览器测试](testing/e2e/medium/cross_browser_testing.md)
  - [数据驱动测试](testing/e2e/medium/data_driven_testing.md)
  - [国际化测试](testing/e2e/medium/internationalization_testing.md)
  - [多设备测试](testing/e2e/medium/multi_device_testing.md)
  - [多租户测试](testing/e2e/medium/multi_tenant_testing.md)
  - [离线模式测试](testing/e2e/medium/offline_mode_testing.md)
  - [实时应用测试](testing/e2e/medium/real_time_application_testing.md)
  - [安全工作流测试](testing/e2e/medium/security_workflow_testing.md)
  - [视觉回归测试](testing/e2e/medium/visual_regression_testing.md)
  - [工作流自动化测试](testing/e2e/medium/workflow_automation_testing.md)
- **高难度**：
  - [端到端测试框架设计与实现](testing/e2e/hard/e2e_testing_framework.md)
  - [AI系统测试框架](testing/e2e/hard/ai_system_testing_framework.md)
  - [AR/VR测试框架](testing/e2e/hard/ar_vr_testing_framework.md)
  - [自主系统测试平台](testing/e2e/hard/autonomous_system_testing_platform.md)
  - [区块链DApp测试框架](testing/e2e/hard/blockchain_dapp_testing_framework.md)
  - [云原生测试平台](testing/e2e/hard/cloud_native_testing_platform.md)
  - [数字孪生测试平台](testing/e2e/hard/digital_twin_testing_platform.md)
  - [分布式系统端到端框架](testing/e2e/hard/distributed_system_e2e_framework.md)
  - [金融科技系统测试平台](testing/e2e/hard/fintech_system_testing_platform.md)
  - [IoT平台测试框架](testing/e2e/hard/iot_platform_testing_framework.md)
  - [微服务测试平台](testing/e2e/hard/microservices_testing_platform.md)
  - [SaaS平台测试框架](testing/e2e/hard/saas_platform_testing_framework.md)