# 基础单元测试编写

## 描述
为给定的函数库编写完整的单元测试，确保代码的正确性和可靠性。

## 要求
1. 使用Jest测试框架编写单元测试
2. 为以下函数编写测试用例：
   - 字符串处理函数
   - 数学计算函数
   - 数据验证函数
3. 测试覆盖率要达到90%以上
4. 包含正常情况和边界情况的测试

## 输入
以下是需要测试的函数库：

```javascript
// stringUtils.js
function capitalize(str) {
  if (typeof str !== 'string') return '';
  return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

function reverse(str) {
  if (typeof str !== 'string') return '';
  return str.split('').reverse().join('');
}

function countOccurrences(str, char) {
  if (typeof str !== 'string' || typeof char !== 'string' || char.length !== 1) return 0;
  return str.split(char).length - 1;
}

// mathUtils.js
function add(a, b) {
  return Number(a) + Number(b);
}

function multiply(a, b) {
  return Number(a) * Number(b);
}

function factorial(n) {
  if (n < 0) return null;
  if (n === 0 || n === 1) return 1;
  return n * factorial(n - 1);
}

// validationUtils.js
function isValidEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

function isValidPassword(password) {
  // At least 8 chars, 1 uppercase, 1 lowercase, 1 number
  const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;
  return regex.test(password);
}

function isValidPhoneNumber(phone) {
  const regex = /^\d{10}$/;
  return regex.test(phone);
}
```

## 期望输出
1. 完整的测试文件，包含所有函数的测试用例
2. 测试覆盖率报告
3. 测试运行命令

## 评估标准
1. 测试用例的完整性和覆盖率
2. 边界情况的处理
3. 测试代码的可读性和组织
4. 测试断言的准确性