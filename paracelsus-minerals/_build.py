"""draft/ の下書きから全訳ファイルと note 用原稿3本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
N = 3
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, N + 1)}
body = "\n\n".join(p[i] for i in range(1, N + 1))

full = head.replace(head.split("\n", 1)[0], "# パラケルスス『鉱物の経済』『金属の組成について』", 1) + "\n\n---\n\n" + body + "\n"
(D / "鉱物の経済_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：パラケルススの名で伝わる Oeconomia mineralium（1584年フランクフルト八折版）と De compositione metallorum（『魔術のアルキドクシス』第六書）。英訳：A. E. Waite, The Hermetic and Alchemical Writings of Paracelsus, vol. 1, London: James Elliott and Co., 1894. 作業の基にした本文と扉：Internet Archive 所蔵の1894年英訳第一巻のスキャン
> 原著と英訳とは日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#パラケルスス #錬金術 #鉱物 #オカルト #神秘主義 #翻訳 #パブリックドメイン
"""

title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1,), "第一回には、『鉱物の経済』の序と第一〜第十五章（水を母とする鉱物の系譜、鉱物の木と果実と死、アルケウスとその下役、塩・ムリア・硝石、緑礬とその試しかた）と、鉄を銅に変える処方や黄金時代の予言を含むジュネーヴ版の異文の注を収めます。"),
    ("（二）", (2,), "第二回には、『鉱物の経済』の第十六〜第二十一章と結び（緑礬の薬効、三重の硫黄、砒素とエレクトルム、水銀、白鉄鉱とカキミア、七つの金属の成り立ち）を収めます。"),
    ("（三・完）", (3,), "第三回には、七つの金属の合金エレクトルムをめぐる小論『金属の組成について』（毒を知らせる杯、癲癇を防ぐ指輪、霊を呼ぶ鈴、惑星の合に合わせた製法）と、『魔術のアルキドクシス』から引かれた金属変成の占星術の表を収めます。"),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/鉱物の経済_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
