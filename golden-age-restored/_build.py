"""draft/ の下書きから全訳ファイルと note 用原稿を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
body = (D / "draft/n1.md").read_text(encoding="utf-8").strip()

full = head.replace(head.split("\n", 1)[0], "# 黄金時代の復活（ヘンリクス・マダタヌス）", 1) + "\n\n---\n\n" + body + "\n"
(D / "黄金時代の復活_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原典：Henricus Madathanus (Adrian von Mynsicht), Aureum Seculum Redivivum (1625; Musaeum Hermeticum, Frankfurt, 1678)。英訳：A. E. Waite, The Hermetic Museum, Restored and Enlarged, vol. 1, London: James Elliott, 1893. 作業の基にした本文と扉：Internet Archive 所蔵の1893年英訳第一巻のスキャン
> 原典と英訳とは日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#錬金術 #賢者の石 #薔薇十字 #雅歌 #オカルト #翻訳 #パブリックドメイン
"""

note = f"<!-- note投稿用（全訳から生成） -->\n\n{head}\n\n---\n\n{body}\n\n{tail}"
(D / "note用").mkdir(exist_ok=True)
(D / "note用/黄金時代の復活_note.md").write_text(note, encoding="utf-8")
print(len(note), len(full))
