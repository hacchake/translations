"""draft/ の下書きから全訳ファイルと note 用原稿を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
ch = [(D / f"draft/k{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 5)]
body = "\n\n".join(ch)

full = head.replace(head.split("\n", 1)[0], "# アエシュ・メツァレフ（浄化の火）", 1) + "\n\n---\n\n" + body + "\n"
(D / "アエシュ・メツァレフ_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Aesch Mezareph or Purifying Fire, translated by a Lover of Philalethes (1714); preface and notes by "Sapere Aude" (W. Wynn Westcott), Collectanea Hermetica Vol. IV, London, 1894. 作業の基にした本文：Internet Archive 公開のスキャン
> 本訳は、原著を全訳したものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#カバラ #錬金術 #ゲマトリア #黄金の夜明け団 #オカルト #翻訳 #パブリックドメイン
"""
note = "<!-- note投稿用（アエシュ・メツァレフ_全訳.md から生成） -->\n\n" + head + "\n\n---\n\n" + body + "\n\n" + tail
(D / "note用/アエシュ・メツァレフ_note.md").write_text(note, encoding="utf-8")
print(len(full), len(note))
