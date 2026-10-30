"""draft/ の下書きから全訳ファイルと note 用原稿（3本）を生成する。"""
import pathlib, re

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
ch = [(D / f"draft/c{i:02d}.md").read_text(encoding="utf-8").strip() for i in range(1, 20)]

# 全訳
full = head + "\n\n---\n\n" + "\n\n---\n\n".join(ch) + "\n"
(D / "健全なオカルティズム_全訳.md").write_text(full, encoding="utf-8")

# note 用：表を箇条書きに
title, rest = head.split("\n", 1)
meta_rows = re.findall(r"^\| (?!項目|---)(.+?) \| (.+?) \|$", rest, re.M)
meta = "\n".join(f"- {k}：{v}" for k, v in meta_rows)
about = re.search(r"## この本について\n\n(.*?)\n\n## 目次", rest, re.S).group(1)
toc = re.search(r"## 目次\n\n(.*)", rest, re.S).group(1)

parts = [
    ("前編　第一〜七章", range(0, 7),
     "本書の前半。オカルティズムとは何か、それはやりがいのあるものか、という問いからはじめ、軽信を避けるための証拠の扱い方、精神分析の自由連想による幻視の吟味、瞑想による探究と照らしあわせの方法、占星術の正しい用いかた、前世の記録の読み方と、その見せかけを見ぬく手がかりを語る。"),
    ("中編　第八〜十三章", range(7, 13),
     "本書の中ほど。数秘術とピラミッド予言、黙示録の獣の数の解釈を批判し、オカルト団体の集団の心とカルマ、教師の権威と弟子の服従、兄弟団の秘密主義の理由を論じる。さらに、薬物や催眠を用いる左手の道、性の力を悪用する当時のオカルト団体への告発に及ぶ。"),
    ("後編　第十四〜十九章", range(13, 19),
     "本書の後半。霊能者の過敏さと交感〔ラポール〕の病理、本人の同意なく他人の心にはたらきかける「心の不法侵入」、菜食主義とオカルトの訓練、東洋の方法を西洋人が用いることの是非、教師と学派を判断する基準を論じ、最後にオカルティズムの理想と、イニシエートの仕事のさまざまな部門を描いて結ぶ。"),
]
tail = """---

## 出典

> 原著：Dion Fortune, Sane Occultism, Rider, London, 1929. 作業の基にした本文：Global Grey 公開の電子書籍
> 本訳は、原著を全訳したものです。著者は1946年に死去し、原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#ダイアン・フォーチュン #オカルト #秘教 #神秘主義 #魔術 #翻訳 #パブリックドメイン
"""
for n, (sub, idx, summary) in enumerate(parts, 1):
    body = "\n\n---\n\n".join(ch[i] for i in idx)
    note = (f"<!-- note投稿用（健全なオカルティズム_全訳.md から生成。表を箇条書きにし、3本に分けた。第{n}本） -->\n\n"
            f"# 【全訳】ダイアン・フォーチュン『健全なオカルティズム』{sub}\n\n"
            f"ダイアン・フォーチュン（Dion Fortune）著／全訳\n\n{meta}\n\n"
            f"## この本について\n\n{about}\n\n## この記事の内容\n\n　{summary}\n\n"
            f"## 全体の目次\n\n{toc}\n\n---\n\n{body}\n\n{tail}")
    (D / f"note用/健全なオカルティズム_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print("full", len(full))
