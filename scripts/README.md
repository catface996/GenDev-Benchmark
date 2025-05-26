# 脚本工具

此目录包含用于维护和管理GenDev-Benchmark项目的实用脚本。

## 可用脚本

### update_readme.py

自动扫描项目目录结构并更新根目录的README.md文件，生成目录树和导航链接。

**用法:**
```bash
cd /path/to/GenDev-Benchmark
python3 scripts/update_readme.py
```

### check_links.py

检查所有md文件是否在README.md中有对应的链接，并验证README.md中的链接是否都指向存在的文件。

**用法:**
```bash
cd /path/to/GenDev-Benchmark
python3 scripts/check_links.py
```

## 注意事项

- 这些脚本应在项目根目录下运行
- 脚本需要Python 3环境
- 脚本会自动处理相对路径