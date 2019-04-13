cd allTXT
for file in ./*; do [ -f "$file" ] && wc -l "$file"; done | sort -rn > ../sorted.txt
