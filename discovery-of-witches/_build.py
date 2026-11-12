"""draft/ の下書きから全訳ファイルと note 用原稿を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
body = (D / "draft/n1.md").read_text(encoding="utf-8").strip()

title, rest = head.split("\n", 1)
full = "# マシュー・ホプキンス『魔女の発見』" + rest + "\n\n---\n\n" + body + "\n"
(D / "魔女の発見_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Matthew Hopkins, The Discovery of Witches, London: R. Royston, 1647. 作業の基にした本文：Wikisource 所収の1928年復刻版（London: The Cayme Press）のうち1647年の本文。扉：同書所載の1647年版の写真。口絵：1647年版の木版画（Wikimedia Commons）
> 原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Fable 5.2）による翻訳であり、誤りを含む可能性があります。

#魔女の発見 #魔女 #魔女狩り #ホプキンス #オカルト #翻訳 #パブリックドメイン
"""
(D / "note用").mkdir(exist_ok=True)
note = f"<!-- note投稿用（全訳から生成） -->\n\n{title}\n{rest}\n\n---\n\n{body}\n\n{tail}"
(D / "note用/魔女の発見_note.md").write_text(note, encoding="utf-8")
print(len(note), len(full))
