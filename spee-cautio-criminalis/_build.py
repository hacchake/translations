"""draft/ の下書きから全訳ファイル、用語集、note 用原稿3本を生成する。"""
import pathlib, re

D = pathlib.Path(__file__).parent
T = "犯罪への警告"
NAMES = sorted(p.stem for p in (D / "draft").glob("c*.md"))


def demote(t):
    out = []
    for l in t.split("\n"):
        if l.startswith("### "):
            l = "**" + l[4:] + "**"
        elif l.startswith("## ") or l.startswith("# "):
            l = "#" + l
        out.append(l)
    return "\n".join(out)


def r(name):
    t = (D / f"draft/{name}.md").read_text(encoding="utf-8").strip()
    return t if name == "head" else demote(t)


def untable(t):
    out = []
    for l in t.split("\n"):
        if l.startswith("|"):
            c = [x.strip() for x in l.strip("|").split("|")]
            if c[0].startswith("原語") or set(c[0]) <= set("-: "):
                continue
            out.append(f"- {c[0]}　→　{c[1]}" + (f"：{c[2]}" if len(c) > 2 and c[2] else ""))
        else:
            out.append(l)
    return "\n".join(out)


head = r("head")
rest = head.split("\n", 1)[1]
info = rest.split("## この本について")[0].strip()
info_noimg = "\n".join(l for l in info.split("\n") if not l.startswith("!["))
about_toc = "## この本について" + rest.split("## この本について")[1]

body = "\n\n".join(r(n) for n in NAMES)
full = f"# {T}（フリードリヒ・シュペー）\n\n{rest.strip()}\n\n---\n\n{body}\n"
(D / f"{T}_全訳.md").write_text(full, encoding="utf-8")
(D / f"{T}_用語集.md").write_text((D / "draft/c46.md").read_text(encoding="utf-8").strip().replace("# 訳者による付録", f"# {T}　訳者による付録", 1) + "\n", encoding="utf-8")

PARTS = [
    ("その一　序・第一問〜第十九問", [n for n in NAMES if n <= "c10"]),
    ("その二　第二十問〜第三十五問", [n for n in NAMES if "c11" <= n <= "c25"]),
    ("その三　第三十六問〜第五十一問・付録", [n for n in NAMES if n >= "c26"]),
]
TAIL = """---

## 出典

> 原著：[Friedrich Spee von Langenfeld,] Cautio Criminalis, seu de processibus contra sagas liber, Rinthelii, Petrus Lucius, 1631.
> 本訳は、ラテン語原典を全訳したものを三回に分けて掲載するものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#魔女裁判 #魔女狩り #シュペー #イエズス会 #拷問 #翻訳 #パブリックドメイン
"""
(D / "note用").mkdir(exist_ok=True)
for k, (sub, ns) in enumerate(PARTS, 1):
    top = f"<!-- note投稿用（全訳から生成） -->\n\n# 【全訳】フリードリヒ・シュペー『{T}』（1631年）{sub}\n\n{info_noimg}\n"
    if k == 1:
        img = [l for l in info.split("\n") if l.startswith("![")][0]
        top += "\n" + img + "\n\n" + about_toc.strip() + "\n"
    else:
        top += f"\n全三回のうち第{'一二三'[k-1]}回です。この本の解説は第一回に載せています。\n"
    b = untable("\n\n".join(r(n) for n in ns))
    txt = f"{top}\n---\n\n{b}\n\n{TAIL}"
    (D / f"note用/{T}_note_{k}.md").write_text(txt, encoding="utf-8")
    print(k, len(txt), ns[0], ns[-1])
print("full", len(full))
