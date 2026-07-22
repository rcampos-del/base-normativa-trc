# Base Normativa — Nahid, De Vitto & Campos Advogados

Acervo normativo versionado, com integridade auditada arquivo a arquivo.

Primeiro setor atacado: **Reforma Tributária × Transporte Rodoviário de Cargas (TRC)**.
A estrutura, porém, é **multissetorial** desde o início — ver `TAXONOMIA.md`.

## Por que git

Norma muda. Quando a LC 214 for alterada de novo, `make mudou` mostra **quais dispositivos**
mudaram e a redação anterior — em vez de uma releitura de 500 artigos.

## Como está organizado

Os textos normalizados ficam **na raiz**, um arquivo por norma. A classificação por setor e
jurisdição é **metadado**, não pasta — porque uma norma pode servir a vários setores, e pasta
obrigaria a escolher um lar só. O porquê está em `TAXONOMIA.md`.

| arquivo | o que é |
|---|---|
| `*.txt` | normas normalizadas (um dispositivo por linha). É onde o `git diff` funciona |
| `fontes.tsv` | catálogo: arquivo, setor, jurisdição, hierarquia, URL oficial |
| `MANIFESTO.md` | proveniência, reparos aplicados e SHA-256 de cada arquivo |
| `TAXONOMIA.md` | como classificar e como entra setor ou UF nova |
| `CLAUDE.md` | instruções de trabalho neste acervo |
| `normalizar.py` | converte a norma em texto versionável, abortando se perder palavra |
| `validar.py` | confere o SHA de cada `.txt` contra o `MANIFESTO.md` |
| `mapear.py` | mapa de correspondência entre a LC 214 e seus regulamentos |
| `baixar.sh` | baixa os originais do Planalto listados em `fontes.tsv` |

## Convenção de nomes

    [UF-]{TIPO}-{NÚMERO}-{ANO}

    EC-132-2023        LEI-11442-2007      CONV-ICMS-106-1996
    LC-214-2025        DEC-12955-2026      RJ-LEI-2657-1996
    LC-227-2026        RES-CGIBS-6-2026    RJ-DEC-47057-2020-FOT

Normas estaduais levam o prefixo da UF. Federais e nacionais, não.

**Sem sufixo de data e sem `_v2` ou `_final`.** O git é o controle de versão. Para saber a
versão de um arquivo: `git log LC-214-2025.txt`.

## Uso

    make validar      # confere a integridade de todos os textos
    make mudou        # o que mudou desde o último commit
    make baixar       # rebaixa os originais do Planalto

Para acrescentar uma norma nova:

    python3 normalizar.py bruto.txt NOVA-NORMA-2026.txt   # aborta se perder palavra
    # 1. acrescentar linha em fontes.tsv (com setor e jurisdição)
    # 2. acrescentar linha na tabela do MANIFESTO.md (com o SHA)
    make validar                                          # deve fechar sem falhas

Ao atualizar uma norma, commit com a data da consulta:

    git commit -m "LC 214/2025 — texto compilado consultado em 2026-07-16"

## Garantia de integridade

`normalizar.py` compara palavra a palavra a fonte e o resultado, e **aborta** se houver
divergência. O texto normalizado nunca é reescrito — só reformatado.

`validar.py` recalcula o SHA-256 de cada arquivo e compara com o `MANIFESTO.md`, acusando
arquivo alterado, arquivo sem registro e registro sem arquivo.

## Regra do projeto

> Nada entra em parecer sem estar fundamentado em dispositivo lido neste acervo.
> Síntese levanta hipótese; texto primário fundamenta.
> `grep` acha string, não dispositivo — ler o artigo inteiro.
