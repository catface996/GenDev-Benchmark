# GitHub Actions基础配置

## 描述

本案例要求为一个简单的Web应用配置基础的GitHub Actions工作流，实现代码提交后的自动构建和测试。

## 要求

1. 为一个Node.js Web应用创建GitHub Actions工作流配置
2. 工作流需要在每次推送到main分支和创建Pull Request时触发
3. 工作流需要包含以下步骤:
   - 检出代码
   - 设置Node.js环境
   - 安装依赖
   - 运行代码检查(lint)
   - 运行单元测试
   - 构建应用
4. 缓存npm依赖以加速构建
5. 在工作流完成后通知团队成员

## 输入

一个简单的Node.js Web应用，使用以下技术栈:
- Node.js 16
- npm作为包管理器
- ESLint用于代码检查
- Jest用于单元测试
- 使用npm scripts定义的命令:
  - `npm run lint`: 运行代码检查
  - `npm test`: 运行单元测试
  - `npm run build`: 构建应用

## 预期输出

1. 完整的GitHub Actions工作流配置文件(`.github/workflows/ci.yml`)
2. 简要的说明文档，解释工作流的各个部分和如何进行自定义

## 评估标准

1. **配置正确性**: GitHub Actions配置是否正确
2. **完整性**: 是否实现了所有要求的步骤
3. **效率**: 是否使用了缓存等优化手段
4. **可读性**: 工作流配置是否清晰易懂
5. **可维护性**: 配置是否易于维护和扩展
6. **文档质量**: 说明文档是否清晰完整

## 难度

低

## 技能点

- GitHub Actions基础
- CI/CD基本概念
- YAML配置
- Node.js构建流程
- 自动化测试