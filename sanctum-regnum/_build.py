"""draft/ の下書きから全訳ファイルと note 用原稿2本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in (1, 2)}
body = p[1] + "\n\n" + p[2]

full = head.replace(head.split("\n", 1)[0], "# 聖王国の魔術儀式――タロットの切り札による解釈（エリファス・レヴィ）", 1) + "\n\n---\n\n" + body + "\n"
(D / "聖王国の魔術儀式_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：The Magical Ritual of the Sanctum Regnum, interpreted by the Tarot Trumps, translated from the MSS. of Éliphaz Lévi and edited by W. Wynn Westcott, George Redway, London, 1896. 作業の基にした本文と図版：Internet Archive 公開のスキャン
> 本訳は、原著を全訳したものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による英訳からの翻訳であり、誤りを含む可能性があります。

#エリファスレヴィ #タロット #魔術 #カバラ #黄金の夜明け団 #翻訳 #パブリックドメイン
"""
title, rest = head.split("\n", 1)
parts = [
    ("前編", 1, "前編には、扉と編者の序、第一章「魔術師」から第十一章「力」までを収めます（図版七枚）。後編は第十二章「吊るされた男」から最後の格言までです。"),
    ("後編", 2, "後編には、第十二章「吊るされた男」から第二十二章「宇宙」（カバラーの祈りと四・七・三の呼び出し）、編者の注、レヴィの結び、オカルトと宗教の格言を収めます。前編は序と第一章〜第十一章です。"),
]
for n, (sub, k, summ) in enumerate(parts, 1):
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{rest}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{p[k]}\n\n{tail}"
    (D / f"note用/聖王国の魔術儀式_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
