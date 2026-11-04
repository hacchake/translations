"""draft/ の下書きから全訳ファイルと note 用原稿を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
ch = [(D / f"draft/b{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 6)]
body = "\n\n".join(ch)

full = head.replace(head.split("\n", 1)[0], "# アニマ・マギカ・アブスコンディタ", 1) + "\n\n---\n\n" + body + "\n"
(D / "アニマ・マギカ・アブスコンディタ_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Thomas Vaughan (Eugenius Philalethes), Anima Magica Abscondita, London, 1650. 作業の基にした本文：A. E. Waite (ed.), The Magical Writings of Thomas Vaughan, London, 1888（Internet Archive 公開のスキャン）
> 本訳は、原著を全訳したものです。原著とウェイトの英訳は、日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#錬金術 #ヘルメス主義 #魔術 #薔薇十字 #オカルト #翻訳 #パブリックドメイン
"""
note = "<!-- note投稿用（アニマ・マギカ・アブスコンディタ_全訳.md から生成） -->\n\n" + head + "\n\n---\n\n" + body + "\n\n" + tail
(D / "note用/アニマ・マギカ・アブスコンディタ_note.md").write_text(note, encoding="utf-8")
print(len(full), len(note))
