"""draft/ の下書きから全訳ファイルと note 用原稿3本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 6)}
body = "\n\n".join(p[i] for i in range(1, 6))

full = head.replace(head.split("\n", 1)[0], "# 賢者たちの水石", 1) + "\n\n---\n\n" + body + "\n"
(D / "賢者たちの水石_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原典：[Johann Ambrosius Siebmacher], Wasserstein der Weysen (Frankfurt, 1619); Hydrolithus Sophicus (Musaeum Hermeticum, Frankfurt, 1678)。英訳：A. E. Waite, The Hermetic Museum, Restored and Enlarged, vol. 1, London: James Elliott, 1893. 作業の基にした本文と扉：Internet Archive 所蔵の1893年英訳第一巻のスキャン
> 原典と英訳とは日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#錬金術 #賢者の石 #キリスト教神秘思想 #ヘルメス主義 #オカルト #翻訳 #パブリックドメイン
"""

title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1, 2), "第一回には、序と、第一部（術に取り組む者の心構え）、第二部（石の物質の性質、作業の手順、失敗の手当て、謎の詩）、第三部（石の効用）の大部分を収めます。"),
    ("（二）", (3, 4), "第二回には、第三部の結びと、第四部「地上の石と天の隅の親石キリストとの類比」の前半から中ほど（受肉、受難、死と復活、洗礼、信仰の成長、悪魔の試み、内なる火、聞くこと、愛）を収めます。"),
    ("（三・完）", (5,), "第三回には、第四部の結び（十字架の炉、烏の頭、復活、悔い改めと聖餐）と、エピローグ、付録、祈り、二つのエピグラムを収めます。"),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/賢者たちの水石_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
