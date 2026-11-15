"""draft/ の下書きから全訳ファイルと note 用原稿を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
body = "\n\n".join((D / f"draft/{n}.md").read_text(encoding="utf-8").strip()
                   for n in ("p0", "p1a", "p1b", "p2a", "p2b"))

full = head.replace(head.split("\n", 1)[0], "# 人間の不死と先在（J・M・E・マクタガート）", 1) + "\n\n---\n\n" + body + "\n"
(D / "人間の不死と先在_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：John McTaggart Ellis McTaggart, Human Immortality and Pre-Existence, Edward Arnold, London, 1916. 作業の基にした本文：Internet Archive 公開のスキャン
> 本訳は、原著を全訳したものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Fable 5.2）による翻訳であり、誤りを含む可能性があります。

#マクタガート #不死 #輪廻 #形而上学 #哲学 #翻訳 #パブリックドメイン
"""
note = f"<!-- note投稿用（全訳から生成） -->\n\n{head}\n\n---\n\n{body}\n\n{tail}"
(D / "note用").mkdir(exist_ok=True)
(D / "note用/人間の不死と先在_note.md").write_text(note, encoding="utf-8")
print(len(note), len(full))
