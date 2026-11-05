"""draft/ の下書きから全訳ファイルと note 用原稿2本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 7)}
body = "\n\n".join(p[i] for i in range(1, 7))

full = head.replace(head.split("\n", 1)[0], "# 秘儀参入者の訓練とはたらき（ダイアン・フォーチュン）", 1) + "\n\n---\n\n" + body + "\n"
(D / "秘儀参入者の訓練とはたらき_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Dion Fortune, The Training and Work of an Initiate, Rider, London, 1930. 作業の基にした本文：Internet Archive 公開の第二版（The Aquarian Press, London, 1955）のスキャン
> 本訳は、原著を全訳したものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#ダイアンフォーチュン #秘儀参入 #西洋魔術 #神秘主義 #オカルト #翻訳 #パブリックドメイン
"""
title, rest = head.split("\n", 1)
parts = [
    ("前編", (1, 2, 3), "前編には、序論、第一部「倫理」（第一章〜第六章）、第二部「理論」のうち第七章〜第九章「照明主義の見取り図」を収めます。後編は第十章「オカルティズムの源流」から第十六章「西方の秘教の体系」、分類表と訳注までです。"),
    ("後編", (4, 5, 6), "後編には、第十章「オカルティズムの源流」、第十一章「秘教的キリスト教の伝統の源」、第十二章「秘儀のアルファベット」、第三部「実践」（第十三章〜第十六章）、巻末の分類表と訳注を収めます。前編は序論から第九章までです。"),
]
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{rest}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/秘儀参入者の訓練とはたらき_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
