# JavaScript表单验证

## 描述
使用原生JavaScript实现客户端表单验证功能，确保用户输入的数据符合要求。

## 要求
1. 使用原生JavaScript（不使用jQuery或其他库）
2. 为以下表单字段实现验证：
   - 用户名（字母和数字，长度限制）
   - 电子邮件（有效的电子邮件格式）
   - 密码（包含大小写字母、数字和特殊字符，最小长度要求）
   - 确认密码（与密码匹配）
   - 电话号码（特定格式）
   - 出生日期（年龄限制）
3. 实现实时验证（在用户输入时）和提交验证
4. 显示适当的错误消息
5. 使用正则表达式进行模式匹配
6. 实现表单提交前的最终验证

## 输入
HTML表单结构：
```html
<form id="registrationForm">
  <div class="form-group">
    <label for="username">用户名</label>
    <input type="text" id="username" name="username">
    <div class="error" id="username-error"></div>
  </div>
  
  <div class="form-group">
    <label for="email">电子邮件</label>
    <input type="email" id="email" name="email">
    <div class="error" id="email-error"></div>
  </div>
  
  <div class="form-group">
    <label for="password">密码</label>
    <input type="password" id="password" name="password">
    <div class="error" id="password-error"></div>
  </div>
  
  <div class="form-group">
    <label for="confirm-password">确认密码</label>
    <input type="password" id="confirm-password" name="confirmPassword">
    <div class="error" id="confirm-password-error"></div>
  </div>
  
  <div class="form-group">
    <label for="phone">电话号码</label>
    <input type="tel" id="phone" name="phone">
    <div class="error" id="phone-error"></div>
  </div>
  
  <div class="form-group">
    <label for="birthdate">出生日期</label>
    <input type="date" id="birthdate" name="birthdate">
    <div class="error" id="birthdate-error"></div>
  </div>
  
  <button type="submit">注册</button>
</form>
```

## 期望输出
1. 完整的JavaScript验证代码
2. 适当的错误处理和用户反馈
3. 验证规则的说明文档

## 评估标准
1. JavaScript语法和DOM操作的正确性
2. 验证逻辑的完整性和准确性
3. 代码组织和结构
4. 错误消息的清晰性和用户友好性
5. 性能考虑（如防抖动）
6. 代码可读性和注释