#!/usr/bin/env python3
"""
检查所有md文件是否在README.md中有对应的链接
"""

import os
import re

def find_all_md_files(root_dir):
    """查找所有md文件"""
    md_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md') and file != 'README.md':
                rel_path = os.path.join(root, file).replace(root_dir, '').lstrip('/')
                md_files.append(rel_path)
    return md_files

def extract_links_from_readme(readme_path):
    """从README.md中提取所有链接"""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 使用正则表达式提取所有Markdown链接
    links = re.findall(r'\[.*?\]\((.*?\.md)\)', content)
    return links

def main():
    # 获取脚本所在目录的上一级目录（项目根目录）
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme_path = os.path.join(root_dir, 'README.md')
    
    # 查找所有md文件
    all_md_files = find_all_md_files(root_dir)
    print(f"找到 {len(all_md_files)} 个md文件")
    
    # 从README.md中提取所有链接
    readme_links = extract_links_from_readme(readme_path)
    print(f"README.md中有 {len(readme_links)} 个链接")
    
    # 检查每个md文件是否有对应的链接
    missing_links = []
    for md_file in all_md_files:
        if md_file not in readme_links:
            missing_links.append(md_file)
    
    # 检查README.md中的链接是否都指向存在的文件
    broken_links = []
    for link in readme_links:
        if not os.path.exists(os.path.join(root_dir, link)):
            broken_links.append(link)
    
    # 输出结果
    if missing_links:
        print("\n以下md文件在README.md中没有对应的链接:")
        for file in missing_links:
            print(f"  - {file}")
    else:
        print("\n所有md文件在README.md中都有对应的链接")
    
    if broken_links:
        print("\nREADME.md中以下链接指向不存在的文件:")
        for link in broken_links:
            print(f"  - {link}")
    else:
        print("\nREADME.md中所有链接都指向存在的文件")

if __name__ == "__main__":
    main()