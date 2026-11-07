"""draft/ の下書きから全訳ファイルと note 用原稿2本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 7)}
body = "\n\n".join(p[i] for i in range(1, 7))

full = head.replace(head.split("\n", 1)[0], "# エジプト魔術（フローレンス・ファー）", 1) + "\n\n---\n\n" + body + "\n"
(D / "エジプト魔術_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：S. S. D. D. (Florence Farr), Egyptian Magic, Collectanea Hermetica vol. VIII, ed. W. Wynn Westcott, London: Theosophical Publishing Society, 1896. 作業の基にした本文と図版：Internet Archive 所蔵の1896年初版のスキャン
> 原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#フローレンスファー #エジプト魔術 #黄金の夜明け団 #グノーシス #オカルト #翻訳 #パブリックドメイン
"""

def table_to_list(s):
    # note は表を表示できないので箇条書きにする
    out = []
    for l in s.split("\n"):
        if l.startswith("|"):
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            if c[0].startswith("決定詞") or set(c[0]) <= set("-"):
                continue
            out.append(f"- {c[0]}＝{c[1]}：{c[2]}")
        else:
            out.append(l)
    return "\n".join(out)


title, rest = head.split("\n", 1)
parts = [
    ("（一）", (1, 2, 3), "第一回には、口絵「人間の諸部分」と、本文の前半――エジプト魔術の原理、『死者の書』第六十四章、ハリス魔術パピルス、超自然の出現の理論、ラーとイシスの伝説、物語に見える魔術の例、王と神々への讃歌――を収めます。"),
    ("（二・完）", (4, 5, 6), "第二回には、本文の後半――エジプトのグノーシスの魔術と、ブルース写本からの抜粋（プレーローマの深淵とアイオーンたち、三つの洗礼とその印章、大いなる名）、そして結び――を収めます。"),
]
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = table_to_list("\n\n".join(p[i] for i in rng))
    h = rest if n == 1 else rest.split("\n## この本について")[0]
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/エジプト魔術_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
