"""OCR テキストから柱（ページ見出し）を除き、段落をつなぐ。"""
import pathlib, re, sys
src, out = sys.argv[1], sys.argv[2]
t = pathlib.Path(src).read_text(encoding="utf-8")
t = re.sub(r"[ \t]+", " ", t)
lines = [l.strip() for l in t.split("\n")]
# 柱：「2 Human Immortality」「Notes 57」「vi Preface to Second Edition」など
pat = re.compile(r"^(\w{1,4} )?(Human Immortality|Preface to Second Edition|Notes)( \w{1,4})?$")
lines = [l for l in lines if not pat.match(l)]
paras, cur = [], []
for l in lines:
    if not l:
        if cur:
            paras.append(" ".join(cur)); cur = []
    else:
        cur.append(l)
if cur:
    paras.append(" ".join(cur))
# ページまたぎ：文末記号で終わらない段落は次とつなぐ
END = ".?!:)" + "'" + '"' + "”’"
res = []
for p in paras:
    if res and res[-1][-1] not in END and not res[-1].isupper():
        res[-1] = res[-1] + " " + p
    else:
        res.append(p)
pathlib.Path(out).write_text("\n\n".join(res), encoding="utf-8")
print(len(res))
