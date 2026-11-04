"""draft/ の下書きから全訳ファイルと note 用原稿を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
ch = [(D / f"draft/m{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 6)]
body = "\n\n".join(ch)

full = head.replace(head.split("\n", 1)[0], "# ヘルメスの秘奥", 1) + "\n\n---\n\n" + body + "\n"
(D / "ヘルメスの秘奥_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Jean d'Espagnet, Arcanum Hermeticae Philosophiae Opus, 1623; English translation by Elias Ashmole (1650), revised with preface and notes by "Sapere Aude" (W. Wynn Westcott), Collectanea Hermetica Vol. I, London, 1893. 作業の基にした本文：Internet Archive 公開のスキャン
> 本訳は、原著を全訳したものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#錬金術 #賢者の石 #ヘルメス主義 #黄金の夜明け団 #オカルト #翻訳 #パブリックドメイン
"""
note = "<!-- note投稿用（ヘルメスの秘奥_全訳.md から生成） -->\n\n" + head + "\n\n---\n\n" + body + "\n\n" + tail
(D / "note用/ヘルメスの秘奥_note.md").write_text(note, encoding="utf-8")
print(len(full), len(note))
