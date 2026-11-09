"""draft/ の下書きから全訳ファイルと note 用原稿3本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 5)}
body = "\n\n".join(p[i] for i in range(1, 5))

full = head.replace(head.split("\n", 1)[0], "# フィラレテスの三つの論文", 1) + "\n\n---\n\n" + body + "\n"
(D / "フィラレテスの三つの論文_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原典：Eirenaeus Philalethes, Metamorphosis Metallorum; Brevis Manuductio ad Rubinum Coelestem; Fons Chymicae Veritatis (Amsterdam, 1668; Musaeum Hermeticum, Frankfurt, 1678)。英訳：A. E. Waite, The Hermetic Museum, Restored and Enlarged, vol. 2, London: James Elliott, 1893. 作業の基にした本文と扉：Internet Archive 所蔵の1893年英訳第二巻のスキャン
> 原典と英訳とは日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#錬金術 #賢者の石 #フィラレテス #ヘルメス主義 #オカルト #翻訳 #パブリックドメイン
"""

title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1, 2), "第一回には、第一論文『金属の変容』の全八章（術への非難への反論と学ぶ者の心得、術の起源と著者たち、元素と金属の生成、金と銀との生成、金の種、その抽出、第一の働き手すなわち子宮、賢者たちのメルクリウスの系譜）を収めます。"),
    ("（二）", (3,), "第二回には、第二論文『天のルビーへの短い携行の手引き』の前半から中ほど（石とは何か、なぜ石と呼ばれるか、いかに得られるか、我々の水、十二の過程の第一である焼成、二匹の蛇、黒の段階）を収めます。"),
    ("（三・完）", (4,), "第三回には、第二論文の結び（黒から白への色の順序、溶解）と、第三論文『化学の真理の泉』の全体（十の作業と二つの火、汚い衣の清い乙女としての水、南西の山と草サトゥルニア、金の種と生きた金）を収めます。"),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/フィラレテスの三つの論文_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
