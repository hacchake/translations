"""draft/ の下書きから全訳ファイルと note 用原稿3本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 9)}
body = "\n\n".join(p[i] for i in range(1, 9))

full = head.replace(head.split("\n", 1)[0], "# アーリア人の知恵（アラン・ベネット）", 1) + "\n\n---\n\n" + body + "\n"
(D / "アーリア人の知恵_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Allan Bennett (Ananda M.), The Wisdom of the Aryas, London: Kegan Paul, Trench, Trubner & Co., 1923. 作業の基にした本文と扉：Internet Archive 所蔵の1923年初版のスキャン
> 原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#アランベネット #仏教 #黄金の夜明け団 #瞑想 #神秘主義 #翻訳 #パブリックドメイン
"""

title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1, 2, 3), "第一回には、献辞、序論、第一章「教えの源――ブッダとその到達」、第二章「根本原理――普遍の法則の支配」を収めます。"),
    ("（二）", (4, 5, 6), "第二回には、第三章「仏教の世界観――三つのしるし」、第四章「四つのアーリアの真理」、第五章「到達の道」を収めます。"),
    ("（三・完）", (7, 8), "第三回には、第六章「三つの帰依と涅槃」と第七章「仏教の再生の教え」を収めます。"),
]
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/アーリア人の知恵_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
