"""draft/ の下書きから全訳ファイルと note 用原稿（3本）を生成する。"""
import pathlib, re

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
ch = [(D / f"draft/p{i:02d}.md").read_text(encoding="utf-8").strip() for i in range(19)]

# 全訳
full = head + "\n\n---\n\n" + "\n\n---\n\n".join(ch) + "\n"
(D / "数_全訳.md").write_text(full, encoding="utf-8")

# note 用：表を箇条書きに
title, rest = head.split("\n", 1)
meta_rows = re.findall(r"^\| (?!項目|---)(.+?) \| (.+?) \|$", rest, re.M)
meta = "\n".join(f"- {k}：{v}" for k, v in meta_rows)
about = re.search(r"## この本について\n\n(.*?)\n\n## 目次", rest, re.S).group(1)
toc = re.search(r"## 目次\n\n(.*)", rest, re.S).group(1).replace("  - ", "- 　")

parts = [
    ("前編　序・第一〜三部・一から四まで", range(0, 9),
     "本書の前半。三つの序、ピタゴラスの生涯と学派、偶数・奇数・完全数・友愛数などのピタゴラス派の数の分類、ヘブライ文字を数として読むカバラの技法（ゲマトリア、ノタリコン、テムラ）と惑星の魔方陣、そして一から四までの数（三・五を含む）の伝承を収める。"),
    ("中編　五から十まで", range(9, 15),
     "本書の中ほど。五（五芒星、第五元素）、六（ダビデの盾、六百年の周期ナロス）、七（七つの惑星、人間の七つの原理、七不思議）、八、九（九つの天使の階級、エレウシスの秘儀）、十（十のセフィロト、薔薇十字協会の十の位階）の伝承を収める。"),
    ("後編　十一から黙示録の数まで", range(15, 19),
     "本書の後半。不吉な数とされた十一、黄道十二宮にまつわる十二、マヤの暦と十三、数のヒンドゥーの用法、十四から二万五千に至る「そのほかの大きな数」（ゲマトリアの値、薔薇十字の年代、ボーデの法則など）、そしてヨハネの黙示録に出てくる数の一覧を収める。"),
]
tail = """---

## 出典

> 原著：W. Wynn Westcott, Numbers: Their Occult Power and Mystic Virtues, 3rd edition, Theosophical Publishing Society, London and Benares, 1911. 作業の基にした本文：Sacred Texts Archive の電子テキスト
> 本訳は、原著を全訳したものです。著者は1925年に死去し、原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#数秘術 #カバラ #ピタゴラス #黄金の夜明け団 #オカルト #翻訳 #パブリックドメイン
"""
for n, (sub, idx, summary) in enumerate(parts, 1):
    body = "\n\n---\n\n".join(ch[i] for i in idx)
    note = (f"<!-- note投稿用（数_全訳.md から生成。表を箇条書きにし、3本に分けた。第{n}本） -->\n\n"
            f"# 【全訳】ウィン・ウェストコット『数――その隠秘の力と神秘の徳』{sub}\n\n"
            f"W・ウィン・ウェストコット（W. Wynn Westcott）著／全訳\n\n{meta}\n\n"
            f"## この本について\n\n{about}\n\n## この記事の内容\n\n　{summary}\n\n"
            f"## 全体の目次\n\n{toc}\n\n---\n\n{body}\n\n{tail}")
    (D / f"note用/数_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print("full", len(full))
