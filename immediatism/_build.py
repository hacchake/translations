"""draft/ の下書きから全訳ファイルと note 用原稿3本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
N = 3
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, N + 1)}
body = "\n\n".join(p[i] for i in range(1, N + 1))

title, rest = head.split("\n", 1)
full = "# ハキム・ベイ『イミディアティズム』" + rest + "\n\n---\n\n" + body + "\n"
(D / "イミディアティズム_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Hakim Bey, Immediatism, Edinburgh / San Francisco: AK Press, 1994（初出：Radio Sermonettes, New York: Libertarian Book Club, 1992）。作業の基にした本文：Internet Archive 所蔵の1994年版のスキャンと、The Anarchist Library 所収のテキスト
> 原著には「アンチコピーライト、1994年。自由に海賊版をつくり、引用してよい」という表示があり、この翻訳はその表示にもとづいています。訳文も同じ条件で自由に複製・引用できます。訳文は人工知能（Claude Fable 5.2）による翻訳であり、誤りを含む可能性があります。

#ハキムベイ #イミディアティズム #TAZ #アナキズム #オカルト #翻訳 #アンチコピーライト
"""

short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", "第一回には、1994年版の序文「存在論的アナーキー早わかり」、表題作「イミディアティズム」、そして「トン（堂）」を収めます。カオスと欲望から出発する著者の立場のあらまし、媒介を抜いた遊びをひそかに実践しようという十七項目の宣言、中国の秘密結社を手本にした集まり方の提案です。"),
    ("（二）", "第二回には、「イミディアティズム対資本主義」「インヴォリューション」「想像力」の三編を収めます。友人と集まることを妨げる三つの怪物（忙しさ、成功、弾圧）、メディアが人を自分のなかへ巻きこんで孤立させる仕組み、想像力の分かちあいから見た演劇・映画・本・ラジオ・テレビの序列を論じます。"),
    ("（三・完）", "第三回には、「ラスコー」「ヴェルニサージュ」「ロー・ヴィジョン」「イミディアティストのポトラッチ」「沈黙」「聴き手の批判」の六編を収めます。旧石器時代の回帰、笑いで社会を壊しそこねた芸術、アウトサイダー・アートの扱い方、手づくりの贈り物を持ちよる宴の遊び方、そして語ることと書くことそのものへの疑いが語られます。"),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, summ) in enumerate(parts, 1):
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{p[n]}\n\n{tail}"
    (D / f"note用/イミディアティズム_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
