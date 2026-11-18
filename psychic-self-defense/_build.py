"""draft/ の下書きから全訳ファイル、用語集、note 用原稿3本（部ごと）を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
T = "心霊的自己防衛"


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


head = r("head")
title_line, rest = head.split("\n", 1)
info = rest.split("## この本について")[0].strip()          # 著者行と書誌の箇条
about_toc = "## この本について" + rest.split("## この本について")[1]

body = "\n\n".join(r(f"n{i}") for i in range(1, 17))
full = f"# {T}（ダイアン・フォーチュン）\n\n{rest.strip()}\n\n---\n\n{body}\n"
(D / f"{T}_全訳.md").write_text(full, encoding="utf-8")
(D / f"{T}_用語集.md").write_text((D / "draft/n16.md").read_text(encoding="utf-8").strip().replace("# 付録　用語集・人名と書名の解説", f"# {T}　用語集・人名と書名の解説", 1) + "\n", encoding="utf-8")

PARTS = [
    ("その一　序文・第一部「心霊的な攻撃の種類」", range(1, 8)),
    ("その二　第二部「鑑別診断」・第三部「心霊的な攻撃の診断」", range(8, 12)),
    ("その三　第四部「防衛の方法」・結論・付録", range(12, 17)),
]
TAIL = """---

## 出典

> 原著：Dion Fortune, Psychic Self-Defence: A Study in Occult Pathology and Criminality, Rider, London, 1930.
> 本訳は、原著を全訳したものを三回に分けて掲載するものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。商業出版の既訳として、大島有子訳『心霊的自己防衛』（国書刊行会）があります。

#ダイアンフォーチュン #心霊的自己防衛 #秘教 #西洋魔術 #オカルト #翻訳 #パブリックドメイン
"""
(D / "note用").mkdir(exist_ok=True)
for k, (sub, rng) in enumerate(PARTS, 1):
    top = f"<!-- note投稿用（全訳から生成） -->\n\n# 【全訳】ダイアン・フォーチュン『{T}』（1930年）{sub}\n\n{info}\n"
    if k == 1:
        top += "\n" + about_toc.strip() + "\n"
    else:
        top += f"\n全三回のうち第{'一二三'[k-1]}回です。この本の解説と全体の目次は第一回に載せています。\n"
    b = "\n\n".join(r(f"n{i}") for i in rng)
    txt = f"{top}\n---\n\n{b}\n\n{TAIL}"
    (D / f"note用/{T}_note_{k}.md").write_text(txt, encoding="utf-8")
    print(k, len(txt))
print("full", len(full))
