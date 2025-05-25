# 研发维度基准测试

本目录包含用于评估AI代码生成工具在软件研发方面能力的基准测试案例。

## 目录结构

```
development/
├── frontend/                        # 前端开发案例
│   ├── easy/                        # 低难度前端案例
│   │   ├── android_ui_basic.md      # Android基础UI组件实现
│   │   ├── responsive_layout.md     # HTML/CSS响应式布局实现
│   │   ├── vue_todo_app.md          # Vue.js待办事项应用
│   │   ├── ios_list_view.md         # iOS列表视图实现
│   │   ├── javascript_form_validation.md # JavaScript表单验证
│   │   ├── css_animation.md         # CSS动画效果实现
│   │   ├── react_component_library.md # React基础组件库开发
│   │   ├── flutter_ui_widgets.md    # Flutter UI组件实现
│   │   ├── html5_canvas_drawing.md  # HTML5 Canvas绘图应用
│   │   ├── static_blog_template.md  # 静态博客网站模板
│   │   └── svg_icon_animation.md    # SVG图标动画实现
│   ├── medium/                      # 中难度前端案例
│   │   ├── react_state_management.md # React状态管理实现
│   │   ├── electron_chatbox_app.md  # Electron大模型ChatBox应用
│   │   ├── electron_s3_manager.md   # Electron AWS S3管理工具
│   │   ├── react_hooks_advanced.md  # React Hooks高级应用
│   │   ├── vue_ecommerce.md         # Vue.js电商前端实现
│   │   ├── flutter_state_management.md # Flutter状态管理实现
│   │   ├── typescript_design_patterns.md # TypeScript设计模式实现
│   │   ├── progressive_web_app.md   # 渐进式Web应用(PWA)实现
│   │   ├── angular_dashboard.md     # Angular数据仪表盘实现
│   │   ├── react_native_social_app.md # React Native社交应用
│   │   ├── web_animation_library.md # Web动画库开发
│   │   ├── webgl_3d_viewer.md       # WebGL 3D模型查看器
│   │   └── svelte_realtime_app.md   # Svelte实时协作应用
│   └── hard/                        # 高难度前端案例
│       ├── micro_frontend_architecture.md # 微前端架构设计与实现
│       ├── react_performance_optimization.md # React应用性能优化
│       ├── webassembly_image_processing.md # WebAssembly图像处理应用
│       ├── graphql_client_framework.md # GraphQL客户端框架实现
│       ├── virtual_dom_implementation.md # 虚拟DOM实现与渲染引擎
│       ├── web_3d_game_engine.md    # Web 3D游戏引擎开发
│       ├── cross_platform_design_system.md # 跨平台设计系统实现
│       ├── web_compiler_interpreter.md # Web编译器/解释器实现
│       ├── offline_first_pwa.md     # 离线优先PWA应用框架
│       ├── web_accessibility_framework.md # Web无障碍性框架开发
│       └── realtime_collaboration_engine.md # 实时协作引擎实现
├── backend/                         # 后端开发案例
│   ├── easy/                        # 低难度后端案例
│   │   ├── spring_boot_rest_api.md  # Spring Boot RESTful API实现
│   │   ├── dev_environment_setup.md # Java开发环境搭建
│   │   ├── node_rest_api.md         # Node.js RESTful API实现
│   │   ├── python_flask_web.md      # Python Flask Web应用
│   │   ├── go_http_server.md        # Go语言HTTP服务器
│   │   ├── java_servlet_app.md      # Java Servlet Web应用
│   │   ├── csharp_aspnet_mvc.md     # C# ASP.NET MVC应用
│   │   ├── php_laravel_crud.md      # PHP Laravel CRUD应用
│   │   ├── ruby_rails_blog.md       # Ruby on Rails博客应用
│   │   ├── python_fastapi.md        # Python FastAPI服务
│   │   ├── rust_actix_api.md        # Rust Actix Web API
│   │   └── kotlin_spring_boot.md    # Kotlin Spring Boot应用
│   ├── medium/                      # 中难度后端案例
│   │   ├── design_patterns.md       # 设计模式应用
│   │   ├── spring_cloud_microservices.md # Spring Cloud微服务架构实现
│   │   └── node_graphql_api.md      # Node.js GraphQL API实现
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
- **低难度**：
  - [Android基础UI组件实现](frontend/easy/android_ui_basic.md)
  - [HTML/CSS响应式布局实现](frontend/easy/responsive_layout.md)
  - [Vue.js待办事项应用](frontend/easy/vue_todo_app.md)
  - [iOS列表视图实现](frontend/easy/ios_list_view.md)
  - [JavaScript表单验证](frontend/easy/javascript_form_validation.md)
  - [CSS动画效果实现](frontend/easy/css_animation.md)
  - [React基础组件库开发](frontend/easy/react_component_library.md)
  - [Flutter UI组件实现](frontend/easy/flutter_ui_widgets.md)
  - [HTML5 Canvas绘图应用](frontend/easy/html5_canvas_drawing.md)
  - [静态博客网站模板](frontend/easy/static_blog_template.md)
  - [SVG图标动画实现](frontend/easy/svg_icon_animation.md)
- **中难度**：
  - [React状态管理实现](frontend/medium/react_state_management.md)
  - [Electron大模型ChatBox应用](frontend/medium/electron_chatbox_app.md)
  - [Electron AWS S3管理工具](frontend/medium/electron_s3_manager.md)
  - [React Hooks高级应用](frontend/medium/react_hooks_advanced.md)
  - [Vue.js电商前端实现](frontend/medium/vue_ecommerce.md)
  - [Flutter状态管理实现](frontend/medium/flutter_state_management.md)
  - [TypeScript设计模式实现](frontend/medium/typescript_design_patterns.md)
  - [渐进式Web应用(PWA)实现](frontend/medium/progressive_web_app.md)
  - [Angular数据仪表盘实现](frontend/medium/angular_dashboard.md)
  - [React Native社交应用](frontend/medium/react_native_social_app.md)
  - [Web动画库开发](frontend/medium/web_animation_library.md)
  - [WebGL 3D模型查看器](frontend/medium/webgl_3d_viewer.md)
  - [Svelte实时协作应用](frontend/medium/svelte_realtime_app.md)
- **高难度**：
  - [微前端架构设计与实现](frontend/hard/micro_frontend_architecture.md)
  - [React应用性能优化](frontend/hard/react_performance_optimization.md)
  - [WebAssembly图像处理应用](frontend/hard/webassembly_image_processing.md)
  - [GraphQL客户端框架实现](frontend/hard/graphql_client_framework.md)
  - [虚拟DOM实现与渲染引擎](frontend/hard/virtual_dom_implementation.md)
  - [Web 3D游戏引擎开发](frontend/hard/web_3d_game_engine.md)
  - [跨平台设计系统实现](frontend/hard/cross_platform_design_system.md)
  - [Web编译器/解释器实现](frontend/hard/web_compiler_interpreter.md)
  - [离线优先PWA应用框架](frontend/hard/offline_first_pwa.md)
  - [Web无障碍性框架开发](frontend/hard/web_accessibility_framework.md)
  - [实时协作引擎实现](frontend/hard/realtime_collaboration_engine.md)

### 后端开发
后端开发案例涵盖了从简单API实现到复杂分布式系统设计，包括多种编程语言和框架。

#### 案例列表
- **低难度**：
  - [Spring Boot RESTful API实现](backend/easy/spring_boot_rest_api.md)
  - [Java开发环境搭建](backend/easy/dev_environment_setup.md)
  - [Node.js RESTful API实现](backend/easy/node_rest_api.md)
  - [Python Flask Web应用](backend/easy/python_flask_web.md)
  - [Go语言HTTP服务器](backend/easy/go_http_server.md)
  - [Java Servlet Web应用](backend/easy/java_servlet_app.md)
  - [C# ASP.NET MVC应用](backend/easy/csharp_aspnet_mvc.md)
  - [PHP Laravel CRUD应用](backend/easy/php_laravel_crud.md)
  - [Ruby on Rails博客应用](backend/easy/ruby_rails_blog.md)
  - [Python FastAPI服务](backend/easy/python_fastapi.md)
  - [Rust Actix Web API](backend/easy/rust_actix_api.md)
  - [Kotlin Spring Boot应用](backend/easy/kotlin_spring_boot.md)
- **中难度**：
  - [设计模式应用](backend/medium/design_patterns.md)
  - [Spring Cloud微服务架构实现](backend/medium/spring_cloud_microservices.md)
  - [Node.js GraphQL API实现](backend/medium/node_graphql_api.md)
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