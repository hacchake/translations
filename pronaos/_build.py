"""draft/ の下書きから全訳ファイルと note 用原稿3本を生成する。"""
import pathlib

D = pathlib.Path(__file__).parent
head = (D / "draft/head.md").read_text(encoding="utf-8").strip()
p = {i: (D / f"draft/n{i}.md").read_text(encoding="utf-8").strip() for i in range(1, 9)}
body = "\n\n".join(p[i] for i in range(1, 9))

full = head.replace(head.split("\n", 1)[0], "# 叡智の神殿の前廊にて（フランツ・ハルトマン）", 1) + "\n\n---\n\n" + body + "\n"
(D / "叡智の神殿の前廊にて_全訳.md").write_text(full, encoding="utf-8")

tail = """---

## 出典

> 原著：Franz Hartmann, In the Pronaos of the Temple of Wisdom, Occult Publishing Company, Boston, 1890. 作業の基にした本文：Internet Archive 公開の1890年初版のスキャン（Global Grey の電子版を併用）
> 本訳は、原著を全訳したものです。原著は日本・米国・英国で保護期間が満了しています。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#薔薇十字団 #フランツハルトマン #錬金術 #神秘主義 #オカルト #翻訳 #パブリックドメイン
"""
title, rest = head.split("\n", 1)
parts = [
    ("（一）", (1, 2, 3), "第一回には、序文、第一章「序論」、第二章「ヘルメス哲学」（新プラトン派の哲学者たち）、第三章「中世の哲学者たち」を収めます。第二回は第四章から付録の前書きまで、第三回は第七章・第八章と訳注です。"),
    ("（二）", (4, 5, 6), "第二回には、第四章「『熟達者』たちのあいだで」、第五章「薔薇十字の『団』」、第六章「偽の薔薇十字団員――詐欺師と愚か者」と、付録の前書きを収めます。第一回は序文から第三章まで、第三回は第七章・第八章と訳注です。"),
    ("（三）", (7, 8), "第三回には、第七章「まことの薔薇十字の神殿の前廊にて」（薔薇十字の規則・務め・十六のしるし・十二の宝石・象徴図の銘文）、第八章「錬金術」（ヘルメスの公理四十三か条）と訳注を収めます。第一回は序文から第三章まで、第二回は第四章から付録の前書きまでです。"),
]
for n, (sub, rng, summ) in enumerate(parts, 1):
    b = "\n\n".join(p[i] for i in rng)
    note = f"<!-- note投稿用（全訳から生成） -->\n\n{title} {sub}\n{rest}\n\n## この記事の内容\n\n　{summ}\n\n---\n\n{b}\n\n{tail}"
    (D / f"note用/叡智の神殿の前廊にて_note_{n}.md").write_text(note, encoding="utf-8")
    print(n, len(note))
print(len(full))
