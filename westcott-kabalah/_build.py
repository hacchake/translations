"""draft/ の下書きから全訳ファイルと note 用原稿を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
ch = [(D / f"draft/d{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 5)]
body = "\n\n---\n\n".join(ch)

full = head.replace("# 【全訳】ウィン・ウェストコット『カバラ研究入門』", "# カバラ研究入門", 1) + "\n\n---\n\n" + body + "\n"
(D / "カバラ研究入門_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：W. Wynn Westcott, An Introduction to the Study of the Kabalah, J. M. Watkins, London, 1910. 作業の基にした本文：Global Grey 公開の電子書籍
> 本訳は、原著を全訳したものです。著者は1925年に死去し、原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#カバラ #生命の木 #黄金の夜明け団 #ウェストコット #オカルト #翻訳 #パブリックドメイン
"""
note = ("<!-- note投稿用（カバラ研究入門_全訳.md から生成） -->\n\n" + head + "\n\n---\n\n" + body + "\n\n" + tail)
(D / "note用/カバラ研究入門_note.md").write_text(note, encoding="utf-8")
print(len(full), len(note))
