"""draft/ の下書きから全訳ファイルと note 用原稿2本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
N = 4
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, N + 1)}
body = "\n\n".join(p[i] for i in range(1, N + 1))

full = head.replace(head.split("\n", 1)[0], "# パラケルスス『哲学者の天』ほか錬金術小論集", 1) + "\n\n---\n\n" + body + "\n"
(D / "哲学者の天_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：パラケルススの名で伝わる錬金術小品（Coelum Philosophorum ほか）。英訳：A. E. Waite, The Hermetic and Alchemical Writings of Paracelsus, vol. 1, London: James Elliott and Co., 1894. 作業の基にした本文と扉：Internet Archive 所蔵の1894年英訳第一巻のスキャン
> 原著と英訳とは日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#パラケルスス #錬金術 #賢者の石 #ヘルメス主義 #オカルト #翻訳 #パブリックドメイン
"""

title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1, 2), "第一回には、『哲学者の天、あるいは悩みの書』の全体（序文、七つの規範、付録の諸論文と宝石の記述）と、『哲学者のチンキについての書』の序文・第一章・第二章、およびそれぞれに付いた英訳者の注を収めます。"),
    ("（二・完）", (3, 4), "第二回には、『哲学者のチンキについての書』の第三章から第七章（注として『ヘルメスの黙示』全文を含む）、『金属の階梯』、『錬金術師のための宝の中の宝』、『金属と膠剤との変成』と、それぞれに付いた英訳者の注を収めます。"),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/哲学者の天_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
