"""draft/ の下書きから全訳ファイルと note 用原稿3本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
N = 4
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, N + 1)}
body = "\n\n".join(p[i] for i in range(1, N + 1))

full = head.replace(head.split("\n", 1)[0], "# パラケルスス『元素の生成について』ほか小論三篇", 1) + "\n\n---\n\n" + body + "\n"
(D / "元素の生成について_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：パラケルススの名で伝わる Philosophia de generationibus et fructibus quatuor elementorum ほか（ジュネーヴ版全集1658年第二巻など）。英訳：A. E. Waite, The Hermetic and Alchemical Writings of Paracelsus, vol. 1, London: James Elliott and Co., 1894. 作業の基にした本文と扉：Internet Archive 所蔵の1894年英訳第一巻のスキャン
> 原著と英訳とは日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#パラケルスス #錬金術 #四元素 #オカルト #神秘主義 #翻訳 #パブリックドメイン
"""

title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1, 2), "第一回には、金属から水銀・硫黄・クロクスを取り出す三つの小論と、『元素の生成について』第一の書「空気の元素について」（イリアステルの分割、三原質、卵の殻としての空、地球を浮かべる混沌、上下のない丸い世界）を収めます。"),
    ("（二）", (3,), "第二回には、第二の書「火の元素について」（太陽マグダリオンと赤い星々、太陽の休耕と星々の収穫、蒼穹の不死鳥としての月、風の星、露と霧、天から降る金属と宝石、水晶と緑柱石）と、『気象の書』からの長い補注を収めます。"),
    ("（三・完）", (4,), "第三回には、第三の書「土の元素について」（アニアドゥスによる草木の配分、楽園から来た種、木を人にたとえる比喩）と、第四の書「水の元素とその果実について」（川を枝とする一本の水の木、天蓋としての海、塩・鉱物・宝石・石）を収めます。"),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/元素の生成について_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
