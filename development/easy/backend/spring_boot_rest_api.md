# Spring Boot RESTful API实现

## 描述
使用Spring Boot框架实现一个简单的RESTful API，提供基本的CRUD操作。

## 要求
1. 创建一个Spring Boot应用
2. 实现一个简单的实体类（如Product）
3. 创建对应的Repository接口
4. 实现RESTful API，支持以下操作：
   - GET /products：获取所有产品
   - GET /products/{id}：获取单个产品
   - POST /products：创建新产品
   - PUT /products/{id}：更新产品
   - DELETE /products/{id}：删除产品
5. 添加基本的输入验证
6. 实现适当的错误处理

## 输入
无特定输入，需要从头创建一个新的Spring Boot项目。

## 期望输出
1. 完整的项目结构，包括实体类、Repository、Controller等
2. 所有API端点的实现
3. 输入验证和错误处理逻辑
4. 应用配置文件

## 评估标准
1. API设计的RESTful合规性
2. 代码结构和组织
3. 输入验证的完整性
4. 错误处理的合理性
5. 代码可读性和注释