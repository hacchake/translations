"""OCRテキスト(djvu.txt)の本文部分を段落ごとに整形して clean.txt に書き出す。"""
import re, pathlib
D = pathlib.Path(__file__).parent / "src"
lines = (D / "djvu.txt").read_text(encoding="utf-8").split("\n")
start = next(i for i, l in enumerate(lines) if l.startswith("The  study  of  Magic"))
end = next(i for i, l in enumerate(lines) if l.strip().startswith("THE  END"))
paras, cur = [], []
for l in lines[start:end + 1]:
    s = re.sub(r"\s+", " ", l).strip()
    if not s:
        if cur: paras.append(cur); cur = []
        continue
    if re.fullmatch(r"[\d\W]{1,6}|[ivxl]+|y", s):  # 頁番号・ゴミ
        continue
    cur.append(s)
if cur: paras.append(cur)
out = []
for p in paras:
    t = ""
    for s in p:
        if t.endswith("-") and not t.endswith(" -"):
            t = t[:-1] + s
        else:
            t = (t + " " + s).strip()
    t = re.sub(r"(\w)- (\w)", r"\1\2", t)
    if out and not re.search(r"[.:;!?”\"’)]$", out[-1]) and t[:1].islower():
        out[-1] += " " + t
    else:
        out.append(t)
(D / "clean.txt").write_text("\n\n".join(out) + "\n", encoding="utf-8")
print(len(out), sum(len(x.split()) for x in out))
