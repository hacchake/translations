"""draft/ の下書きから全訳ファイルと note 用原稿3本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 9)}
body = "\n\n".join(p[i] for i in range(1, 9))

full = head.replace(head.split("\n", 1)[0], "# 小人たちのあいだで（フランツ・ハルトマン）", 1) + "\n\n---\n\n" + body + "\n"
(D / "小人たちのあいだで_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Franz Hartmann, Among the Gnomes: An Occult Tale of Adventure in the Untersberg, London: T. Fisher Unwin, 1895. 作業の基にした本文：Global Grey の電子版。挿絵：Internet Archive 所蔵の1895年初版
> 原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#フランツハルトマン #小人 #元素霊 #神秘主義 #オカルト #翻訳 #パブリックドメイン
"""


def for_note(s):
    # note には裸体を含む「竜の穴」の挿絵を載せない
    return "\n".join(l for l in s.split("\n") if "dragons-den.jpg" not in l).replace("\n\n\n", "\n\n")


title, rest = head.split("\n", 1)
parts = [
    ("（一）", (1, 2, 3), "第一回には、第一章「序」、第二章「竜の穴にて」、第三章「ウンタースベルクの内部で」を収めます。懐疑派の委員会が小人の非存在を証明しに山へ登り、語り手は洞穴の奥で王女アダルガに出会って小人の王国へ導かれます。"),
    ("（二）", (4, 5, 6), "第二回には、第四章と第五章「小人たちのあいだで」、第六章「ルシファー」を収めます。語り手は宮廷の占い師となって小人たちの暮らしと種族とを見聞し、やがて荒野の果ての「ルシファーの神殿」に踏みこみます。"),
    ("（三・完）", (7, 8), "第三回には、第七章「光を求めて掘る」と第八章「戦争」を収めます。太陽を見るために空に穴を掘りはじめた小人の王国は、論理と懐疑との教育によって変わりはて、ついに空気の精の国と戦争を始めます。"),
]
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    note = for_note(f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{rest}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}")
    (D / f"note用/小人たちのあいだで_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
