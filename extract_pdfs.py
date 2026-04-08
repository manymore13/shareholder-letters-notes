#!/usr/bin/env python3
"""
批量提取巴菲特致股东信PDF文本
"""
import pdfplumber
import os
from pathlib import Path

# PDF目录
pdf_dir = Path("d:/codebuddySpace/Buffett'sLetter/raw/books/pdf")
output_dir = Path("d:/codebuddySpace/Buffett'sLetter/temp/pdf_text")

# 创建输出目录
output_dir.mkdir(parents=True, exist_ok=True)

# 要处理的年份（第3批次：2003-2012）
years = range(2003, 2013)

for year in years:
    pdf_file = pdf_dir / f"{year}_buffett_letter.pdf"
    output_file = output_dir / f"{year}_buffett_letter.txt"
    
    if not pdf_file.exists():
        print(f"PDF文件不存在：{pdf_file}")
        continue
    
    if output_file.exists():
        print(f"已存在，跳过：{output_file}")
        continue
    
    print(f"处理：{pdf_file.name}")
    
    try:
        text_content = []
        with pdfplumber.open(pdf_file) as pdf:
            print(f"  页数：{len(pdf.pages)}")
            
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    text_content.append(f"\n--- Page {i+1} ---\n{text}\n")
        
        # 保存文本
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(text_content))
        
        print(f"  已保存：{output_file.name}")
        
    except Exception as e:
        print(f"  错误：{e}")

print("\n处理完成！")
print(f"提取的文本保存在：{output_dir}")
