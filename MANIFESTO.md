# MANIFESTO DO ACERVO

Proveniência e integridade. Gerado em 16/07/2026.

Cada arquivo foi normalizado (um dispositivo por linha) a partir da fonte oficial,
com conferência palavra a palavra. O texto **não foi reescrito** — apenas reformatado
e reparado quanto a caracteres corrompidos na conversão (ver "Reparos" abaixo).

| Arquivo | Norma | Linhas | Palavras | SHA-256 (12) |
|---|---|---:|---:|---|
| `DEC-12955-2026.txt` | Decreto nº 12.955, de 29/04/2026 — Regulamento da CBS | 5,606 | 130,507 | `6ccde9b698aa` |
| `EC-132-2023.txt` | Emenda Constitucional nº 132, de 20/12/2023 | 623 | 14,770 | `4742874996d7` |
| `LC-214-2025.txt` | Lei Complementar nº 214, de 16/01/2025 — texto compilado | 6,094 | 126,519 | `ad53bd0bcd8d` |
| `LC-227-2026.txt` | Lei Complementar nº 227, de 13/01/2026 | 3,004 | 61,623 | `dc36fa1b24cc` |
| `LEI-11442-2007.txt` | Lei nº 11.442, de 05/01/2007 — Transporte Rodoviário de Cargas | 152 | 6,423 | `e3c44dd58953` |
| `NT-CTE-2025.001.txt` | Nota Técnica CT-e 2025.001 v1.00, de 28/03/2025 — DESATUALIZADA | 11 | 5,809 | `3af4c6200b5e` |
| `RES-CGIBS-6-2026.txt` | Resolução CGIBS nº 6, de 30/04/2026 — Regulamento do IBS | 6,934 | 143,186 | `bc41cb73a72c` |

## Fontes

- `DEC-12955-2026.txt` — https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/decreto/d12955.htm
- `EC-132-2023.txt` — https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm
- `LC-214-2025.txt` — https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm
- `LC-227-2026.txt` — https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp227.htm
- `LEI-11442-2007.txt` — https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/lei/l11442.htm
- `NT-CTE-2025.001.txt` — https://www.cte.fazenda.gov.br/portal/
- `RES-CGIBS-6-2026.txt` — portal do Comitê Gestor do IBS

## Reparos aplicados

A conversão do HTML/PDF de origem corrompeu 83 caracteres. Verificados um a um
em 16/07/2026 e restaurados. **Apagá-los teria corrompido o texto** — "ano-calendário"
viraria "anocalendário", e o termo deixaria de ser localizável por busca.

| Corrompido | Restaurado | Ocorrências | O que era |
|---|---|---:|---|
| `U+0002` | `-` | 65 | hífen não-separável: ano-calendário, considera-se, matéria-prima, Repetro-Temporário |
| `U+F0B7` | `•` | 16 | marcador de lista (fonte Symbol) |
| `U+F0FC` | `✓` | 2 | visto (fonte Wingdings) |

O `normalizar.py` **falha com erro** se encontrar caractere de controle não mapeado —
para que uma corrupção nova nunca entre silenciosamente.

## Limitações conhecidas

- `NT-CTE-2025.001.txt` é a **versão 1.00, de 28/03/2025 — desatualizada**. O cronograma
  vigente (homologação 01/07/2026, produção 03/08/2026) não está nela. Substituir pela
  versão consolidada do Portal Nacional do CT-e.
- `DEC-12955-2026.txt`: o ANEXO I (tabela de depreciação por NCM) não tem estrutura de
  artigo e permanece em linha única de ~48 mil caracteres. Não afeta a leitura dos
  dispositivos; afeta o `git diff` daquele anexo apenas.
- Faltam no acervo: Convênio ICMS 106/1996, Leis 10.833/2003 e 10.637/2002,
  LC 123/2006, Lei 10.209/2001, Lei 13.703/2018, Ato Conjunto RFB/CGIBS 1/2025.
