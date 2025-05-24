# MySQL基础查询优化

## 描述
针对给定的数据库表结构和查询，进行SQL优化以提高查询性能。

## 要求
1. 分析给定的表结构和查询
2. 设计适当的索引
3. 重写查询以提高性能
4. 解释优化思路和预期效果

## 输入
数据库表结构：

```sql
CREATE TABLE customers (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status ENUM('active', 'inactive', 'pending') DEFAULT 'pending'
);

CREATE TABLE orders (
  id INT PRIMARY KEY AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total_amount DECIMAL(10, 2) NOT NULL,
  status ENUM('new', 'processing', 'shipped', 'delivered', 'cancelled') DEFAULT 'new',
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE order_items (
  id INT PRIMARY KEY AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(id)
);

CREATE TABLE products (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock INT NOT NULL DEFAULT 0,
  category VARCHAR(50)
);
```

需要优化的查询：

```sql
SELECT c.name, c.email, COUNT(o.id) as order_count, SUM(o.total_amount) as total_spent
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE c.status = 'active'
AND o.order_date >= '2023-01-01'
GROUP BY c.id, c.name, c.email
HAVING COUNT(o.id) > 0
ORDER BY total_spent DESC;
```

## 期望输出
1. 索引创建语句
2. 优化后的查询
3. 优化思路和解释
4. 预期的性能提升

## 评估标准
1. 索引设计的合理性
2. 查询优化的有效性
3. 解释的清晰度和准确性
4. 对查询执行计划的理解