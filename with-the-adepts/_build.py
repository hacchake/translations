"""draft/ の下書きから全訳ファイルと note 用原稿2本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 9)}
body = "\n\n".join(p[i] for i in range(1, 9))

full = head.replace(head.split("\n", 1)[0], "# 熟達者たちとともに（フランツ・ハルトマン）", 1) + "\n\n---\n\n" + body + "\n"
(D / "熟達者たちとともに_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Franz Hartmann, With the Adepts: An Adventure among the Rosicrucians, Second Edition, Revised, The Theosophical Publishing Co., New York, 1910（初版 1887年）. 作業の基にした本文：Global Grey の電子版を Internet Archive 公開の1910年版のスキャンで確認
> 本訳は、原著を全訳したものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#薔薇十字団 #フランツハルトマン #錬金術 #神秘主義 #オカルト #翻訳 #パブリックドメイン
"""
title, rest = head.split("\n", 1)
parts = [
    ("前編", (1, 2, 3, 4), "前編には、序文と第一章「遠出」から第四章「食堂」までを収めます。語り手がアルプスの近づきがたい山の向こうの谷で薔薇十字の熟達者たちの僧院に迎えられ、インペラトールと語り、食堂で婦人の熟達者たちに会うところまでです。後編は第五章「前世の記憶」から終わりまでです。"),
    ("後編", (5, 6, 7, 8), "後編には、第五章「前世の記憶」、第六章「錬金術の実験室」、第七章「より高い生」、第八章「黒魔術」、第九章「終わり」、付録「スイスにおける薔薇十字の施設」と訳注を収めます。前編は序文から第四章までです。"),
]
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{rest}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/熟達者たちとともに_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
