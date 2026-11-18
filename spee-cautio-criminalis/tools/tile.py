"""PDF の各ページを画像にし、2ページずつ横に並べたタイルを作る。"""
import sys, fitz, pathlib
src, out = sys.argv[1], pathlib.Path(sys.argv[2])
d = fitz.open(src)
n = d.page_count
for i in range(0, n, 2):
    pix = [d[j].get_pixmap(dpi=120, colorspace=fitz.csGRAY) for j in range(i, min(i + 2, n))]
    w = sum(p.width for p in pix); h = max(p.height for p in pix)
    t = fitz.Pixmap(fitz.csGRAY, fitz.IRect(0, 0, w, h), False); t.clear_with(255)
    x = 0
    for p in pix:
        p.set_origin(x, 0); t.copy(p, p.irect); x += p.width
    t.save(out / f"t{i+1:03d}.png")
print(n)
