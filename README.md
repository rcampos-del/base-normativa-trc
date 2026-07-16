# Base Normativa — Nahid, De Vitto & Campos Advogados

Acervo normativo versionado. Projeto inicial: **Reforma Tributária × Transporte Rodoviário de Cargas (TRC)**.

## Por que git

Norma muda. Quando a LC 214 for alterada de novo, `make mudou` mostra **quais dispositivos**
mudaram e a redação anterior — em vez de uma releitura de 500 artigos.

## Estrutura

| pasta | o que é | pode editar? |
|---|---|---|
| `fontes/` | original oficial, como baixado. **Imutável.** É o que se junta a uma peça. | Nunca |
| `texto/` | mesmo conteúdo, normalizado (um dispositivo por linha). É onde o diff funciona. | Só via `make normalizar` |
| `caderno/` | extrações curadas por nicho (ex.: só os artigos que tocam o TRC) | Gerado |
| `produto/` | pareceres, teses, checklists, matrizes. **Nosso trabalho.** | Sim |
| `scripts/` | automação | Sim |

Hierarquia dentro de `fontes/`: `01-constitucional` → `02-complementar` → `03-ordinaria` →
`04-decreto` → `05-infralegal` → `06-documento-fiscal` → `07-convenio`.

## Convenção de nomes

    {TIPO}-{NÚMERO}-{ANO}

    EC-132-2023        LEI-11442-2007      RES-CGIBS-6-2026
    LC-214-2025        DEC-12955-2026      NT-CTE-2025.001
    LC-227-2026        CONV-ICMS-106-1996  ATO-RFB-CGIBS-1-2025

**Sem sufixo de data e sem "_v2" ou "_final".** O git é o controle de versão — data no nome
é justamente o que ele existe para eliminar. Para saber a versão: `git log texto/LC-214-2025.txt`.

## Uso

    make baixar       # busca os originais do Planalto (fontes.tsv)
    make normalizar   # fontes/ -> texto/
    make validar      # confere que nada foi perdido na normalização
    make mudou        # o que mudou desde o último commit

Ao atualizar uma norma, commit com a data da consulta:

    git commit -m "LC 214/2025 — texto compilado consultado em 2026-07-16"

## Garantia de integridade

`normalizar.py` compara palavra a palavra a fonte e o resultado, e **aborta** se houver
qualquer divergência. O texto normalizado nunca é reescrito — só reformatado.

## Regra do projeto

> Nada entra em `produto/` sem estar fundamentado em dispositivo lido em `texto/`.
> Síntese levanta hipótese; texto primário fundamenta.
