#!/usr/bin/env python3
"""
链接转换工具模块

提供 Obsidian 链接到标准 Markdown 链接的转换功能：
- Link: 链接数据类
- LinkParser: 解析 Obsidian 链接
- PathCalculator: 计算相对路径
- LinkConverter: 转换链接格式
"""
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional, Tuple


# ==================== 数据类 ====================

@dataclass
class Link:
    """表示一个 Obsidian 链接"""
    raw_text: str          # 原始文本 [[link|text]] 或 [[link]]
    link_name: str         # 链接名称（不含 [[ ]]）
    display_text: str      # 显示文本
    line_number: int       # 行号
    start_pos: int         # 起始位置
    end_pos: int           # 结束位置
    
    def __repr__(self) -> str:
        return f"Link({self.link_name}, display='{self.display_text}')"


# ==================== 链接解析器 ====================

class LinkParser:
    """解析 Obsidian 格式的双向链接"""
    
    # 匹配 [[link]] 或 [[link|display text]]
    PATTERN = r'\[\[([^\]]+)\]\]'
    
    @staticmethod
    def extract_links(content: str) -> List[Link]:
        """
        从 Markdown 内容中提取所有 Obsidian 链接
        
        Args:
            content: Markdown 文件内容
            
        Returns:
            Link 对象列表
        """
        links = []
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, start=1):
            for match in re.finditer(LinkParser.PATTERN, line):
                raw_text = match.group(0)
                inner_text = match.group(1)
                
                # 分离链接名称和显示文本
                if '|' in inner_text:
                    link_name, display_text = inner_text.split('|', 1)
                    link_name = link_name.strip()
                    display_text = display_text.strip()
                else:
                    link_name = inner_text.strip()
                    display_text = link_name
                
                link = Link(
                    raw_text=raw_text,
                    link_name=link_name,
                    display_text=display_text,
                    line_number=line_num,
                    start_pos=match.start(),
                    end_pos=match.end()
                )
                links.append(link)
        
        return links
    
    @staticmethod
    def has_obsidian_links(content: str) -> bool:
        """
        检查内容是否包含 Obsidian 链接
        
        Args:
            content: Markdown 文件内容
            
        Returns:
            是否包含 Obsidian 链接
        """
        return bool(re.search(LinkParser.PATTERN, content))


# ==================== 路径计算器 ====================

class PathCalculator:
    """计算从源文件到目标文件的相对路径"""
    
    @staticmethod
    def get_link_type(link_name: str) -> str:
        """
        根据链接名称判断链接类型
        
        Args:
            link_name: 链接名称（如 entity-warren-buffett）
            
        Returns:
            链接类型（entities, concepts, sources 或空字符串）
        """
        if link_name.startswith('entity-'):
            return 'entities'
        elif link_name.startswith('concept-'):
            return 'concepts'
        elif link_name.startswith('source-'):
            return 'sources'
        else:
            return ''
    
    @staticmethod
    def calculate_relative_path(
        source_file: Path, 
        target_link_name: str
    ) -> str:
        """
        计算从源文件到目标链接的相对路径
        
        Args:
            source_file: 源文件路径
            target_link_name: 目标链接名称
            
        Returns:
            相对路径字符串
        """
        # 确定目标文件类型和目录
        link_type = PathCalculator.get_link_type(target_link_name)
        
        if not link_type:
            # 无法识别类型，返回默认路径
            return f"./{target_link_name}.md"
        
        # 构建目标文件的完整路径
        wiki_dir = source_file.parent.parent if source_file.parent.name in ['entities', 'concepts', 'sources'] else source_file.parent
        target_file = wiki_dir / link_type / f"{target_link_name}.md"
        
        # 计算相对路径
        # 直接使用手动计算，更可靠
        return PathCalculator._manual_relative_path(source_file, link_type, target_link_name)
    
    @staticmethod
    def _manual_relative_path(
        source_file: Path, 
        link_type: str, 
        target_link_name: str
    ) -> str:
        """
        手动计算相对路径（回退方案）
        
        Args:
            source_file: 源文件路径
            link_type: 链接类型
            target_link_name: 目标链接名称
            
        Returns:
            相对路径字符串
        """
        source_dir = source_file.parent
        
        # 情况1: 源文件在 wiki 根目录（如 index.md）
        if source_dir.name == 'wiki' or (source_dir.parent.name == '' and source_dir.name != 'entities' and source_dir.name != 'concepts' and source_dir.name != 'sources'):
            return f"./{link_type}/{target_link_name}.md"
        
        # 情况2: 源文件在子目录（entities/concepts/sources）
        if source_dir.name in ['entities', 'concepts', 'sources']:
            if source_dir.name == link_type:
                # 同级目录
                return f"./{target_link_name}.md"
            else:
                # 不同子目录，需要先返回上级
                return f"../{link_type}/{target_link_name}.md"
        
        # 其他情况（保险）
        return f"../{link_type}/{target_link_name}.md"


# ==================== 链接转换器 ====================

class LinkConverter:
    """将 Obsidian 链接转换为标准 Markdown 链接"""
    
    @staticmethod
    def convert_link(link: Link, relative_path: str) -> str:
        """
        将 Obsidian 链接转换为标准 Markdown 链接
        
        Args:
            link: Link 对象
            relative_path: 相对路径
            
        Returns:
            标准 Markdown 链接字符串
        """
        return f"[{link.display_text}]({relative_path})"
    
    @staticmethod
    def convert_content(
        content: str, 
        source_file: Path
    ) -> Tuple[str, List[Link], List[str]]:
        """
        转换文件内容中的所有 Obsidian 链接
        
        Args:
            content: 文件内容
            source_file: 源文件路径
            
        Returns:
            (转换后的内容, 成功转换的链接列表, 错误消息列表)
        """
        links = LinkParser.extract_links(content)
        converted_links = []
        errors = []
        
        if not links:
            return content, converted_links, errors
        
        # 从后往前替换，避免位置偏移
        lines = content.split('\n')
        result_lines = lines.copy()
        
        # 按行号分组
        links_by_line: dict = {}
        for link in links:
            if link.line_number not in links_by_line:
                links_by_line[link.line_number] = []
            links_by_line[link.line_number].append(link)
        
        # 转换每一行的链接
        for line_num in sorted(links_by_line.keys(), reverse=True):
            line_idx = line_num - 1
            original_line = result_lines[line_idx]
            new_line = original_line
            
            # 该行的所有链接（从后往前替换）
            line_links = sorted(links_by_line[line_num], key=lambda l: l.start_pos, reverse=True)
            
            for link in line_links:
                try:
                    # 计算相对路径
                    relative_path = PathCalculator.calculate_relative_path(source_file, link.link_name)
                    
                    # 转换链接
                    markdown_link = LinkConverter.convert_link(link, relative_path)
                    
                    # 替换
                    new_line = new_line[:link.start_pos] + markdown_link + new_line[link.end_pos:]
                    
                    converted_links.append(link)
                    
                except Exception as e:
                    error_msg = f"[ERROR] Line {link.line_number}: Failed to convert '{link.raw_text}' - {e}"
                    errors.append(error_msg)
            
            result_lines[line_idx] = new_line
        
        return '\n'.join(result_lines), converted_links, errors


# ==================== 辅助函数 ====================

def safe_read_file(file_path: Path) -> Optional[str]:
    """
    安全读取文件内容
    
    Args:
        file_path: 文件路径
        
    Returns:
        文件内容，失败返回 None
    """
    try:
        return file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"[ERROR] Failed to read {file_path}: {e}")
        return None


def safe_write_file(file_path: Path, content: str) -> bool:
    """
    安全写入文件内容
    
    Args:
        file_path: 文件路径
        content: 文件内容
        
    Returns:
        是否成功
    """
    try:
        file_path.write_text(content, encoding='utf-8')
        return True
    except Exception as e:
        print(f"[ERROR] Failed to write {file_path}: {e}")
        return False


def count_obsidian_links(content: str) -> int:
    """
    统计内容中 Obsidian 链接的数量
    
    Args:
        content: 文件内容
        
    Returns:
        链接数量
    """
    return len(re.findall(LinkParser.PATTERN, content))


# 导入 os 模块（用于 relpath）
import os
