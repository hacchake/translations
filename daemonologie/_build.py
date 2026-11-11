"""draft/ の下書きから全訳ファイルと note 用原稿4本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
N = 4
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, N + 1)}
body = "\n\n".join(p[i] for i in range(1, N + 1))

full = head.replace(head.split("\n", 1)[0], "# ジェームズ王『悪魔学』（付録『スコットランドからの知らせ』）", 1) + "\n\n---\n\n" + body + "\n"
(D / "悪魔学_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：James VI, Daemonologie, In Forme of a Dialogue, Edinburgh: Robert Walde-graue, 1597. 付録：Newes from Scotland, London: William Wright, 1591. 作業の基にした本文：Project Gutenberg 第25929番。扉：Internet Archive 所蔵の1597年版のスキャン。木版画：同グーテンベルク版の図版
> 原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#悪魔学 #魔女 #魔女狩り #ジェームズ1世 #オカルト #翻訳 #パブリックドメイン
"""

title, rest = head.split("\n", 1)
short = rest.split("\n## この本について")[0]
parts = [
    ("（一）", (1,), "第一回には、王自身による序文と、第一書（全七章）を収めます。魔女術が存在することを聖書によって論じたあと、魔術と降霊術の語源、悪魔の「学校」としての占星術と「手ほどき」としての民間のまじない、円陣と呪文による悪魔の呼び出し、悪魔と魔術師との契約、魔術師への罰を扱います。"),
    ("（二）", (2,), "第二回には、第二書（全七章）を収めます。魔女はどのようにして悪魔の弟子になるのか、教会での集会と悪魔の礼拝、篩に乗った海渡りや霊の飛行はほんとうか幻か、蠟人形による呪殺や嵐を起こす力、魔女に男より女が多いわけ、牢のなかの魔女と悪魔、教皇主義の時代と比べて魔女が増えたわけを論じます。"),
    ("（三）", (3,), "第三回には、第三書（全六章）を収めます。家に出る幽霊、レイス（死の前ぶれの幻）、人狼、ブラウニー、インクブスとスックブス（夢魔）、悪霊つきとその見分け方、妖精の王と女王の話を取りあげ、最後に、魔女の審理と処罰（悪魔のしるし、水に浮くかどうかの試し）を論じて対話を結びます。"),
    ("（四・完）", (4,), "第四回には、付録として、ジェームズ王が取り調べに立ち会ったノース・バーウィックの魔女裁判を伝える小冊子『スコットランドからの知らせ』（1591年）を、木版画とともに収めます。篩で海を渡って教会で悪魔を拝んだという自白、洗礼を施した猫で嵐を起こしたという話、そして拷問の末に火刑に処せられた学校教師フィアン博士の顛末が語られます。"),
]
(D / "note用").mkdir(exist_ok=True)
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    h = rest if n == 1 else short
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{h}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/悪魔学_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
