from pypdf import PdfReader
import sys

pdf_path = r"d:\codebuddySpace\Buffett'sLetter\raw\books\pdf\2002pdf.pdf"
reader = PdfReader(pdf_path)

print(f"Total pages: {len(reader.pages)}")

text = ""
for i, page in enumerate(reader.pages[:15]):  # 前15页
    page_text = page.extract_text()
    if page_text:
        text += f"\n--- Page {i+1} ---\n"
        text += page_text

# 保存到文件
with open(r"d:\codebuddySpace\Buffett'sLetter\temp\pdf_content.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("PDF内容已保存到 temp/pdf_content.txt")
print(f"Total characters: {len(text)}")
