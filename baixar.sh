#!/usr/bin/env bash
# Baixa os originais listados em fontes.tsv, preservando o texto oficial.
# Só automatiza fontes do Planalto. As demais (CONFAZ, CGIBS, SEFAZ-RJ, ALERJ,
# CT-e) exigem obtenção manual — este script avisa e pula.
set -euo pipefail

mkdir -p fontes
pulados=0; baixados=0

while IFS=$'\t' read -r nome setor jurisdicao hier url; do
  [[ "$nome" =~ ^#.*$ || -z "${nome:-}" ]] && continue

  if [[ "$url" != *"planalto.gov.br"* ]]; then
    printf '>> %-30s PULADO — obter manualmente: %s\n' "$nome" "$url"
    pulados=$((pulados+1)); continue
  fi

  dest="fontes/${nome}.html"
  printf '>> %-30s ' "$nome"
  curl -sSfL --compressed -A 'Mozilla/5.0' "$url" \
    | iconv -f ISO-8859-1 -t UTF-8//TRANSLIT 2>/dev/null \
    | sed -e 's/<[^>]*>//g' -e 's/&nbsp;/ /g' -e 's/&amp;/\&/g' -e 's/&lt;/</g' -e 's/&gt;/>/g' \
    > "$dest"
  printf '%s bytes\n' "$(wc -c < "$dest")"
  baixados=$((baixados+1))
done < fontes.tsv

echo ""
echo "Baixados: ${baixados} | Manuais (pulados): ${pulados}"
echo "Agora: python3 normalizar.py fontes/NOME.html NOME.txt"
