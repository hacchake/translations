"""draft/ の下書きから全訳ファイルと note 用原稿（2本）を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
ch = [(D / f"draft/e{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 9)]

full = head.replace(head.split("\n", 1)[0], "# ルーメン・デ・ルーミネ", 1) + "\n\n---\n\n" + "\n\n".join(ch) + "\n"
(D / "ルーメン・デ・ルーミネ_全訳.md").write_text(full, encoding="utf-8")

title, rest = head.split("\n", 1)
parts = [
    ("前編", range(0, 3), "扉・献辞・ボドリーへの詩・読者への序と、本論の前半（タリアとの出会いの夢物語、魔術の学校、学問の一致、天の印章の魔術、魔術の学校の図、薔薇十字団の書簡、図の解きあかし）を収める。"),
    ("後編", range(3, 8), "本論の後半（第一質料、哲学の火、真珠の川、エーテル、天の月、星の魂、ゾロアスターのプレステル、緑の塩、魔術の香、再生と上昇、下降と転生、結び）と、ラテン語の「魔術の箴言」を収める。"),
]
tail = """---

## 出典

> 原著：Thomas Vaughan (Eugenius Philalethes), Lumen de Lumine, London, 1651. 作業の基にした本文：Text Creation Partnership (EEBO-TCP) A64767（CC0）。図版：Wellcome Collection 所蔵本のスキャン（パブリックドメイン）
> 本訳は、原著を全訳したものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#錬金術 #薔薇十字 #魔術 #ヘルメス主義 #オカルト #翻訳 #パブリックドメイン
"""
for n, (sub, idx, summary) in enumerate(parts, 1):
    body = "\n\n".join(ch[i] for i in idx)
    note = (f"<!-- note投稿用（ルーメン・デ・ルーミネ_全訳.md から生成。2本に分けた。第{n}本。画像は ![](...) の行で示す） -->\n\n"
            f"{title} {sub}\n{rest}\n\n## この記事の内容\n\n　{summary}\n\n---\n\n{body}\n\n{tail}")
    (D / f"note用/ルーメン・デ・ルーミネ_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print("full", len(full))
