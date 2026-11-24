"""draft/ の下書きから全訳ファイルと note 用原稿3本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
T = "暦林問答集"
BODY = [f"{i:02d}" for i in range(1, 11)]


def demote(t):
    out = []
    for l in t.split("\n"):
        if l.startswith("### "):
            l = "**" + l[4:] + "**"
        elif l.startswith("## ") or l.startswith("# "):
            l = "#" + l
        out.append(l)
    return "\n".join(out)


def r(name, dem=True):
    t = (D / f"draft/{name}.md").read_text(encoding="utf-8").strip()
    return demote(t) if dem else t


head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
rest = head.split("\n", 1)[1].strip()
info = rest.split("## この本について")[0].strip()
about_toc = "## この本について" + rest.split("## この本について")[1]
fu = (D / "draft/fu.md").read_text(encoding="utf-8").strip()

# 全訳（見出しの階層はそのまま）
body = "\n\n".join((D / f"draft/{n}.md").read_text(encoding="utf-8").strip() for n in BODY)
full = f"# {T}（賀茂在方）　現代語訳\n\n{rest}\n\n---\n\n{body}\n\n---\n\n{fu.replace('# 訳者による付録', '## 訳者による付録', 1).replace(chr(10) + '## ', chr(10) + '### ')}\n"
(D / f"{T}_現代語訳.md").write_text(full, encoding="utf-8")
(D / f"{T}_付録.md").write_text(fu.replace("# 訳者による付録", f"# {T}　訳者による付録", 1) + "\n", encoding="utf-8")

PARTS = [
    ("その一　序・上巻（天地から歳次まで）", ["01", "02"], False),
    ("その二　上巻（二十四気・七十二候から月建まで）", ["03", "04", "05", "06"], False),
    ("その三　下巻・跋・付録", ["07", "08", "09", "10"], True),
]
KANJI = "一二三"
TAIL = """---

## 出典

> 原著：賀茂在方『暦林問答集』（応永二十一年〈一四一四年〉序）。底本：塙保己一編『群書類従』巻第五百六 雑部六十一（版本、国立国会図書館デジタルコレクション）。図版も同本による。
> 本訳は、序・本文六十四段・跋・奥書を全訳し、三回に分けて掲載するものです。原著・底本とも保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#暦林問答集 #賀茂在方 #陰陽道 #暦注 #陰陽師 #現代語訳 #古典
"""
(D / "note用").mkdir(exist_ok=True)
for k, (sub, ns, with_fu) in enumerate(PARTS, 1):
    top = f"<!-- note投稿用（draft から生成） -->\n\n# 【現代語訳】賀茂在方『{T}』（一四一四年）{sub}\n\n{info}\n"
    if k == 1:
        top += "\n" + about_toc.strip() + "\n"
    else:
        top += f"\n全三回のうち第{KANJI[k-1]}回です。この本の解説と目次は第一回に載せています。\n"
    b = "\n\n".join(r(n) for n in ns)
    if with_fu:
        b += "\n\n---\n\n" + demote(fu)
    txt = f"{top}\n---\n\n{b}\n\n{TAIL}"
    (D / f"note用/{T}_note_{k}.md").write_text(txt, encoding="utf-8")
    print(k, len(txt), ns[0], ns[-1])
print("full", len(full))
