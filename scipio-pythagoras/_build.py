"""draft/ の下書きから全訳ファイルと note 用原稿2本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/p{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 5)}
body = "\n\n".join(p[i] for i in range(1, 5))

full = head.replace(head.split("\n", 1)[0], "# スキピオの夢／ピュタゴラスの黄金の詩句と象徴", 1) + "\n\n---\n\n" + body + "\n"
(D / "スキピオの夢とピュタゴラス_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Collectanea Hermetica Vol. V (Somnium Scipionis, with an essay by L. O.; The Golden Verses of Pythagoras by A. E. A.; The Symbols of Pythagoras by S. A.), edited by W. Wynn Westcott, London, 1894. 作業の基にした本文：Internet Archive 公開のスキャン
> 本訳は、原著を全訳したものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による英訳からの翻訳であり、誤りを含む可能性があります。

#ピュタゴラス #スキピオの夢 #キケロ #黄金の夜明け団 #オカルト #翻訳 #パブリックドメイン
"""
title, rest = head.split("\n", 1)
parts = [
    ("前編", (1, 2), "前編には、扉と、キケロ『スキピオの夢』（序・L・O訳・注）、L・Oの論考「秘儀の断片としてのスキピオの夢」を収めます。後編は『ピュタゴラスの黄金の詩句』と『ピュタゴラスの象徴』です。"),
    ("後編", (3, 4), "後編には、『ピュタゴラスの黄金の詩句』（序・本文・A・E・Aによる注）と、サペレ・アウデの『ピュタゴラスの象徴』八十七項を収めます。前編は『スキピオの夢』とL・Oの論考です。"),
]
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{rest}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/スキピオの夢とピュタゴラス_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
