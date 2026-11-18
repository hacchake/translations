#!/bin/sh
# 呪文の多い巻用：欄外の行も14字以上なら残す
sed -n "$1,$2p" "$(dirname "$0")/../src/scot_clean.txt" | awk '/^    \| / { s=substr($0,7); if (s ~ /The .*Chapter/) print "@@ " s; else if (length(s) >= 14 && s !~ /(Booke|of Witchcraft|The discover)/) print "| " s; next } { print }'
