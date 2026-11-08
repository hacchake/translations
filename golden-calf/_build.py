"""draft/ の下書きから全訳ファイルと note 用原稿2本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 4)}
body = "\n\n".join(p[i] for i in range(1, 4))

full = head.replace(head.split("\n", 1)[0], "# 金の子牛（ヘルヴェティウス）", 1) + "\n\n---\n\n" + body + "\n"
(D / "金の子牛_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原典：Johann Friedrich Helvetius, Vitulus Aureus, quem mundus adorat et orat, Amsterdam, 1667（Musaeum Hermeticum, Frankfurt, 1678 所収）。英訳：A. E. Waite, The Hermetic Museum, Restored and Enlarged, vol. 2, London: James Elliott, 1893. 作業の基にした本文と図版：Internet Archive 所蔵の1893年英訳第二巻のスキャン
> 原典と英訳とは日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#錬金術 #賢者の石 #ヘルヴェティウス #ヘルメス主義 #オカルト #翻訳 #パブリックドメイン
"""

title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1, 2), "第一回には、扉と献辞、第一章（序）、第二章（パラケルスス、クンラート、ファン・ヘルモントの証言、プラハのメダル、グリルの例）、第三章（術師エリアスの訪問と鉛の金への変成、試金）、第四章の対話のはじまりを収めます。"),
    ("（二・完）", (3,), "第二回には、第四章の医者と術師エリアスとの対話の続き（普遍の薬と体質、命の精気、変成のチンキ、秘密を守る誓い、読むべき著者）と、ヘルヴェティウスの結びとを収めます。"),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/金の子牛_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
