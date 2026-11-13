"""draft/ の下書きから全訳ファイルと note 用原稿2本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
r = lambda f: (D / "draft" / f).read_text(encoding="utf-8").strip()
h1, h2, b1, b2 = r("head1.md"), r("head2.md"), r("n1.md"), r("n2.md")

full = ("# 機械の中のダーウィン／酔いどれの夜なべ仕事（サミュエル・バトラー）\n\n"
        + h1.split("\n", 1)[1].strip() + "\n\n---\n\n" + b1 + "\n\n---\n\n"
        + "## 続編\n\n" + h2.split("\n", 1)[1].strip() + "\n\n---\n\n" + b2 + "\n")
(D / "機械の中のダーウィン_全訳.md").write_text(full, encoding="utf-8")

src = "R. A. Streatfeild (ed.), A First Year in Canterbury Settlement, with Other Early Essays, London: Jonathan Cape, 1923 (first ed. 1914)"
def tail(orig):
    return f"""---

## 出典

> 原著：Samuel Butler, {orig}. 作業の基にした本文：{src} の Internet Archive 公開スキャン
> 原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#サミュエルバトラー #エレホン #機械 #人工知能 #ダーウィン #進化論 #翻訳 #パブリックドメイン
"""
(D / "note用").mkdir(exist_ok=True)
for name, h, b, orig in [
    ("機械の中のダーウィン", h1, b1, '"Darwin Among the Machines", The Press (Christchurch), 13 June 1863'),
    ("酔いどれの夜なべ仕事", h2, b2, '"Lucubratio Ebria", The Press (Christchurch), 29 July 1865'),
]:
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{h}\n\n---\n\n{b}\n\n{tail(orig)}"
    (D / f"note用/{name}_note.md").write_text(note, encoding="utf-8")
    print(name, len(note))
print(len(full))
