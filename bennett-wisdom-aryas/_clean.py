"""OCRテキスト(djvu.txt)を段落ごとに整形して src/clean.txt に書き出す。"""
import re, pathlib
D = pathlib.Path(__file__).parent / "src"
lines = (D / "djvu.txt").read_text(encoding="utf-8").split("\n")
start = next(i for i, l in enumerate(lines) if l.strip() == "DEDICATION")
paras, cur = [], []
romans = {"I", "II", "III", "IV", "V", "VI", "VII"}
L = lines[start:]
for k, l in enumerate(L):
    s = re.sub(r"\s+", " ", l).strip()
    if s in romans:
        nxt = next((x.strip() for x in L[k + 1:k + 4] if x.strip()), "")
        if nxt.isupper():
            if cur: paras.append(cur); cur = []
            paras.append(["##CH " + s]); continue
    if not s:
        if cur: paras.append(cur); cur = []
        continue
    if re.fullmatch(r"([\dioIlS]{2,4} )?[A-Z][A-Z :;,'’\-]{3,60}( [\dioIlS]{2,4})?", s) and len(s) < 60 and re.search(r"(^|\s)[\dioIlS]{2,4}($|\s)", s) and not any(s == x for x in ()):
        continue  # 頁番号つきの柱
    if re.fullmatch(r"[\divxlc .]{1,8}", s, re.I):  # 頁番号
        continue
    if re.fullmatch(r"(\d+ )?[A-Z][A-Z :;,'’\-]{3,60}( \d+)?", s) and len(s) < 60 and not cur:
        if paras and paras[-1][0].startswith("##"):
            paras[-1][0] += " / " + s  # 章の見出し
        continue  # それ以外は柱なので捨てる
    cur.append(s)
if cur: paras.append(cur)
out = []
for p in paras:
    t = ""
    for s in p:
        if t.endswith("¬") or (t.endswith("-") and not t.endswith(" -")):
            t = t.rstrip("¬-") + s
        else:
            t = (t + " " + s).strip()
    if out and not out[-1].startswith("##") and not t.startswith("##") and not re.search(r"[.:;!?”\"’)—]$", out[-1]) and t[:1].islower():
        out[-1] += " " + t
    else:
        out.append(t)
(D / "clean.txt").write_text("\n\n".join(out) + "\n", encoding="utf-8")
print(len(out))
