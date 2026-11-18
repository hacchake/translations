#!/bin/sh
# 指定行範囲の本文を表示。欄外の行は、章見出しと、本文のはみ出しらしい長めの行（「|」付き）だけ残す
sed -n "$1,$2p" "$(dirname "$0")/../src/scot_clean.txt" | awk '/^    \| / { s=substr($0,7); if (s ~ /The .*Chapter/) print "@@ " s; else if (length(s) >= 28) print "| " s; next } { print }'
