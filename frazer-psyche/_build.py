"""draft/ の下書きと Gutenberg の原注から、全訳ファイルと note 用原稿2本を生成する。"""
import json, pathlib, re, sys
D = pathlib.Path(__file__).parent
sys.path.insert(0, str(D / "draft"))
from notes_ja import JA

NL2 = "\n\n"
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
rd = lambda n: (D / f"draft/{n}.md").read_text(encoding="utf-8").strip()
part1 = NL2.join(rd(n) for n in ["a00"] + [f"a{i:02d}" for i in range(1, 16)])
part2 = NL2.join(rd(n) for n in ("b01", "b02"))

notes = json.load(open(D / "src/notes.json", encoding="utf-8"))


def fmt(k, v):
    v = v.replace(" The Scope of Social Anthropology Notes", "")
    v = re.sub(r"_([^_]+)_", r"*\1*", v)
    s = f"〔{k}〕　{v}"
    if k in JA:
        s += f"\n　　（訳）{JA[k]}"
    return s


def note_block(lo, hi):
    return NL2.join(fmt(k, v) for k, v in notes if lo <= float(k) < hi)


nb1, nb2 = note_block(0, 157), note_block(157, 999)
NOTE_HEAD = "## 原注" + NL2 + "〔訳注〕原注の典拠（書名・ページ）は原文のまま残した。説明の文を含む注には、その部分の訳を「（訳）」として添えた。"
full = (head.replace(head.split("\n", 1)[0], "# プシュケーの務め（J・G・フレイザー）", 1)
        + NL2 + "---" + NL2 + part1 + NL2 + NOTE_HEAD + NL2 + "**プシュケーの務め**" + NL2 + nb1
        + NL2 + "---" + NL2 + part2 + NL2 + "**社会人類学の範囲の原注**" + NL2 + nb2 + "\n")
(D / "プシュケーの務め_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：J. G. Frazer, Psyche's Task: A Discourse concerning the Influence of Superstition on the Growth of Institutions, Second Edition, Macmillan, London, 1913（初版1909年）。作業の基にした本文：Project Gutenberg 版
> 本訳は、原著を全訳したものです（索引を除く）。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#フレイザー #金枝篇 #文化人類学 #宗教学 #迷信 #翻訳 #パブリックドメイン
"""
title, rest = head.split("\n", 1)
SPLIT = "## 五　人命の尊重"
pa, pb = part1.split(SPLIT)
parts = [
    ("前編", pa,
     "前編には、エピグラフと献辞、序文、第二版への付記、本文の第一章「序論」から第四章「結婚」までと、その原注を収めます。後編は第五章「人命の尊重」、第六章「結論」、講演「社会人類学の範囲」とその原注です。",
     NOTE_HEAD + NL2 + note_block(0, 111)),
    ("後編", SPLIT + pb + NL2 + "---" + NL2 + part2,
     "後編には、本文の第五章「人命の尊重」、第六章「結論」、付録の講演「社会人類学の範囲」と、それらの原注を収めます。前編は序文から第四章「結婚」までです。",
     NOTE_HEAD + NL2 + "**プシュケーの務め**" + NL2 + note_block(111, 157) + NL2 + "**社会人類学の範囲**" + NL2 + nb2),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, b, summ, nts) in enumerate(parts, 1):
    note = (f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{rest}\n\n## この記事の内容\n\n　{summ}"
            + NL2 + "---" + NL2 + b + NL2 + nts + NL2 + tail)
    (D / f"note用/プシュケーの務め_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
