# CI/CD流水线配置

## 描述
为一个基于Git的项目配置完整的CI/CD流水线，实现代码提交后的自动构建、测试和部署。

## 要求
1. 使用GitHub Actions配置CI/CD流水线
2. 实现以下阶段：
   - 代码检查（linting）
   - 单元测试
   - 构建Docker镜像
   - 推送镜像到Docker Registry
   - 部署到测试环境
3. 配置不同分支的不同行为：
   - `main`分支：完整流程直到生产部署
   - `develop`分支：完整流程直到测试环境部署
   - 其他分支：只进行代码检查和单元测试

## 输入
项目结构如下：
```
project/
├── src/
│   └── app.js
├── tests/
│   └── app.test.js
├── Dockerfile
└── package.json
```

## 期望输出
1. 完整的GitHub Actions工作流配置文件（`.github/workflows/ci-cd.yml`）
2. 必要的环境变量和密钥配置说明
3. 部署脚本（如果需要）

## 评估标准
1. 工作流配置的正确性和完整性
2. 分支策略实现的准确性
3. 安全实践（如密钥处理）
4. 流水线效率和可维护性