.PHONY: baixar validar mudou ajuda

ajuda:       ## lista os comandos
	@grep -E '^[a-z]+:.*##' Makefile | sed 's/:.*##/ —/'

baixar:      ## baixa os originais do Planalto conforme fontes.tsv (pula os manuais)
	@bash baixar.sh

validar:     ## confere o SHA-256 de cada .txt contra o MANIFESTO.md
	@python3 validar.py

mudou:       ## mostra o que mudou nos textos desde o último commit
	@git diff --stat -- '*.txt' || true
	@git diff -U0 -- '*.txt' | grep -E '^[+-][^+-]' || echo "  (sem alterações)"
