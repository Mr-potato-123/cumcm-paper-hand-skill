# -*- coding: utf-8 -*-
"""OCR 图片型 PDF → Markdown,供 AI Agent 通读 ref 论文。
用法:python _tools/ocr_pdfs.py
输出:ref/<name>.md(含页标记与说明头)
"""
import os
import sys
import time
import fitz
from rapidocr_onnxruntime import RapidOCR

REF_DIR = os.path.join(os.path.dirname(__file__), '..', 'ref')
HEADER_TMPL = """---
source: {pdf}
note: 本文档由 OCR 自动识别生成,仅供 AI Agent 通读参考;公式、表格、图片可能存在识别误差,关键信息请对照原 PDF。
---

"""


def ocr_pdf(pdf_path, md_path):
    doc = fitz.open(pdf_path)
    total = len(doc)
    parts = [HEADER_TMPL.format(pdf=os.path.basename(pdf_path))]
    for i in range(total):
        pix = doc[i].get_pixmap(dpi=200)
        png = f'_page_{i}.png'
        pix.save(png)
        res, _ = OCR(png)
        os.remove(png)
        text = '\n'.join(line[1] for line in res) if res else '(本页为纯图表页,无文字)'
        parts.append(f'\n<!-- ==== 第 {i+1} 页 / 共 {total} 页 ==== -->\n\n{text}\n')
        print(f'[{os.path.basename(pdf_path)}] page {i+1}/{total}', flush=True)
    doc.close()
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(''.join(parts))
    print(f'done: {md_path}', flush=True)


if __name__ == '__main__':
    OCR = RapidOCR()
    targets = sys.argv[1:] if len(sys.argv) > 1 else None
    pdfs = [f for f in sorted(os.listdir(REF_DIR)) if f.lower().endswith('.pdf')]
    if targets:
        pdfs = [f for f in pdfs if f in targets]
    for pdf in pdfs:
        md = os.path.join(REF_DIR, pdf[:-4] + '.md')
        if os.path.exists(md):
            print(f'skip(已存在): {md}', flush=True)
            continue
        ocr_pdf(os.path.join(REF_DIR, pdf), md)
        time.sleep(1)
    print('ALL DONE', flush=True)
