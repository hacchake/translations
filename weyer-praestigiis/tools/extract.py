"""PDF の OCR テキストをページごとに src/weyer.txt へ書き出す（[[pNNN]] はPDFのページ番号）。"""
import sys, pathlib, pymupdf
D = pathlib.Path(__file__).parent.parent
d = pymupdf.open(sys.argv[1])
out = []
for i, p in enumerate(d):
    out.append(f"[[p{i:03d}]]\n" + p.get_text())
(D / "src/weyer.txt").write_text("\n".join(out), encoding="utf-8")
print(d.page_count)
