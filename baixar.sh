#!/usr/bin/env bash
# baixa os originais listados em fontes.tsv, preservando o HTML oficial intacto.
set -euo pipefail
while IFS=$'\t' read -r nome hier url; do
  [[ "$nome" =~ ^#.*$ || -z "${nome:-}" ]] && continue
  dest="fontes/${hier}/${nome}.html"
  echo ">> ${nome}"
  curl -sSfL --compressed -A 'Mozilla/5.0' "$url" \
    | iconv -f ISO-8859-1 -t UTF-8//TRANSLIT 2>/dev/null \
    | sed -e 's/<[^>]*>//g' -e 's/&nbsp;/ /g' -e 's/&amp;/\&/g' -e 's/&lt;/</g' -e 's/&gt;/>/g' \
    > "$dest"
  printf '   %s (%s bytes)\n' "$dest" "$(wc -c < "$dest")"
done < fontes.tsv
echo "OK. Agora: make normalizar"
