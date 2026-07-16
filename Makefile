.PHONY: baixar normalizar validar mudou tudo

tudo: baixar normalizar validar

baixar:      ## baixa os originais do Planalto conforme fontes.tsv
	@bash scripts/baixar.sh

normalizar:  ## converte fontes/ -> texto/ (um dispositivo por linha)
	@for f in fontes/*/*.html; do \
	  n=$$(basename $$f .html); \
	  python3 scripts/normalizar.py $$f texto/$$n.txt; \
	done

validar:     ## confere integridade de todos os textos normalizados
	@python3 scripts/validar.py

mudou:       ## o que mudou desde o último commit
	@git diff --stat -- texto/ || true
	@git diff -U0 -- texto/ | grep -E '^[+-][^+-]' || echo "  (sem alterações)"
