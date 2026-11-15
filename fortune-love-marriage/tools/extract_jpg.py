"""画像だけの PDF から、各ページの JPEG（DCTDecode ストリーム）を取り出す。"""
import pathlib, re, sys
data = pathlib.Path(sys.argv[1]).read_bytes()
out = pathlib.Path(sys.argv[2]); out.mkdir(exist_ok=True)
n = 0
for m in re.finditer(rb"stream\r?\n", data):
    s = m.end()
    if data[s:s+3] != b"\xff\xd8\xff":
        continue
    e = data.find(b"endstream", s)
    n += 1
    (out / f"p{n:03d}.jpg").write_bytes(data[s:e].rstrip(b"\r\n"))
print(n)
