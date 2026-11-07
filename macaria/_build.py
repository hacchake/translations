"""draft/ の下書きから全訳ファイルと note 用原稿を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
body = (D / "draft/n1.md").read_text(encoding="utf-8").strip()

full = head.replace(head.split("\n", 1)[0], "# 名高きマカリア王国の記（ガブリエル・プラッツ）", 1) + "\n\n---\n\n" + body + "\n"
(D / "マカリア王国の記_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：[Gabriel Plattes,] A Description of the Famous Kingdome of Macaria, London: Francis Constable, 1641. 作業の基にした本文：Project Gutenberg 第55269番
> 原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#ユートピア #マカリア #ピューリタン革命 #ハートリブ #古典 #翻訳 #パブリックドメイン
"""

note = f"<!-- note投稿用（全訳から生成） -->\n\n{head}\n\n---\n\n{body}\n\n{tail}"
(D / "note用").mkdir(exist_ok=True)
(D / "note用/マカリア王国の記_note.md").write_text(note, encoding="utf-8")
print(len(note), len(full))
