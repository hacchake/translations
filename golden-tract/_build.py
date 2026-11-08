"""draft/ の下書きから全訳ファイルと note 用原稿3本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 5)}
body = "\n\n".join(p[i] for i in range(1, 5))

full = head.replace(head.split("\n", 1)[0], "# 賢者の石についての黄金論文", 1) + "\n\n---\n\n" + body + "\n"
(D / "黄金論文_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原典：Tractatus Aureus de Lapide Philosophorum（Musaeum Hermeticum, Frankfurt, 1625／1678）。英訳：A. E. Waite, The Hermetic Museum, Restored and Enlarged, vol. 1, London: James Elliott, 1893. 作業の基にした本文と図版：Internet Archive 所蔵の1893年英訳第一巻のスキャン
> 原典と英訳とは日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#錬金術 #賢者の石 #薔薇十字 #ヘルメス主義 #オカルト #翻訳 #パブリックドメイン
"""

title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1, 2), "第一回には、作者の序と、論文前半（賢者たちの一致、物質が一つであること、動物・植物・石・塩・中間の鉱物・緑礬・普通の硫黄と水銀とを退ける議論、不完全な金属の検討の始まり）を収めます。"),
    ("（二）", (3,), "第二回には、論文の続き（不完全な金属を退け、物質は「賢者たちの生きた金と銀」にあるとする議論）と「溶解について」を収めます。"),
    ("（三・完）", (4,), "第三回には、溶解の二つの段階と論文の結び、短い詩、そして作業の全体を物語る「たとえ話」（獅子、薔薇の庭、水車、兄妹の王と女王の死と再生）を収めます。"),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/黄金論文_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
