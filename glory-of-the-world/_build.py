"""draft/ の下書きから全訳ファイルと note 用原稿4本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
N = 8
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, N + 1)}
body = "\n\n".join(p[i] for i in range(1, N + 1))

full = head.replace(head.split("\n", 1)[0], "# 世界の栄光、あるいは楽園の板", 1) + "\n\n---\n\n" + body + "\n"
(D / "世界の栄光_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原典：Gloria Mundi, alias Paradeiss Taffel（ラテン語訳は Musaeum Hermeticum, Frankfurt, 1678 所収）。英訳：A. E. Waite, The Hermetic Museum, Restored and Enlarged, vol. 1, London: James Elliott, 1893. 作業の基にした本文と扉：Internet Archive 所蔵の1893年英訳第一巻のスキャン
> 原典と英訳とは日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#錬金術 #賢者の石 #楽園の板 #ヘルメス主義 #オカルト #翻訳 #パブリックドメイン
"""

title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1, 2), "第一回には、扉と冒頭の祈り、この術を愛する人々への勧め、石を見分けるいくつもの方法、チンキの中の宝、体と霊、塩についての説、セニオルによる物質と方法、土の浄め、太陽を父とし月を母とすること、第一の物質すなわち金属の種、まことの術の単純な説明までを収めます。"),
    ("（二）", (3, 4), "第二回には、著者が子らに宛てた「遺言」とヒュレー、第二部（アダムとセツと十字架の木、まことの術の説明、著者自身の意見、金属の起源、火と水、「子どもの尿」と「賢者たちのメルクリウス」、アルベルトゥスによる組成）、そして第三部「賢者たちの言葉」の最初の三つ（アダム、アベル、セツ）を収めます。"),
    ("（三）", (5, 6), "第三回には、「賢者たちの言葉」の第四から第六十七まで（ピタゴラス、パルメニデス、アリストテレス、プラトン、エメラルド板、ソクラテス、ノア、ゲベルほか）と、格言の解説の前半（アダム、アベル、セツ、イシンドルス、アナクサゴラスの言葉の解説）を収めます。"),
    ("（四・完）", (7, 8), "第四回には、格言の解説の後半（ピタゴラス、アリステウス、パルメニデス、ルカス、エテリウス、ヘルメスのエメラルド板）と、巻末の「もう一つの論文」（天地と人の創造、アダムの栄光と堕落、アダムを支えた医薬とセツの十字架の木、体と霊をアダムとエバの結婚になぞらえる作業、トレヴィザン伯の泉の王）と結びの言葉を収めます。"),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/世界の栄光_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
