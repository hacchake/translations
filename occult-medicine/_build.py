"""draft/ の下書きから全訳ファイルと note 用原稿2本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(5)}
body = "\n\n".join(p[i] for i in range(5))

full = head.replace(head.split("\n", 1)[0], "# 医学における隠秘学（フランツ・ハルトマン）", 1) + "\n\n---\n\n" + body + "\n"
(D / "医学における隠秘学_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Franz Hartmann, Occult Science in Medicine, Theosophical Publishing Society, London, 1893. 作業の基にした本文：Internet Archive 公開のスキャン
> 本訳は、原著を全訳したものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#パラケルスス #神智学 #オカルト医学 #錬金術 #オカルト #翻訳 #パブリックドメイン
"""
title, rest = head.split("\n", 1)
parts = [
    ("前編", (0, 1, 2), "前編には、序文、序論、第一章「人の構成」、第二章「医学の四本の柱」（哲学・天文学・錬金術・医師の徳）を収めます。後編は第三章「病気の五つの原因」から第五章「未来の医師」までです。"),
    ("後編", (3, 4), "後編には、第三章「病気の五つの原因」、第四章「医師の五つの類」、第五章「未来の医師」と訳注を収めます。前編は序文から第二章までです。"),
]
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{rest}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/医学における隠秘学_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
