"""
提取2013-2025年巴菲特致股东信PDF文本
"""
import os
from PyPDF2 import PdfReader

# 设置路径
pdf_dir = r"d:\codebuddySpace\Buffett'sLetter\raw\books\pdf"
output_dir = r"d:\codebuddySpace\Buffett'sLetter\temp\pdf_text"

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 处理2013-2025年的PDF
years = range(2013, 2026)

for year in years:
    pdf_file = os.path.join(pdf_dir, f"{year}_buffett_letter.pdf")
    txt_file = os.path.join(output_dir, f"{year}_buffett_letter.txt")
    
    if not os.path.exists(pdf_file):
        print(f"[ERROR] PDF file not found: {pdf_file}")
        continue
    
    try:
        # 读取PDF
        reader = PdfReader(pdf_file)
        num_pages = len(reader.pages)
        
        # 提取文本
        text_content = []
        for i, page in enumerate(reader.pages):
            text_content.append(f"\n--- Page {i+1} ---\n")
            text_content.append(page.extract_text())
        
        # 保存文本
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(''.join(text_content))
        
        print(f"[OK] {year}: Extracted {num_pages} pages")
    except Exception as e:
        print(f"[ERROR] {year}: Extraction failed - {e}")

print("\nDone!")
