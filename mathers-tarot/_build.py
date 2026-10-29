# 下書きから全訳とnote用原稿を作る
import re, pathlib
d = pathlib.Path(__file__).parent
parts = ['head'] + [f't{i}' for i in range(1, 7)]
texts = [(d / 'draft' / f'{p}.md').read_text(encoding='utf-8').strip() for p in parts]
TAIL = '''---

## 出典

> 原作：S. L. MacGregor Mathers, The Tarot: Its Occult Signification, Use in Fortune-Telling, and Method of Play, Etc.（George Redway, London, 1888年）
> 本訳は、原作を全訳したものです。原作は著作権保護期間が満了しています。本文は Sacred Texts Archive の電子テキストによりました。訳文は人工知能（Claude Opus 5.5）による翻訳であり、誤りを含む可能性があります。

#タロット #マサース #黄金の夜明け団 #オカルト #占い #翻訳 #パブリックドメイン
'''
full = '\n\n'.join(texts) + '\n'
(d / 'タロット_全訳.md').write_text(full, encoding='utf-8')

# note用：表と図（コードブロック）を箇条書きにする
DIAGRAMS = [
    # 第二の方法
    ['表示札を右端に置き、その左に右から左へ並べる。',
     '一列目：1、2、3、4、5、6、7（右から左へ）',
     '二列目：8、9、10、11、12、13、14（一列目の下）',
     '三列目：15、16、17、18、19、20、21（二列目の下）'],
    # 第三の方法
    ['アーチの上の部分（二列）：上の列に、右から左へ23〜33。その下の列に、右から左へ56〜66。',
     'アーチの右の柱：上から下へ11、10、9……1（1が右下）。',
     'アーチの左の柱：上から下へ22、21、20……12（12が左下）。',
     '三角形の右の辺：右の柱の内側に、上から斜め左下へ44、43……34。',
     '三角形の左の辺：左の柱の内側に、上から斜め右下へ55、54……45。二つの辺は下の中央（45と34）で出会い、逆さの三角形になる。',
     '表示札：三角形の中央。'],
]
def to_note(md):
    out, lines, i, k = [], md.split('\n'), 0, 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('```'):
            j = i + 1
            while not lines[j].startswith('```'):
                j += 1
            out += ['- ' + x for x in DIAGRAMS[k]]
            k += 1; i = j + 1; continue
        if l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip('|').split('|')]); i += 1
            head, body = rows[0], [r for r in rows[2:]]
            for r in body:
                if not any(head):  # 見出しのない表（365日の計算）
                    out.append(f'- {r[0]}：{r[1]}')
                elif len(r) == 2:
                    out.append(f'- {r[0]}：{r[1]}点' if head[1] == '点' else f'- {r[0]}：{r[1]}')
                elif head[0] == '番号':
                    out.append(f'- {r[0]}　{r[3]}（イタリア語 {r[1]}／フランス語 {r[2]}）……{r[4]}')
                else:
                    out.append(f'- {r[2]}（イタリア語 {r[0]}／フランス語 {r[1]}）……普通のカードの{r[3]}')
            continue
        out.append(l); i += 1
    return '\n'.join(out)
note = '<!-- note投稿用（タロット_全訳.md から生成。表と図を箇条書きにした） -->\n\n' + to_note(full).rstrip() + '\n\n' + TAIL
(d / 'note用').mkdir(exist_ok=True)
(d / 'note用' / 'タロット_note.md').write_text(note, encoding='utf-8')
print(len(full), len(note), k if False else '')
