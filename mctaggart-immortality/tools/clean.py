"""OCR テキストから柱（ページ見出し）を除き、段落をつなぐ。"""
import pathlib, re, sys
src, out = sys.argv[1], sys.argv[2]
t = pathlib.Path(src).read_text(encoding="utf-8")
t = re.sub(r"[ \t]+", " ", t)
lines = [l.strip() for l in t.split("\n")]
# 柱：「10 HUMAN IMMORTALITY」「HUMAN PRE-EXISTENCE 73」など
pat = re.compile(r"^(\w{1,3} )?(HUMAN IMMORTALITY|HUMAN PRE-EXISTENCE|POSTSCRIPT|HUMAN IMMORTALITY AND)( \w{1,3})?$")
lines = [l for l in lines if not pat.match(l)]
paras, cur = [], []
for l in lines:
    if not l:
        if cur:
            paras.append(" ".join(cur)); cur = []
    else:
        cur.append(l)
if cur: paras.append(" ".join(cur))
# ページまたぎ：文末記号で終わらない段落は次とつなぐ
res = []
for p in paras:
    if res and not re.search(r"[.?!:'\"”’)]$", res[-1]) and not res[-1].isupper():
        res[-1] = (res[-1][:-1] if res[-1].endswith("-") else res[-1] + " ") + p
    else:
        res.append(p)
text = "\n\n".join(res)
text = re.sub(r"(\w)- (\w)", r"\1\2", text)
pathlib.Path(out).write_text(text, encoding="utf-8")
print(len(text.split()))
