# 简单Docker容器部署

## 描述
创建一个Docker容器，用于部署一个简单的Web应用。

## 要求
1. 创建一个Dockerfile，基于官方的Node.js镜像
2. 将一个简单的Express应用打包到容器中
3. 配置容器在8080端口暴露服务
4. 提供构建和运行容器的命令

## 输入
提供一个简单的Express应用代码：
```javascript
const express = require('express');
const app = express();
const port = 8080;

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
```

## 期望输出
1. 完整的Dockerfile
2. 构建镜像的命令
3. 运行容器的命令

## 评估标准
1. Dockerfile的正确性和最佳实践
2. 构建和运行命令的准确性
3. 容器配置的安全性和效率