"""draft/ の下書きから全訳ファイルと note 用原稿3本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
N = 6
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, N + 1)}
body = "\n\n".join(p[i] for i in range(1, N + 1))

full = head.replace(head.split("\n", 1)[0], "# センディヴォギウス『化学の新しい光』", 1) + "\n\n---\n\n" + body + "\n"
(D / "化学の新しい光_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原典：Michael Sendivogius, Novum Lumen Chymicum (Prague, 1604); Tractatus de Sulphure (1616)（Musaeum Hermeticum, Frankfurt, 1678 所収）。英訳：A. E. Waite, The Hermetic Museum, Restored and Enlarged, vol. 2, London: James Elliott, 1893. 作業の基にした本文と扉：Internet Archive 所蔵の1893年英訳第二巻のスキャン
> 原典と英訳とは日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#錬金術 #賢者の石 #センディヴォギウス #ヘルメス主義 #オカルト #翻訳 #パブリックドメイン
"""

title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1, 2), "第一回には、扉と著者のアナグラム、序文、アルノルドゥス・デ・ウィラノウァの遺言、そして十二の論文の第一から第十まで（自然とその弟子、自然の働きと種子、金属の第一の物質、金属と石の生成、第二の物質と腐敗、第二の物質の効能、種子における自然の働き、金属の混合と種子の引き出し、太陽の息子の超自然的な生成）を収めます。"),
    ("（二）", (3, 4), "第二回には、第十一・第十二の論文（実践と石の効能）、十二の論文の『結び』、「賢者たちの謎への序文」、南の島の夢を語る「たとえ話」、そして「メルクリウスと錬金術師と自然との対話」を収めます。"),
    ("（三・完）", (5, 6), "第三回には、第二部「硫黄について」の全体（序文、土・水・空気・火の四元素、三つの原理、牢獄の硫黄をめぐるサトゥルヌスとの対話と夢、結び）を収めます。"),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/化学の新しい光_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
