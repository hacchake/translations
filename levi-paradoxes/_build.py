"""draft/ の下書きから全訳ファイルと note 用原稿3本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(0, 11)}
body = "\n\n".join(p[i] for i in range(0, 11))

full = head.replace(head.split("\n", 1)[0], "# 至高の学の逆説（エリファス・レヴィ）", 1) + "\n\n---\n\n" + body + "\n"
(D / "至高の学の逆説_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Éliphas Lévi, The Paradoxes of the Highest Science, Theosophical Miscellanies, Calcutta, 1883（第二版 Theosophical Publishing House, Adyar, 1922）. 作業の基にした本文：Global Grey の電子版
> 本訳は、英訳を全訳したものです。原著・英訳は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#エリファスレヴィ #魔術 #神智学 #神秘主義 #オカルト #翻訳 #パブリックドメイン
"""
title, rest = head.split("\n", 1)
parts = [
    ("（一）", (0, 1, 2, 3), "第一回には、英訳者の序文、第二版の序言、第一の逆説「宗教とは、権威によって認可された魔術である」、第二の逆説「自由とは、法への服従である」、第三の逆説「愛とは、不可能なものの実現である」と、その注を収めます。"),
    ("（二）", (4, 5, 6, 7), "第二回には、第四の逆説「知識とは、悪を知らないこと、あるいは悪の否定である」、第五の逆説「理性は神である」、第六の逆説「想像力は、その発明するものを実現する」、第七の逆説「意志は、それが欲しないすべてのことをなしとげる」と、その注を収めます。"),
    ("（三）", (8, 9, 10), "第三回には、長い「総括」（魔術と魔術学、五十一か条の原理、大いなる秘密）と、その注を収めます。"),
]
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{rest}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/至高の学の逆説_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
