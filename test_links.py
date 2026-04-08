#!/usr/bin/env python3
"""
链接验证测试脚本

验证转换后的 Markdown 链接有效性，确保：
- 所有链接指向的文件存在
- 相对路径计算正确
- 无断裂链接
- 跨平台兼容性

功能：
- 扫描所有 Markdown 文件
- 提取标准 Markdown 链接
- 验证链接目标文件存在
- 生成详细的验证报告
"""
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Set
from urllib.parse import urlparse


# ==================== 配置 ====================

BASE_DIR = Path(__file__).parent
WIKI_DIR = BASE_DIR / "wiki"


# ==================== 数据类 ====================

class MarkdownLink:
    """标准 Markdown 链接"""
    def __init__(self, raw_text: str, display_text: str, target_path: str, 
                 line_number: int, source_file: Path):
        self.raw_text = raw_text
        self.display_text = display_text
        self.target_path = target_path
        self.line_number = line_number
        self.source_file = source_file
        self.target_file = None  # 解析后的目标文件路径
        self.is_valid = False
        self.error_message = ""
    
    def __repr__(self) -> str:
        return f"MarkdownLink({self.display_text} -> {self.target_path})"


# ==================== 链接提取器 ====================

class MarkdownLinkExtractor:
    """提取标准 Markdown 链接"""
    
    # 匹配 [text](path) 格式，排除 http/https 链接
    PATTERN = r'\[([^\]]+)\]\(([^)]+)\)'
    
    @staticmethod
    def extract_links(content: str, source_file: Path) -> List[MarkdownLink]:
        """
        从 Markdown 内容中提取所有标准链接
        
        Args:
            content: Markdown 文件内容
            source_file: 源文件路径
            
        Returns:
            MarkdownLink 对象列表
        """
        links = []
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, start=1):
            for match in re.finditer(MarkdownLinkExtractor.PATTERN, line):
                raw_text = match.group(0)
                display_text = match.group(1)
                target_path = match.group(2)
                
                # 跳过外部链接（http/https）
                if target_path.startswith('http://') or target_path.startswith('https://'):
                    continue
                
                # 跳过锚点链接
                if target_path.startswith('#'):
                    continue
                
                link = MarkdownLink(
                    raw_text=raw_text,
                    display_text=display_text,
                    target_path=target_path,
                    line_number=line_num,
                    source_file=source_file
                )
                links.append(link)
        
        return links


# ==================== 链接验证器 ====================

class LinkValidator:
    """验证链接有效性"""
    
    def __init__(self):
        self.stats = {
            'total_files': 0,
            'total_links': 0,
            'valid_links': 0,
            'broken_links': 0,
            'warnings': 0
        }
        self.broken_links_list: List[MarkdownLink] = []
        self.warnings_list: List[str] = []
    
    def validate_link(self, link: MarkdownLink) -> bool:
        """
        验证单个链接是否有效
        
        Args:
            link: Markdown 链接对象
            
        Returns:
            是否有效
        """
        try:
            # 解析目标路径
            if link.target_path.startswith('./') or link.target_path.startswith('../'):
                # 相对路径
                target_file = (link.source_file.parent / link.target_path).resolve()
            else:
                # 相对于当前目录
                target_file = (link.source_file.parent / link.target_path).resolve()
            
            link.target_file = target_file
            
            # 检查文件是否存在
            if not target_file.exists():
                link.is_valid = False
                link.error_message = f"Target file not found: {target_file}"
                return False
            
            # 检查是否为 Markdown 文件
            if target_file.suffix != '.md':
                link.is_valid = False
                link.error_message = f"Target is not a Markdown file: {target_file}"
                return False
            
            link.is_valid = True
            return True
            
        except Exception as e:
            link.is_valid = False
            link.error_message = f"Path resolution error: {e}"
            return False
    
    def validate_file(self, file_path: Path) -> Tuple[List[MarkdownLink], List[str]]:
        """
        验证单个文件中的所有链接
        
        Args:
            file_path: 文件路径
            
        Returns:
            (链接列表, 错误消息列表)
        """
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            return [], [f"Failed to read {file_path}: {e}"]
        
        # 提取链接
        links = MarkdownLinkExtractor.extract_links(content, file_path)
        
        if not links:
            return [], []
        
        # 验证每个链接
        errors = []
        for link in links:
            if not self.validate_link(link):
                errors.append(f"Line {link.line_number}: {link.error_message}")
                self.broken_links_list.append(link)
        
        return links, errors
    
    def validate_all(self, files: List[Path]) -> Dict:
        """
        验证所有文件
        
        Args:
            files: 文件路径列表
            
        Returns:
            统计信息字典
        """
        print("\n" + "=" * 60)
        print("VALIDATION IN PROGRESS")
        print("=" * 60)
        
        self.stats['total_files'] = len(files)
        
        for i, file_path in enumerate(files, 1):
            relative_path = file_path.relative_to(BASE_DIR)
            
            # 验证文件
            links, errors = self.validate_file(file_path)
            
            # 更新统计
            if links:
                self.stats['total_links'] += len(links)
                valid_count = sum(1 for link in links if link.is_valid)
                self.stats['valid_links'] += valid_count
                broken_count = len(links) - valid_count
                self.stats['broken_links'] += broken_count
                
                # 打印进度
                if broken_count > 0:
                    print(f"[BROKEN] [{i}/{len(files)}] {relative_path} ({broken_count} broken links)")
                else:
                    print(f"[OK] [{i}/{len(files)}] {relative_path} ({valid_count} links)")
            
            # 记录错误
            if errors:
                self.warnings_list.extend(errors)
                self.stats['warnings'] += len(errors)
        
        return self.stats
    
    def print_report(self):
        """打印验证报告"""
        print("\n" + "=" * 60)
        print("VALIDATION REPORT")
        print("=" * 60)
        print(f"Total files scanned:     {self.stats['total_files']}")
        print(f"Total links found:       {self.stats['total_links']}")
        print(f"Valid links:             {self.stats['valid_links']}")
        print(f"Broken links:            {self.stats['broken_links']}")
        print(f"Warnings:                {self.stats['warnings']}")
        
        # 打印断裂链接详情
        if self.broken_links_list:
            print("\n" + "-" * 60)
            print("BROKEN LINKS DETAILS")
            print("-" * 60)
            
            for link in self.broken_links_list:
                source_rel = link.source_file.relative_to(BASE_DIR)
                print(f"\nFile: {source_rel}")
                print(f"  Line {link.line_number}: [{link.display_text}]({link.target_path})")
                print(f"  Error: {link.error_message}")
        
        # 打印警告
        if self.warnings_list:
            print("\n" + "-" * 60)
            print("WARNINGS")
            print("-" * 60)
            for warning in self.warnings_list[:10]:  # 只显示前10条
                print(f"  {warning}")
            
            if len(self.warnings_list) > 10:
                print(f"  ... and {len(self.warnings_list) - 10} more warnings")
        
        # 总结
        print("\n" + "=" * 60)
        if self.stats['broken_links'] == 0:
            print("✓ ALL LINKS VALID")
            print("All Markdown links are valid and target files exist.")
        else:
            print("✗ BROKEN LINKS FOUND")
            print(f"Found {self.stats['broken_links']} broken links that need to be fixed.")
        print("=" * 60)


# ==================== 辅助功能 ====================

def check_for_remaining_obsidian_links(files: List[Path]) -> int:
    """
    检查是否还有剩余的 Obsidian 链接
    
    Args:
        files: 文件路径列表
        
    Returns:
        剩余的 Obsidian 链接数量
    """
    obsidian_pattern = r'\[\[([^\]]+)\]\]'
    total_count = 0
    
    print("\n" + "=" * 60)
    print("CHECKING FOR REMAINING OBSIDIAN LINKS")
    print("=" * 60)
    
    for file_path in files:
        try:
            content = file_path.read_text(encoding='utf-8')
            matches = re.findall(obsidian_pattern, content)
            
            if matches:
                relative_path = file_path.relative_to(BASE_DIR)
                print(f"[FOUND] {relative_path}: {len(matches)} Obsidian links")
                total_count += len(matches)
        except Exception:
            pass
    
    if total_count == 0:
        print("[OK] No Obsidian links found. Conversion complete.")
    else:
        print(f"\n[WARNING] Found {total_count} remaining Obsidian links.")
        print("Run convert_links.py again to convert them.")
    
    return total_count


def scan_wiki_directory() -> List[Path]:
    """扫描 wiki 目录"""
    if not WIKI_DIR.exists():
        print(f"[ERROR] Wiki directory not found: {WIKI_DIR}")
        return []
    
    md_files = list(WIKI_DIR.rglob("*.md"))
    print(f"[INFO] Found {len(md_files)} Markdown files in wiki/")
    return md_files


# ==================== 主函数 ====================

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Validate Markdown links after conversion'
    )
    parser.add_argument(
        '--check-obsidian',
        action='store_true',
        help='Also check for remaining Obsidian links'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed output'
    )
    
    args = parser.parse_args()
    
    # 打印欢迎信息
    print("=" * 60)
    print("MARKDOWN LINK VALIDATOR")
    print("=" * 60)
    print(f"Wiki directory: {WIKI_DIR}")
    
    # 扫描文件
    files = scan_wiki_directory()
    
    if not files:
        print("[ERROR] No Markdown files found")
        sys.exit(1)
    
    # 验证链接
    validator = LinkValidator()
    validator.validate_all(files)
    validator.print_report()
    
    # 检查剩余的 Obsidian 链接
    if args.check_obsidian:
        remaining = check_for_remaining_obsidian_links(files)
        if remaining > 0:
            sys.exit(1)
    
    # 退出码
    if validator.stats['broken_links'] > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
