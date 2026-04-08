#!/usr/bin/env python3
"""
Obsidian 链接转换脚本

将所有 Obsidian 格式的双向链接 [[link]] 转换为标准 Markdown 链接 [text](path.md)
确保在 GitHub、VSCode、Typora 等所有平台正常工作。

功能：
- 扫描 wiki/ 目录下所有 Markdown 文件
- 解析 Obsidian 链接格式
- 计算正确的相对路径
- 批量转换并生成报告
"""
import sys
from pathlib import Path
from typing import List, Dict, Tuple
from datetime import datetime

# 导入工具模块
from link_utils import (
    LinkParser, 
    PathCalculator, 
    LinkConverter, 
    safe_read_file, 
    safe_write_file,
    count_obsidian_links
)


# ==================== 配置 ====================

BASE_DIR = Path(__file__).parent
WIKI_DIR = BASE_DIR / "wiki"
BACKUP_DIR = BASE_DIR / ".backup"


# ==================== 扫描器 ====================

class WikiScanner:
    """扫描 wiki 目录下的所有 Markdown 文件"""
    
    @staticmethod
    def scan_all_markdown_files() -> List[Path]:
        """
        扫描 wiki/ 目录下所有 .md 文件
        
        Returns:
            Markdown 文件路径列表
        """
        if not WIKI_DIR.exists():
            print(f"[ERROR] Wiki directory not found: {WIKI_DIR}")
            return []
        
        md_files = list(WIKI_DIR.rglob("*.md"))
        print(f"[INFO] Found {len(md_files)} Markdown files in wiki/")
        return md_files
    
    @staticmethod
    def categorize_files(files: List[Path]) -> Dict[str, List[Path]]:
        """
        按目录分类文件
        
        Args:
            files: 文件路径列表
            
        Returns:
            分类字典 {category: [files]}
        """
        categories = {
            'root': [],
            'entities': [],
            'concepts': [],
            'sources': []
        }
        
        for file_path in files:
            if file_path.parent.name == 'wiki':
                categories['root'].append(file_path)
            elif file_path.parent.name == 'entities':
                categories['entities'].append(file_path)
            elif file_path.parent.name == 'concepts':
                categories['concepts'].append(file_path)
            elif file_path.parent.name == 'sources':
                categories['sources'].append(file_path)
            else:
                categories['root'].append(file_path)
        
        return categories


# ==================== 转换器 ====================

class BatchConverter:
    """批量转换器"""
    
    def __init__(self, dry_run: bool = False):
        """
        初始化批量转换器
        
        Args:
            dry_run: 是否为预览模式（不实际修改文件）
        """
        self.dry_run = dry_run
        self.stats = {
            'total_files': 0,
            'files_with_links': 0,
            'total_links': 0,
            'converted_links': 0,
            'errors': []
        }
    
    def convert_file(self, file_path: Path) -> Tuple[bool, int, List[str]]:
        """
        转换单个文件
        
        Args:
            file_path: 文件路径
            
        Returns:
            (是否成功, 转换的链接数量, 错误消息列表)
        """
        # 读取文件
        content = safe_read_file(file_path)
        if content is None:
            return False, 0, [f"Failed to read file: {file_path}"]
        
        # 检查是否包含 Obsidian 链接
        if not LinkParser.has_obsidian_links(content):
            return True, 0, []
        
        # 转换链接
        new_content, converted_links, errors = LinkConverter.convert_content(content, file_path)
        
        if not converted_links:
            return True, 0, errors
        
        # 写入文件（如果不是预览模式）
        if not self.dry_run:
            if not safe_write_file(file_path, new_content):
                return False, 0, [f"Failed to write file: {file_path}"]
        
        return True, len(converted_links), errors
    
    def convert_all(self, files: List[Path]) -> Dict:
        """
        批量转换所有文件
        
        Args:
            files: 文件路径列表
            
        Returns:
            统计信息字典
        """
        print(f"\n{'[DRY RUN] ' if self.dry_run else ''}Starting conversion...")
        print("=" * 60)
        
        self.stats['total_files'] = len(files)
        
        for i, file_path in enumerate(files, 1):
            relative_path = file_path.relative_to(BASE_DIR)
            
            # 转换文件
            success, link_count, errors = self.convert_file(file_path)
            
            # 更新统计
            if link_count > 0:
                self.stats['files_with_links'] += 1
                self.stats['total_links'] += link_count
                
                if success:
                    self.stats['converted_links'] += link_count
                    status = "[OK]"
                else:
                    status = "[ERROR]"
                
                print(f"{status} [{i}/{len(files)}] {relative_path} ({link_count} links)")
            else:
                # 无链接的文件，静默处理
                pass
            
            # 记录错误
            if errors:
                self.stats['errors'].extend(errors)
                for error in errors:
                    print(f"  {error}")
        
        return self.stats
    
    def print_report(self):
        """打印转换报告"""
        print("\n" + "=" * 60)
        print("CONVERSION REPORT")
        print("=" * 60)
        print(f"Total files scanned:     {self.stats['total_files']}")
        print(f"Files with links:        {self.stats['files_with_links']}")
        print(f"Total links found:       {self.stats['total_links']}")
        print(f"Links converted:         {self.stats['converted_links']}")
        print(f"Errors:                  {len(self.stats['errors'])}")
        
        if self.dry_run:
            print("\n[DRY RUN] No files were modified.")
        else:
            print("\n[COMPLETED] All files have been converted.")


# ==================== 备份 ====================

def create_backup():
    """创建 Git 提交备份"""
    import subprocess
    
    try:
        # 检查是否有未提交的更改
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            cwd=BASE_DIR,
            capture_output=True,
            text=True
        )
        
        if result.stdout.strip():
            # 有更改，创建提交
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            commit_message = f"Backup before link conversion - {timestamp}"
            
            subprocess.run(['git', 'add', '.'], cwd=BASE_DIR, check=True)
            subprocess.run(['git', 'commit', '-m', commit_message], cwd=BASE_DIR, check=True)
            
            print(f"[INFO] Created backup commit: {commit_message}")
        else:
            print("[INFO] No changes to backup")
            
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to create backup: {e}")
        return False
    except FileNotFoundError:
        print("[WARNING] Git not found, skipping backup")
        return True
    
    return True


# ==================== 主函数 ====================

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Convert Obsidian links to standard Markdown links'
    )
    parser.add_argument(
        '--dry-run', 
        action='store_true',
        help='Preview mode - scan and report without modifying files'
    )
    parser.add_argument(
        '--no-backup',
        action='store_true',
        help='Skip creating Git backup before conversion'
    )
    parser.add_argument(
        '--category',
        choices=['all', 'root', 'entities', 'concepts', 'sources'],
        default='all',
        help='Convert only files in specific category'
    )
    
    args = parser.parse_args()
    
    # 打印欢迎信息
    print("=" * 60)
    print("OBSIDIAN LINK TO MARKDOWN CONVERTER")
    print("=" * 60)
    print(f"Mode: {'DRY RUN (Preview)' if args.dry_run else 'CONVERT'}")
    print(f"Category: {args.category}")
    print(f"Wiki directory: {WIKI_DIR}")
    
    # 扫描文件
    scanner = WikiScanner()
    all_files = scanner.scan_all_markdown_files()
    
    if not all_files:
        print("[ERROR] No Markdown files found")
        sys.exit(1)
    
    # 分类文件
    categorized = scanner.categorize_files(all_files)
    
    # 选择要处理的文件
    if args.category == 'all':
        target_files = all_files
    else:
        target_files = categorized.get(args.category, [])
    
    if not target_files:
        print(f"[ERROR] No files in category: {args.category}")
        sys.exit(1)
    
    print(f"[INFO] Processing {len(target_files)} files in category: {args.category}")
    
    # 创建备份（如果不是预览模式）
    if not args.dry_run and not args.no_backup:
        if not create_backup():
            print("[ERROR] Backup failed, aborting conversion")
            sys.exit(1)
    
    # 执行转换
    converter = BatchConverter(dry_run=args.dry_run)
    converter.convert_all(target_files)
    converter.print_report()
    
    # 退出码
    if converter.stats['errors']:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
