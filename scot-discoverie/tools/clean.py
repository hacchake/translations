"""OCR テキストから本文（原本99〜568ページ）を取り出し、読みやすく整える。
長い行（本文）は段落に繋ぎ、短い行（欄外注・見出し・柱）は行のまま残す。"""
import re, pathlib
D = pathlib.Path(__file__).parent.parent
raw = (D / "src/scot.txt").read_text(encoding="utf-8")
pages = re.split(r"=====\[p(\d+)\]=====\n", raw)
out = []
for i in range(1, len(pages), 2):
    n = int(pages[i]); t = pages[i + 1]
    if n < 63 or n > 568:
        continue
    out.append(f"\n[[p{n}]]\n")
    buf = ""
    for l in t.split("\n"):
        l = re.sub(r"\s+", " ", l).strip()
        if not l:
            continue
        if len(l) >= 50:
            if buf.endswith("-"):
                buf = buf[:-1] + l
            else:
                buf = (buf + " " + l).strip()
            if re.search(r"[.:;?!)\]]$", l) and len(l) < 62:
                out.append(buf); buf = ""
        else:
            if buf and len(l) > 20 and not re.match(r"^(\d|[A-Z][a-z]*\.|Booke|Chap|of Witch|The disc|Tke|TJie)", l):
                buf = (buf + " " + l).strip(); out.append(buf); buf = ""
            else:
                out.append("    | " + l)
    if buf:
        out.append(buf)
(D / "src/scot_clean.txt").write_text("\n".join(out), encoding="utf-8")
print(len("\n".join(out)))
