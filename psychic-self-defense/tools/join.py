"""抽出テキストからページ区切りとページ番号行を除き、段落に繋ぐ。"""
import re, pathlib
D = pathlib.Path(__file__).parent.parent
raw = (D / "src/psd.txt").read_text(encoding="utf-8")
lines = []
for l in raw.splitlines():
    s = l.strip()
    if re.fullmatch(r"=====\[p\d+\]=====", s) or re.fullmatch(r"\d+ of 103", s) or not s:
        continue
    lines.append(s)
paras, cur = [], ""
for s in lines:
    cur = (cur + " " + s) if cur else s
    if cur.endswith("-") and not cur.endswith("--"):
        pass
    if len(s) < 48 and re.search(r"[.?!:\"'”’)]$", s):
        paras.append(cur); cur = ""
    elif re.fullmatch(r"[A-Z0-9 .,'\-:;()]+", s) and len(s) < 70:
        paras.append(cur); cur = ""
if cur: paras.append(cur)
(D / "src/psd_join.txt").write_text("\n\n".join(paras), encoding="utf-8")
print(len(paras))
