"""draft/ の下書きから全訳ファイルと note 用原稿を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
ch = [(D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 4)]
body = "\n\n".join(ch)

full = head.replace(head.split("\n", 1)[0], "# ゾロアスターのカルデア神託", 1) + "\n\n---\n\n" + body + "\n"
(D / "カルデア神託_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：The Chaldaean Oracles of Zoroaster, edited and revised by "Sapere Aude" (W. Wynn Westcott), with an introduction by L. O., Collectanea Hermetica Vol. VI, London, 1895. 作業の基にした本文：Internet Archive 公開のスキャン
> 本訳は、原著を全訳したものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による英訳からの翻訳であり、誤りを含む可能性があります。

#カルデア神託 #新プラトン主義 #ゾロアスター #黄金の夜明け団 #オカルト #翻訳 #パブリックドメイン
"""
note = "<!-- note投稿用（カルデア神託_全訳.md から生成） -->\n\n" + head + "\n\n---\n\n" + body + "\n\n" + tail
(D / "note用/カルデア神託_note.md").write_text(note, encoding="utf-8")
print(len(full), len(note))
