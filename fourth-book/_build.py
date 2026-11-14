"""draft/ の下書きから全訳ファイルと note 用原稿4本を生成する。

draft/n0.md  扉・ターナーの序文・献詩
draft/n1.md  アグリッパ「ジオマンシーについて」
draft/n2.md  アグリッパ『オカルト哲学第四の書』
draft/n3.md  ピクトリウス「イサゴーゲー」
draft/n4.md  ゲラルドゥス「天文的ジオマンシー」
draft/head_*.md  note 記事ごとの冒頭（書誌と解説）
"""
import pathlib

D = pathlib.Path(__file__).parent
r = lambda p: (D / p).read_text(encoding="utf-8").strip()

n = {i: r(f"draft/n{i}.md") for i in range(5)}

intro = """# 『アグリッパのオカルト哲学第四の書』ほか（ロバート・ターナー英訳、1655年）　全訳

ロバート・ターナーが1655年にロンドンで刊行した英訳本のうち、扉、ターナーの序文と献詩、および「ジオマンシーについて」「オカルト哲学第四の書」「イサゴーゲー（霊の本性について）」「天文的ジオマンシー」の4篇の全訳。同じ本に収められた「ヘプタメロン」と「アルバテル」は、それぞれ `heptameron/` と `arbatel/` に訳してある。作業の記録は `第四の書_作業メモ.md` にある。

---"""
full = "\n\n".join([intro, n[0], "---", n[1], "---", n[2], "---", n[3], "---", n[4]]) + "\n"
(D / "第四の書ほか_全訳.md").write_text(full, encoding="utf-8")

SRC = ("作業の基にした本文と図版：Internet Archive 公開のスキャン（cu31924006718757、"
       "コーネル大学図書館蔵の1655年版の複製本）")
TAIL = "原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による英訳からの翻訳であり、誤りを含む可能性があります。"

notes = [
    ("第四の書", "head_fourth.md", [n[0], n[2]],
     "Henry Cornelius Agrippa (attrib.), Of Occult Philosophy, or Of Magical Ceremonies: The Fourth Book, transl. Robert Turner, London, 1655",
     "#アグリッパ #オカルト哲学 #魔術書 #グリモワール #オカルト #翻訳 #パブリックドメイン"),
    ("ジオマンシーについて", "head_geomancy.md", [n[1]],
     "Henry Cornelius Agrippa (attrib.), Of Geomancy, transl. Robert Turner, London, 1655",
     "#アグリッパ #ジオマンシー #土占い #占い #オカルト #翻訳 #パブリックドメイン"),
    ("イサゴーゲー", "head_isagoge.md", [n[3]],
     "Georg Pictorius, Isagoge, or Of the Nature of Spirits, transl. Robert Turner, London, 1655",
     "#ピクトリウス #悪魔学 #霊 #オカルト #ルネサンス #翻訳 #パブリックドメイン"),
    ("天文的ジオマンシー", "head_astro.md", [n[4]],
     "Gerard of Cremona (attrib.), Of Astronomical Geomancy, transl. Robert Turner, London, 1655",
     "#ジオマンシー #占星術 #ホラリー占星術 #占い #オカルト #翻訳 #パブリックドメイン"),
]
for name, head, bodies, orig, tags in notes:
    body = "\n\n---\n\n".join(bodies)
    tail = f"---\n\n## 出典\n\n> 原著：{orig}. {SRC}\n> {TAIL}\n\n{tags}\n"
    text = (f"<!-- note投稿用（第四の書ほか_全訳.md から生成） -->\n\n"
            + r(f"draft/{head}") + "\n\n---\n\n" + body + "\n\n" + tail)
    (D / f"note用/{name}_note.md").write_text(text, encoding="utf-8")
    print(name, len(text))
print("全訳", len(full))
