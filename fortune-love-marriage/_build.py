"""draft/ の下書きから全訳ファイルと note 用原稿を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
body = "\n\n".join((D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 12))

full = head.replace(head.split("\n", 1)[0], "# 愛と結婚の秘教哲学（ダイアン・フォーチュン）", 1) + "\n\n---\n\n" + body + "\n"
(D / "愛と結婚の秘教哲学_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Dion Fortune, The Esoteric Philosophy of Love and Marriage, Rider, London, 1924. 作業の基にした本文：第四版（1967年。Aquarian Press のペーパーバック）のスキャン
> 本訳は、原著を全訳したものです（底本で欠けていた原書86ページを除く）。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#ダイアンフォーチュン #秘教 #西洋魔術 #神秘主義 #オカルト #翻訳 #パブリックドメイン
"""
note = f"<!-- note投稿用（全訳から生成） -->\n\n{head}\n\n---\n\n{body}\n\n{tail}"
(D / "note用").mkdir(exist_ok=True)
(D / "note用/愛と結婚の秘教哲学_note.md").write_text(note, encoding="utf-8")
print(len(note), len(full))
