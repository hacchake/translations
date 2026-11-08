"""draft/ の下書きから全訳ファイルと note 用原稿2本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 7)}
body = "\n\n".join(p[i] for i in range(1, 7))

full = head.replace(head.split("\n", 1)[0], "# エノクの神との歩み（ジェイン・リード）", 1) + "\n\n---\n\n" + body + "\n"
(D / "エノクの神との歩み_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Jane Lead, The Enochian Walks with God, London: D. Edwards, 1694. 作業の基にした本文と扉：Internet Archive 所蔵の1694年初版のスキャン
> 原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#ジェインリード #神秘主義 #ベーメ #キリスト教神秘思想 #ソフィア #翻訳 #パブリックドメイン
"""

title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1, 2, 3), "第一回には、扉、序、「心の花」、「エノクの生」（七人の守護の天使、三つの休み場、シオンの山への到着と花婿キリストとの対話）を収めます。"),
    ("（二・完）", (4, 5, 6), "第二回には、「ある適切な問いへの答え」（普遍の救い）、付録の「上なる聖徒と下なる聖徒との交わり」「キリストの現れ方」「追伸」「幻の現れ」を収めます。"),
]
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/エノクの神との歩み_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
