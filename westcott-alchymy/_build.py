"""draft/ の下書きから全訳ファイルと note 用原稿1本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
body = (D / "draft/n1.md").read_text(encoding="utf-8").strip()

full = head.replace(head.split("\n", 1)[0], "# 錬金術の学（ウェストコット）", 1) + "\n\n---\n\n" + body + "\n"
(D / "錬金術の学_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著："Sapere Aude" (W. Wynn Westcott), The Science of Alchymy, Spiritual and Material, Theosophical Publishing Society, London, 1893. 作業の基にした本文：Internet Archive 公開のウェルカム図書館所蔵本のスキャン
> 本訳は、原著を全訳したものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#錬金術 #ウェストコット #黄金の夜明け団 #神秘主義 #オカルト #翻訳 #パブリックドメイン
"""
note = f"<!-- note投稿用（全訳から生成） -->\n\n{head}\n\n---\n\n{body}\n\n{tail}"
(D / "note用/錬金術の学_note.md").write_text(note, encoding="utf-8")
print(len(note), len(full))
