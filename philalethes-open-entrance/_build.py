"""draft/ の下書きから全訳ファイルと note 用原稿を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
body = "\n\n".join((D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 6))

full = head.replace(head.split("\n", 1)[0], "# 王の閉ざされた宮殿への開かれた入口（エイレナエウス・フィラレテス）", 1) + "\n\n---\n\n" + body + "\n"
(D / "開かれた入口_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Eirenaeus Philalethes, Introitus apertus ad occlusum regis palatium, Amsterdam, 1667. 作業の基にした本文：Global Grey の電子版（英訳 An Open Entrance to the Closed Palace of the King）。扉：Internet Archive 所蔵の1667年版
> 原著と英訳とは日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#フィラレテス #錬金術 #賢者の石 #神秘主義 #オカルト #翻訳 #パブリックドメイン
"""

note = f"<!-- note投稿用（全訳から生成） -->\n\n{head}\n\n---\n\n{body}\n\n{tail}"
(D / "note用").mkdir(exist_ok=True)
(D / "note用/開かれた入口_note.md").write_text(note, encoding="utf-8")
print(len(note), len(full))
