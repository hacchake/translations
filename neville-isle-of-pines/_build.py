"""draft/ の下書きから全訳ファイルと note 用原稿を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
body = "\n\n".join((D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 4))

full = head.replace(head.split("\n", 1)[0], "# パインズ島（ヘンリー・ネヴィル）", 1) + "\n\n---\n\n" + body + "\n"
(D / "パインズ島_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Henry Neville, The Isle of Pines, London, 1668. 作業の基にした本文：Project Gutenberg #21410（Worthington Chauncey Ford, The Isle of Pines, 1668: An Essay in Bibliography, Boston, 1920 所収）。扉図版も同書による
> 原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#ヘンリーネヴィル #パインズ島 #ユートピア #漂流記 #古典 #翻訳 #パブリックドメイン
"""

note = f"<!-- note投稿用（全訳から生成） -->\n\n{head}\n\n---\n\n{body}\n\n{tail}"
(D / "note用").mkdir(exist_ok=True)
(D / "note用/パインズ島_note.md").write_text(note, encoding="utf-8")
print(len(note), len(full))
