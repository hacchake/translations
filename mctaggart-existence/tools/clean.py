"""Internet Archive の OCR テキスト（djvu.txt）を章ごとの段落テキストに整える。
使い方: py tools/clean.py  （src/ の2ファイルから src/ch/chNN.txt を作る）"""
import re, pathlib
D = pathlib.Path(__file__).resolve().parent.parent / "src"
OUT = D / "ch"; OUT.mkdir(exist_ok=True)
ROMAN = {}
def roman(s):
    v = {'I':1,'V':5,'X':10,'L':50}; s = s.replace(' ', '').upper(); t = 0
    for i, c in enumerate(s):
        n = v.get(c, 0)
        t += -n if i + 1 < len(s) and v.get(s[i+1], 0) > n else n
    return t
HEAD = re.compile(r"^(\d+\s+[A-Z][A-Z ,\-'’]+\[\s*bk\.?\s*[ivxl]+.*|ch\.?\s*[ivxl ]+\]\s*[A-Z][A-Z ,\-'’]+\s*\d*|\d+|\d+[—-]\d+|[ivxl]+|mct\.?|M\.\s*N\.?.*)\s*$", re.I)
def process(fn, start):
    lines = (D / fn).read_text(encoding="utf-8", errors="replace").split("\n")[start:]
    chapters, cur, num = {}, [], None
    for l in lines:
        s = l.strip()
        m = re.match(r"^CHAPTER\s+([IVXL ]+)$", s)
        if m:
            if num: chapters[num] = cur
            num, cur = roman(m.group(1)), []
            continue
        if s.startswith("INDEX") and num and num > 60: break
        if HEAD.match(s): continue
        cur.append(s)
    if num: chapters[num] = cur
    for n, ls in chapters.items():
        paras, buf = [], ""
        for s in ls + [""]:
            if not s:
                if buf: paras.append(buf); buf = ""
                continue
            s = re.sub(r"\s{2,}", " ", s)
            if buf.endswith("-") and not buf.endswith("--"):
                buf = buf[:-1] + s
            else:
                buf = (buf + " " + s).strip()
        (OUT / f"ch{n:02d}.txt").write_text("\n\n".join(paras) + "\n", encoding="utf-8")
        print(n, len(paras), sum(len(p) for p in paras))
process("natureofexistenc01mctauoft.txt", 1405)
process("natureofexistenc02mctauoft.txt", 3310)
