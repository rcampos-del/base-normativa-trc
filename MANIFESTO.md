# MANIFESTO DO ACERVO

Proveniência e integridade. Gerado em 16/07/2026; atualizado em **22/07/2026**
(taxonomia de setor e jurisdição — ver `TAXONOMIA.md`).

Cada arquivo foi normalizado a partir da fonte oficial, com conferência palavra a palavra.
O texto **não foi reescrito** — apenas reformatado e reparado quanto a caracteres
corrompidos na conversão (ver "Reparos").

Para conferir a integridade a qualquer momento:

    python3 validar.py

> **Sobre a coluna "Palavras".** Conta os tokens `[0-9A-Za-zÀ-ÿ]+` do arquivo final, de
> forma uniforme para todos os diplomas. Pode divergir em alguns pontos percentuais de
> contagens anteriores, que usavam método distinto para acentuação. **A integridade real é
> ancorada no SHA-256** — os hashes permanecem idênticos aos originais auditados.

## Integridade

| Arquivo | Norma | Setor | Jurisdição | Linhas | Palavras | SHA-256 (12) |
|---|---|---|---|---:|---:|---|
| `EC-132-2023.txt` | Emenda Constitucional nº 132, de 20/12/2023 — ADCT arts. 128-129 (transição do ICMS 2029-2033) | transversal | federal | 623 | 14.770 | `4742874996d7` |
| `LC-214-2025.txt` | Lei Complementar nº 214, de 16/01/2025 — compilada (c/ LC 227). Espinha dorsal do IBS/CBS | transversal | federal | 6.094 | 126.519 | `ad53bd0bcd8d` |
| `LC-227-2026.txt` | Lei Complementar nº 227, de 13/01/2026 — CGIBS; alterou a LC 214 | transversal | federal | 3.004 | 61.623 | `dc36fa1b24cc` |
| `LC-192-2022.txt` | Lei Complementar nº 192, de 11/03/2022 — ICMS monofásico de combustíveis | transversal | federal | 107 | 3.734 | `b5d0ae61a73a` |
| `LEI-10637-2002.txt` | Lei nº 10.637, de 30/12/2002 — PIS não cumulativo | transversal | federal | 382 | 18.003 | `71e6275b73fe` |
| `LEI-10833-2003.txt` | Lei nº 10.833, de 29/12/2003 — COFINS não cumulativo (art. 3º, §§ 19-20) | transversal | federal | 780 | 39.807 | `002fd3028601` |
| `DEC-12955-2026.txt` | Decreto nº 12.955, de 29/04/2026 — Regulamento da CBS | transversal | federal | 5.606 | 130.507 | `6ccde9b698aa` |
| `RES-CGIBS-6-2026.txt` | Resolução CGIBS nº 6, de 30/04/2026 — Regulamento do IBS | transversal | nacional | 6.934 | 143.186 | `bc41cb73a72c` |
| `LEI-11442-2007.txt` | Lei nº 11.442, de 05/01/2007 — Transporte Rodoviário de Cargas (TAC, ETC, CTC) | trc | federal | 152 | 6.423 | `e3c44dd58953` |
| `CONV-ICMS-106-1996.txt` | Convênio ICMS 106/96 (CONFAZ) — crédito outorgado de 20% ao transporte | trc | nacional | 7 | 397 | `ab5f1f4728c8` |
| `NT-CTE-2025.001.txt` | Nota Técnica CT-e 2025.001 v1.00, de 28/03/2025 — **DESATUALIZADA** | trc | nacional | 11 | 5.809 | `3af4c6200b5e` |
| `RJ-LEI-2657-1996.txt` | Lei estadual RJ nº 2.657, de 26/12/1996 — Lei do ICMS-RJ (art. 14: interna a 20%, Lei 10.253/2023) | transversal | rj | 2.012 | 58.163 | `5c2f0f08021b` |
| `RJ-LC-210-2023.txt` | Lei Complementar estadual RJ nº 210, de 21/07/2023 — FECP (c/ LC 217/2023) | transversal | rj | 53 | 2.475 | `7dbf8ae93cb4` |
| `RJ-DEC-47057-2020-FOT.txt` | Decreto estadual RJ nº 47.057, de 04/05/2020 — FOT, consolidado c/ o Dec. 50.248/2026 | transversal | rj | 123 | 5.827 | `bcb6498d5a3e` |
| `RJ-DEC-50248-2026-FOT.txt` | Decreto estadual RJ nº 50.248, de 23/03/2026 — altera o FOT; escalonamento 20%→60% | transversal | rj | 98 | 3.996 | `b8fc87ea3469` |
| `RJ-DEC-27427-2000-LIVRO-IX.txt` | RICMS-RJ (Dec. 27.427/2000), só o Livro IX — prestação de transporte (art. 82-C) | trc | rj | 333 | 15.326 | `795a9cb2b9ec` |

**Resumo:** 16 normas — 12 transversais, 4 de TRC. Por jurisdição: 8 federais, 3 nacionais, 5 do RJ.

## Fontes

As URLs oficiais de cada norma estão em `fontes.tsv`, junto da classificação de setor e
jurisdição. Só as fontes do Planalto são baixáveis por script; CONFAZ, CGIBS, SEFAZ-RJ,
ALERJ e CT-e exigem obtenção manual — o `baixar.sh` avisa e pula.

## Reparos aplicados

**Diplomas federais (fonte HTML do Planalto).** A conversão do original corrompeu 83
caracteres, verificados um a um em 16/07/2026 e restaurados. **Apagá-los teria corrompido o
texto** — "ano-calendário" viraria "anocalendário", e o termo deixaria de ser localizável.

| Corrompido | Restaurado | Ocorrências | O que era |
|---|---|---:|---|
| `U+0002` | `-` | 65 | hífen não-separável: ano-calendário, considera-se, matéria-prima |
| `U+F0B7` | `•` | 16 | marcador de lista (fonte Symbol) |
| `U+F0FC` | `✓` | 2 | visto (fonte Wingdings) |

**Convênio 106/96 e diplomas do RJ (fonte PDF oficial), acrescidos em 21/07/2026.**
Vieram de PDF (CONFAZ / SEFAZ-RJ / ALERJ) e exigiram três limpezas antes da normalização,
todas **preservadoras de conteúdo** — a verificação do `normalizar.py` confirmou zero
palavra perdida em cada um:

| Ruído removido | O que era | Onde |
|---|---|---|
| `U+000C` (form feed) | quebra de página do `pdftotext` | todos os PDF |
| `U+00AD` (hífen de sílaba) | hifenização de fim de linha ("MÁ-QUINAS" → "MÁQUINAS") | `RJ-LEI-2657-1996` (8x) |
| rodapé de página | URL + carimbo de data/hora + título repetido | todos os PDF do RJ |

O `normalizar.py` **falha com erro** diante de caractere de controle não mapeado, para que
uma corrupção nova nunca entre em silêncio.

## Limitações conhecidas

- `NT-CTE-2025.001.txt` é a **versão 1.00, de 28/03/2025 — desatualizada**. O cronograma
  vigente (homologação 01/07/2026, produção 03/08/2026) não está nela. Substituir pela
  versão consolidada do Portal Nacional do CT-e.
- `DEC-12955-2026.txt`: o ANEXO I (tabela de depreciação por NCM) não tem estrutura de
  artigo e permanece em linha única. Não afeta a leitura dos dispositivos.
- `RJ-DEC-27427-2000-LIVRO-IX.txt` cobre **apenas o Livro IX** do RICMS-RJ, não o
  Regulamento inteiro. Suficiente para o escopo de transporte.
- A vigência do crédito outorgado do transporte no RJ está evidenciada na **Consulta
  SEFAZ-RJ 043/25** (18/11/2025), mantida **fora** deste acervo por ser parecer
  administrativo, não legislação.
- Faltam (a obter quando o tema for atacado): LC 123/2006, Lei 10.209/2001, Lei 13.703/2018,
  ADI 7181/7191 (STF), Resolução ANTT do RNTR-C.
