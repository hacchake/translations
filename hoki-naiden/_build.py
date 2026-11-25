"""draft/ の下書きから、巻第五の訳・付録・note 用原稿2本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
T = "簠簋内伝金烏玉兎集"
NL = "\n"

S27 = "室壁奎婁胃昴畢觜参井鬼柳星張翼軫角亢氐房心尾箕斗女虚危"
MONN = ["正", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"]
FIRST = "室奎胃畢参鬼張角氐心斗虚"
KAN = "一二三四五六七八九"


def kn(n):
    if n < 10:
        return KAN[n - 1]
    t, o = divmod(n, 10)
    return ("" if t == 1 else KAN[t - 1]) + "十" + (KAN[o - 1] if o else "")


def table360():
    rows = ["| 日 | " + " | ".join(m + "月" for m in MONN) + " |", "|---" * 13 + "|"]
    for d in range(1, 31):
        cells = [S27[(S27.index(FIRST[m]) + d - 1) % 27] for m in range(12)]
        rows.append(f"| {kn(d)}日 | " + " | ".join(cells) + " |")
    return NL.join(rows)


def kashin():
    Y = "日月火水木金土"
    TOKI = "寅卯辰巳午未申酉戌亥子丑"
    rows = ["| 日の曜 | " + " | ".join(TOKI) + " |", "|---" * 13 + "|"]
    for i, y in enumerate(Y):
        cells = []
        for k in range(12):
            c = Y[(i + k) % 7]
            cells.append(f"**{c}**" if c in "日月木" else c)
        rows.append(f"| {y}曜の日 | " + " | ".join(cells) + " |")
    return NL.join(rows) + NL + NL + "（太字が嘉辰縁会の時。そのうち木曜に当たる刻が幸時・万倍時）"


def rd(n):
    return (D / f"draft/{n}.md").read_text(encoding="utf-8").strip()


maki5 = rd("maki5").replace("{{TABLE360}}", table360()).replace("{{KASHIN}}", kashin())
head = rd("head")
fu = rd("fu")

rest = head.split(NL, 1)[1].strip()
info = rest.split("## この本について")[0].strip()
about = "## この本について" + rest.split("## この本について")[1]
body5 = maki5.split(NL, 1)[1].strip()  # 巻名の見出しを除く

# 全訳ファイル（付録の見出しは一段下げる）
fu_full = fu.replace(NL + "### ", NL + "#### ").replace(NL + "## ", NL + "### ").replace("# 訳者による付録", "## 訳者による付録", 1)
full = f"# {T}　巻第五　現代語訳{NL}{NL}{rest}{NL}{NL}---{NL}{NL}{body5}{NL}{NL}---{NL}{NL}{fu_full}{NL}"
(D / f"{T}_巻第五_現代語訳.md").write_text(full, encoding="utf-8")
(D / f"{T}_付録.md").write_text(fu.replace("# 訳者による付録", f"# {T}　訳者による付録（巻第一〜第四の解説ほか）", 1) + NL, encoding="utf-8")


def demote(t):
    """記事タイトル以外の「# 」見出しを「## 」に下げる。"""
    out, first = [], True
    for l in t.split(NL):
        if l.startswith("# "):
            if first:
                first = False
            else:
                l = "#" + l
        out.append(l)
    return NL.join(out)


def tables_to_lines(t):
    """note は表を扱えないので、表を行ごとの箇条書きに直す。"""
    out, buf = [], []

    def flush():
        if not buf:
            return
        rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in buf]
        hdr = rows[0]
        data = [r for r in rows[1:] if not set("".join(r)) <= set("-: ")]
        out.append("（" + "／".join(h for h in hdr if h) + "）")
        out.append("")
        for r in data:
            first = r[0] if r[0] else "　"
            out.append(f"- **{first}**　" + "／".join(r[1:]))
        out.append("")
        buf.clear()

    for l in t.split(NL):
        if l.startswith("|"):
            buf.append(l)
        else:
            flush()
            out.append(l)
    flush()
    return NL.join(out)


TAIL = """---

## 出典

> 原著：『三国相伝陰陽輨轄簠簋内伝金烏玉兎集』（伝 安倍晴明撰、十四世紀ごろ成立）。底本：天和二年（一六八二年）村上勘兵衛刊本（国立国会図書館デジタルコレクション）。図版も同本による。付録の巻第一・第二の解説には、大正八年刊本（同）の全文テキストも参照した。
> 本稿は巻第五を全訳し、巻第一〜第四を付録で解説するもので、二回に分けて掲載します。原著・底本とも保護期間が満了しています。訳文と解説は人工知能（Claude Opus 5.5）によるもので、誤りを含む可能性があります。

#簠簋内伝 #安倍晴明 #陰陽道 #宿曜 #暦注 #現代語訳 #古典
"""

(D / "note用").mkdir(exist_ok=True)
p1 = (f"<!-- note投稿用（draft から生成） -->{NL}{NL}# 【現代語訳】伝 安倍晴明『{T}』巻第五（宿曜の巻）　その一{NL}{NL}"
      f"{info}{NL}{NL}{about.strip()}{NL}{NL}---{NL}{NL}{body5}{NL}{NL}---{NL}{NL}"
      f"巻第一〜第四の解説などの付録は、その二に載せています。{NL}{NL}{TAIL}")
p2 = (f"<!-- note投稿用（draft から生成） -->{NL}{NL}# 【現代語訳】伝 安倍晴明『{T}』巻第五　その二（付録：巻第一〜第四の解説）{NL}{NL}"
      f"{info}{NL}{NL}全二回のうち第二回です。この本の解説と巻第五の訳は第一回に載せています。{NL}{NL}---{NL}{NL}{fu}{NL}{NL}{TAIL}")
for k, p in enumerate((p1, p2), 1):
    p = tables_to_lines(demote(p))
    (D / f"note用/{T}_note_{k}.md").write_text(p, encoding="utf-8")
    print(k, len(p))
print("full", len(full))
