"""draft/ の下書きから全訳ファイルと note 用原稿3本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
N = 5
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, N + 1)}
body = "\n\n".join(p[i] for i in range(1, N + 1))

full = head.replace(head.split("\n", 1)[0], "# C・G・リーランド『アラディア、あるいは魔女の福音』", 1) + "\n\n---\n\n" + body + "\n"
(D / "アラディア_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Charles Godfrey Leland, Aradia, or the Gospel of the Witches, London: David Nutt, 1899. 作業の基にした本文：Internet Sacred Text Archive（sacred-texts.com）公開の1899年版の翻刻。扉：Internet Archive 所蔵の1899年版のスキャン
> 原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Fable 5.2）による翻訳であり、誤りを含む可能性があります。

#アラディア #魔女 #魔術 #ウィッカ #オカルト #翻訳 #パブリックドメイン
"""

title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1, 2), "第一回には、序と、福音の本体である第一章から第三章（アラディアの誕生と使命、魔女の晩餐の呪文、ディアーナによる星と雨との創造）、そして実用のまじないを集めた第四章から第八章（穴のあいた石と丸い石、レモンと針、恋を得るまじない、掘り出しものを得る祈り、葡萄酒のまじない）を収めます。"),
    ("（二）", (3, 4), "第二回には、物語を中心とする第九章から第十五章（ターナとエンダモーネ、マドンナ・ディアーナ、風の家、月の女神ターナ、ディアーナと子どもたち、小鬼の使者、盗人の女神ラヴェルナ）を収めます。"),
    ("（三・完）", (5,), "第三回には、リーランド自身による付録「以上の本文についての注解」（福音の入手の経緯、魔術を虐げられた者の反逆と見る説、女性原理の創造神話）と、追加の物語三篇（ディアーナの子ら、蛇の女王ディアーナ、美しさを授けるディアーナ）、付記を収めます。"),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/アラディア_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
