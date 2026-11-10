"""draft/ の下書きから全訳ファイルと note 用原稿3本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
N = 4
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, N + 1)}
body = "\n\n".join(p[i] for i in range(1, N + 1))

full = head.replace(head.split("\n", 1)[0], "# W・W・ウェストコット『ベンボ枢機卿のイシス表』", 1) + "\n\n---\n\n" + body + "\n"
(D / "イシス表_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：W. Wynn Westcott, Tabula Bembina sive Mensa Isiaca. The Isiac Tablet of Cardinal Bembo. Its History and Occult Significance, Bath: Robt. H. Fryar, 1887. 作業の基にした本文と図版：Internet Sacred Text Archive（sacred-texts.com）公開の1887年版の翻刻とスキャン
> 原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Fable 5.2）による翻訳であり、誤りを含む可能性があります。

#ウェストコット #イシス #タロット #カバラ #オカルト #翻訳 #パブリックドメイン
"""

plate = "![ベンボ枢機卿のイシス表（原書の口絵。像を指す文字はキルヒャーが付けたもの）](images/isiac-tablet-1887.jpg)\n\n"
title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1,), "第一回には、梗概、表の記述と来歴（ローマ略奪、ベンボ枢機卿、マントヴァ、トリノ）、ピニョリウスの評価、そしてキルヒャーの解明のうち総論と中段（万象の形をとるイユンクスとしてのイシス、七つの三つ組）を収めます。"),
    ("（二）", (2, 3), "第二回には、キルヒャーの解明のつづき（上段の黄道十二宮と十二の月、下段の四つの方角の門、縁飾りリンブス）と、モンフォーコン、シャックフォード、ウォーバートン、ヤブロンスキー、ケリュス、バニエらの説、大英博物館のルヌーフ教授の見解、そして著者自身の結論を収めます。"),
    ("（三・完）", (4,), "第三回には、エリファス・レヴィの見解とその図の読み解き、そして「トートの書」としてのタロット（二十二枚の切り札とヘブライ文字、『セフェル・イェツィラー』、四つの組札とテトラグラマトン、十のセフィロト）を収めます。"),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    pl = "" if n == 1 else plate
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{pl}{b}\n\n{tail}"
    (D / f"note用/イシス表_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
