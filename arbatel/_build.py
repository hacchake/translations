"""draft/ の下書きから全訳ファイルと note 用原稿を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
ch = [(D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in (1, 2)]
body = "\n\n".join(ch)

full = head.replace(head.split("\n", 1)[0], "# アルバテル――古代人の魔術について", 1) + "\n\n---\n\n" + body + "\n"
(D / "アルバテル_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Arbatel De magia veterum (Basel, 1575). 英訳：Robert Turner, "Arbatel of Magick", in Henry Cornelius Agrippa his Fourth Book of Occult Philosophy, London, 1655. 作業の基にした本文と印章：Internet Archive 公開のスキャン
> 本訳は、原著を全訳したものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による英訳からの翻訳であり、誤りを含む可能性があります。

#アルバテル #魔術書 #グリモワール #オリンポスの霊 #オカルト #翻訳 #パブリックドメイン
"""
note = "<!-- note投稿用（アルバテル_全訳.md から生成） -->\n\n" + head + "\n\n---\n\n" + body + "\n\n" + tail
(D / "note用/アルバテル_note.md").write_text(note, encoding="utf-8")
print(len(full), len(note))
