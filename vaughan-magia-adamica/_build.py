"""draft/ の下書きから全訳ファイルと note 用原稿（2本）を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
ch = [(D / f"draft/c{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 8)]

full = head.replace(head.split("\n", 1)[0], "# マギア・アダミカ", 1) + "\n\n---\n\n" + "\n\n".join(ch) + "\n"
(D / "マギア・アダミカ_全訳.md").write_text(full, encoding="utf-8")

title, rest = head.split("\n", 1)
parts = [
    ("前編", range(0, 4), "扉・献辞・読者への序と、本論の前半（魔術の定義、堕落による天と地との断絶、天使ラジエルの書、カインとアベルの犠牲、アダムの自然学、セトの系統と族長たちの術）を収める。"),
    ("後編", range(4, 7), "本論の後半（自然の魔術師モーセと金の子牛、まことのカバラと偽りのカバラ、ヤコブの梯子、ニコラ・フラメルとユダヤ人アブラハムの書、景教碑、エジプトの神学と碑、ギリシア・ローマからキリスト教世界への伝承）を収める。"),
]
tail = """---

## 出典

> 原著：Thomas Vaughan (Eugenius Philalethes), Magia Adamica: or the Antiquitie of Magic, London, 1650. 作業の基にした本文：A. E. Waite (ed.), The Magical Writings of Thomas Vaughan, London, 1888（Internet Archive 公開のスキャン）
> 本訳は、原著を全訳したものです。原著とウェイトの英訳は、日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#錬金術 #ヘルメス主義 #魔術 #カバラ #オカルト #翻訳 #パブリックドメイン
"""
for n, (sub, idx, summary) in enumerate(parts, 1):
    body = "\n\n".join(ch[i] for i in idx)
    note = (f"<!-- note投稿用（マギア・アダミカ_全訳.md から生成。2本に分けた。第{n}本） -->\n\n"
            f"{title} {sub}\n{rest}\n\n## この記事の内容\n\n　{summary}\n\n---\n\n{body}\n\n{tail}")
    (D / f"note用/マギア・アダミカ_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print("full", len(full))
