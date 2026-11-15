"""Gutenberg テキストを整形し、段落ごとに番号を振って chunk ファイルに分ける。"""
import pathlib, re, sys
t = pathlib.Path("src/pg71985.txt").read_text(encoding="utf-8")
body = t.split(" PSYCHE’S TASK\n\n{3}", 1)[1].split("\n INDEX\n", 1)[0]
body = re.sub(r"\{[0-9ivx]+\}", "", body)
paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", body)]
paras = [p for p in paras if p]
out = pathlib.Path("src/paras.txt")
out.write_text("\n\n".join(f"<{i}> {p}" for i, p in enumerate(paras)), encoding="utf-8")
print(len(paras), sum(len(p.split()) for p in paras))
