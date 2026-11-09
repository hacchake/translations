"""draft/ の下書きから全訳ファイルと note 用原稿1本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
body = "\n\n".join((D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 3))

full = head.replace(head.split("\n", 1)[0], "# パラケルスス『惑星の霊について』", 1) + "\n\n---\n\n" + body + "\n"
(D / "惑星の霊について_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：パラケルススの名で伝わる De spiritibus planetarum（1570年バーゼル八折版など）。英訳：A. E. Waite, The Hermetic and Alchemical Writings of Paracelsus, vol. 1, London: James Elliott and Co., 1894. 作業の基にした本文と扉：Internet Archive 所蔵の1894年英訳第一巻のスキャン
> 原著と英訳とは日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#パラケルスス #錬金術 #賢者の石 #占星術 #オカルト #翻訳 #パブリックドメイン
"""

note = f"<!-- note投稿用（全訳から生成） -->\n\n{head}\n\n---\n\n{body}\n\n{tail}"
(D / "note用").mkdir(exist_ok=True)
(D / "note用/惑星の霊について_note.md").write_text(note, encoding="utf-8")
print(len(note), len(full))
