# Kubernetes基础部署与配置

## 描述

本案例要求实现一个基于Kubernetes的应用部署方案，包括创建必要的Deployment、Service、ConfigMap和Secret资源，以及配置基本的资源限制和健康检查。

## 要求

1. 创建一个包含前端和后端两个微服务的Kubernetes部署方案
2. 前端服务需要暴露给外部访问，后端服务只允许集群内部访问
3. 使用ConfigMap存储应用配置
4. 使用Secret存储敏感信息（如数据库密码）
5. 为每个服务配置资源请求和限制
6. 实现存活探针(liveness probe)和就绪探针(readiness probe)
7. 配置水平自动扩展(HorizontalPodAutoscaler)
8. 编写部署脚本，实现一键部署

## 输入

- 前端镜像: `frontend:v1.0`
- 后端镜像: `backend:v1.0`
- 前端需要环境变量: `API_URL`, `NODE_ENV`
- 后端需要环境变量: `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `LOG_LEVEL`
- 前端服务需要暴露80端口
- 后端服务运行在8080端口

## 预期输出

1. 完整的Kubernetes YAML配置文件，包括:
   - Deployment配置
   - Service配置
   - ConfigMap配置
   - Secret配置
   - HorizontalPodAutoscaler配置
2. 部署脚本
3. 简要的部署文档

## 评估标准

1. **配置正确性**: Kubernetes资源定义是否正确
2. **安全性**: Secret的使用是否恰当，权限设置是否合理
3. **可靠性**: 健康检查配置是否合理
4. **可扩展性**: 自动扩展配置是否合理
5. **可维护性**: 配置文件结构和命名是否清晰
6. **文档质量**: 部署文档是否清晰完整

## 难度

中等

## 技能点

- Kubernetes基础概念
- Kubernetes资源配置
- 容器编排
- 应用配置管理
- 敏感信息管理
- 自动扩展
- 健康检查