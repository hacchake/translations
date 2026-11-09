"""draft/ の下書きから全訳ファイルと note 用原稿4本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
N = 7
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, N + 1)}
body = "\n\n".join(p[i] for i in range(1, N + 1))

full = head.replace(head.split("\n", 1)[0], "# パラケルスス『事物の本性について』", 1) + "\n\n---\n\n" + body + "\n"
(D / "事物の本性について_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：パラケルススの名で伝わる De natura rerum（1537年の献辞をもつ）。英訳：A. E. Waite, The Hermetic and Alchemical Writings of Paracelsus, vol. 1, London: James Elliott and Co., 1894. 作業の基にした本文と扉：Internet Archive 所蔵の1894年英訳第一巻のスキャン
> 原著と英訳とは日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#パラケルスス #錬金術 #ホムンクルス #オカルト #神秘主義 #翻訳 #パブリックドメイン
"""

title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1, 2), "第一回には、第一の書「自然物の生成について」（腐敗、鳥の再生、想像による胎児の変形、バシリスク、ホムンクルスの製法、金属と宝石の生成）と、第二〜第四の書（成長、保存、命）を収めます。"),
    ("（二）", (3, 4), "第二回には、第五の書「自然物の死について」（金属・鉱物の殺しの処方）、第六の書「蘇生について」、第七の書「変成について」（変成の七つの段階、火の度合い、金属と宝石の変成）を収めます。"),
    ("（三）", (5, 6), "第三回には、第八の書「自然物の分離について」（人の二つの体の分離、金属・鉱物・植物・動物の分離、最後の審判）と、第九の書「徴について」の前半（人による徴、怪物の徴、人相）を収めます。"),
    ("（四・完）", (7,), "第四回には、第九の書の後半（手相、鉱物の徴と鉱山の閃光、金属の星、アダムの命名、占いの術の徴）と、ヴィンケルシュタインへの献辞などの長い英訳者の注を収めます。"),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/事物の本性について_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
