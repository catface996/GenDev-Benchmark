#!/usr/bin/env python3
"""
脚本用于扫描GenDev-Benchmark目录结构并更新README.md文件中的链接
"""

import os
import re
from collections import defaultdict

def scan_directory(root_dir):
    """扫描目录结构并返回文件树"""
    result = {}
    
    # 主要维度
    dimensions = ['development', 'testing', 'operations']
    
    for dimension in dimensions:
        dimension_path = os.path.join(root_dir, dimension)
        if not os.path.isdir(dimension_path):
            continue
            
        result[dimension] = {}
        
        # 扫描技术领域
        for domain in os.listdir(dimension_path):
            domain_path = os.path.join(dimension_path, domain)
            if not os.path.isdir(domain_path) or domain == '__pycache__' or domain.startswith('.'):
                continue
                
            result[dimension][domain] = {}
            
            # 扫描难度级别
            for level in ['easy', 'medium', 'hard']:
                level_path = os.path.join(domain_path, level)
                if not os.path.isdir(level_path):
                    continue
                    
                result[dimension][domain][level] = []
                
                # 扫描案例文件
                for case_file in os.listdir(level_path):
                    if case_file.endswith('.md') and not case_file.startswith('.'):
                        case_path = os.path.join(level_path, case_file)
                        # 读取文件标题
                        try:
                            with open(case_path, 'r', encoding='utf-8') as f:
                                first_line = f.readline().strip()
                                title = first_line.lstrip('#').strip() if first_line.startswith('#') else os.path.splitext(case_file)[0].replace('_', ' ').title()
                        except:
                            title = os.path.splitext(case_file)[0].replace('_', ' ').title()
                            
                        result[dimension][domain][level].append({
                            'file': case_file,
                            'title': title,
                            'path': os.path.join(dimension, domain, level, case_file)
                        })
    
    return result

def generate_directory_tree(root_dir):
    """生成目录树文本"""
    tree = []
    tree.append("```")
    tree.append("GenDev-Benchmark/")
    tree.append("├── README.md                                 # 项目主文档")
    
    # 主要维度
    dimensions = ['development', 'testing', 'operations']
    
    for i, dimension in enumerate(dimensions):
        is_last_dimension = i == len(dimensions) - 1
        dimension_prefix = "└── " if is_last_dimension else "├── "
        tree.append(f"{dimension_prefix}{dimension}/                              # {dimension.capitalize()}相关案例")
        tree.append(f"{'│   ' if not is_last_dimension else '    '}├── README.md                             # {dimension.capitalize()}维度说明")
        
        dimension_path = os.path.join(root_dir, dimension)
        if not os.path.isdir(dimension_path):
            continue
            
        domains = [d for d in os.listdir(dimension_path) if os.path.isdir(os.path.join(dimension_path, d)) and not d.startswith('.')]
        
        for j, domain in enumerate(domains):
            is_last_domain = j == len(domains) - 1
            domain_prefix = "└── " if is_last_domain else "├── "
            indent = '    ' if is_last_dimension else '│   '
            tree.append(f"{indent}{domain_prefix}{domain}/                            # {domain.capitalize()}案例")
            
            domain_path = os.path.join(dimension_path, domain)
            levels = [l for l in os.listdir(domain_path) if os.path.isdir(os.path.join(domain_path, l)) and l in ['easy', 'medium', 'hard']]
            
            for k, level in enumerate(levels):
                is_last_level = k == len(levels) - 1
                level_prefix = "└── " if is_last_level else "├── "
                level_indent = indent + ('    ' if is_last_domain else '│   ')
                tree.append(f"{level_indent}{level_prefix}{level}/                             # {level.capitalize()}难度{domain}案例")
                
                level_path = os.path.join(domain_path, level)
                cases = [c for c in os.listdir(level_path) if c.endswith('.md')]
                
                if cases:
                    case = cases[0]
                    case_indent = level_indent + ('    ' if is_last_level else '│   ')
                    tree.append(f"{case_indent}└── {case}               # 示例案例")
    
    tree.append("```")
    return "\n".join(tree)

def generate_navigation_links(file_tree):
    """生成导航链接"""
    links = []
    
    # 维度说明文档
    links.append("### 维度说明文档")
    for dimension in ['development', 'testing', 'operations']:
        if dimension in file_tree:
            links.append(f"- [{dimension.capitalize()}维度说明]({dimension}/README.md)")
    
    # 各维度案例
    for dimension, domains in file_tree.items():
        links.append(f"\n### {dimension.capitalize()}维度案例\n")
        
        for domain, levels in domains.items():
            links.append(f"#### {domain.capitalize()}")
            
            for level in ['easy', 'medium', 'hard']:
                if level in levels and levels[level]:
                    links.append(f"- **{level.capitalize()}难度**：")
                    for case in sorted(levels[level], key=lambda x: x['file']):
                        links.append(f"  - [{case['title']}]({case['path']})")
    
    return "\n".join(links)

def update_readme(root_dir):
    """更新README.md文件"""
    readme_path = os.path.join(root_dir, 'README.md')
    
    # 读取现有README内容
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 扫描目录结构
    file_tree = scan_directory(root_dir)
    
    # 生成目录树
    directory_tree = generate_directory_tree(root_dir)
    
    # 生成导航链接
    navigation_links = generate_navigation_links(file_tree)
    
    # 更新目录树部分
    tree_pattern = r"```\nGenDev-Benchmark/.*?```"
    if re.search(tree_pattern, content, re.DOTALL):
        content = re.sub(tree_pattern, directory_tree, content, flags=re.DOTALL)
    else:
        # 如果没有找到目录树部分，添加到文件描述后面
        content = re.sub(r"(本项目从运维、研发和测试三个维度.*?组织案例，帮助评估和比较不同的AI代码生成工具。)\n",
                        r"\1\n\n## 文件目录\n\n" + directory_tree + "\n", content)
    
    # 更新导航链接部分
    nav_pattern = r"## 文档导航\n\n.*?(?=\n##|\Z)"
    if re.search(nav_pattern, content, re.DOTALL):
        content = re.sub(nav_pattern, "## 文档导航\n\n" + navigation_links, content, flags=re.DOTALL)
    else:
        # 如果没有找到导航链接部分，添加到目录树后面
        content += f"\n\n## 文档导航\n\n{navigation_links}\n"
    
    # 写回README.md
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"README.md 已更新")

if __name__ == "__main__":
    # 获取脚本所在目录的上一级目录（项目根目录）
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    update_readme(root_dir)