"""draft/ の下書きから全訳ファイルと note 用原稿を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
body = "\n\n".join((D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in (1, 2))

full = head.replace(head.split("\n", 1)[0], "# 錬金術の秘密についての精妙な寓意（マイアー）", 1) + "\n\n---\n\n" + body + "\n"
(D / "精妙な寓意_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原典：Michael Maier, Subtilis Allegoria super Secreta Chymiae（Musaeum Hermeticum, Frankfurt, 1678 所収）。英訳：A. E. Waite, The Hermetic Museum, Restored and Enlarged, vol. 2, London: James Elliott, 1893. 作業の基にした本文と扉：Internet Archive 所蔵の1893年英訳第二巻のスキャン
> 原典と英訳とは日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#錬金術 #フェニックス #ミヒャエルマイアー #薔薇十字 #オカルト #翻訳 #パブリックドメイン
"""

note = f"<!-- note投稿用（全訳から生成） -->\n\n{head}\n\n---\n\n{body}\n\n{tail}"
(D / "note用").mkdir(exist_ok=True)
(D / "note用/精妙な寓意_note.md").write_text(note, encoding="utf-8")
print(len(note), len(full))
