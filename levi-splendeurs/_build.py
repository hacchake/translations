"""draft/ の下書きから全訳ファイルと note 用原稿5本を生成する。

draft/l00.md        序文
draft/l01〜l03.md   第一部　イドラ・ズータ
draft/l05.md        第二部　キリスト教の栄光（クリシュナの伝説を含む）
draft/l06〜l07.md   第三部　燃える星
draft/l08.md        信仰告白
draft/l09〜l10.md   カバラーの要素――十講
draft/l11〜l13.md   付録　パピュ「エリファス・レヴィの教え」
draft/head_*.md     note 記事ごとの冒頭（書誌と解説）
"""
import pathlib

D = pathlib.Path(__file__).parent
r = lambda p: (D / p).read_text(encoding="utf-8").strip()
L = lambda *ns: "\n\n".join(r(f"draft/l{n:02d}.md") for n in ns)

# 1行ずつ並べた箇所（列挙・連禱など）は、note で1段落にまとまらないよう空行で分ける
import re
L0 = L
L = lambda *ns: re.sub(r"(?<=[^\n])\n(?=　)", "\n\n", L0(*ns))

parts = [
    L(0, 1, 2, 3),
    L(5),
    L(6, 7),
    L(8, 9, 10),
    L(11, 12, 13),
]

intro = """# エリファス・レヴィ『光輝の書』（Le Livre des Splendeurs, 1894年）　全訳

エリファス・レヴィの遺稿をパピュが刊行した『光輝の書』の全訳。序文、第一部「イドラ・ズータ」、第二部「キリスト教の栄光」、第三部「燃える星」、「信仰告白」、「カバラーの要素――十講」、およびパピュによる付録「エリファス・レヴィの教え」を収める。底本は1902年の第2版（Google ブックスの公開スキャン）。スキャンに欠けている原本105〜120ページは訳していない。作業の記録は `作業メモ.md` にある。

---"""
full = "\n\n---\n\n".join([intro] + parts) + "\n"
(D / "光輝の書_全訳.md").write_text(full, encoding="utf-8")

ORIG = ("Éliphas Lévi, Le Livre des Splendeurs, Paris, Chamuel, 1894. "
        "作業の基にした本文：2e éd., Paris, Chacornac, 1902（Google ブックス公開スキャン）")
TAIL = ("原著は日本・米国・フランスで保護期間が満了しています。"
        "訳文は人工知能（Claude Opus 5.5）によるフランス語原典からの翻訳であり、誤りを含む可能性があります。")
TAGS = [
    "#エリファス・レヴィ #カバラー #ゾーハル #神秘主義 #オカルト #翻訳 #パブリックドメイン",
    "#エリファス・レヴィ #キリスト教 #クリシュナ #神秘主義 #オカルト #翻訳 #パブリックドメイン",
    "#エリファス・レヴィ #フリーメイソン #ヒラム #バフォメット #オカルト #翻訳 #パブリックドメイン",
    "#エリファス・レヴィ #カバラー #タロット #セフィロト #オカルト #翻訳 #パブリックドメイン",
    "#エリファス・レヴィ #パピュ #アストラル光 #魔術 #オカルト #翻訳 #パブリックドメイン",
]
NAMES = ["光輝の書1_イドラ・ズータ", "光輝の書2_キリスト教の栄光", "光輝の書3_燃える星",
         "光輝の書4_信仰告白とカバラー十講", "光輝の書5_パピュの付録"]

(D / "note用").mkdir(exist_ok=True)
for i, (name, body, tags) in enumerate(zip(NAMES, parts, TAGS), 1):
    tail = f"---\n\n## 出典\n\n> 原著：{ORIG}\n> {TAIL}\n\n{tags}\n"
    text = (f"<!-- note投稿用（光輝の書_全訳.md から生成） -->\n\n"
            + r(f"draft/head_{i}.md") + "\n\n---\n\n" + body + "\n\n" + tail)
    (D / f"note用/{name}_note.md").write_text(text, encoding="utf-8")
    print(name, len(text))
print("全訳", len(full))
