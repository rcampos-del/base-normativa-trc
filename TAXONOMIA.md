# TAXONOMIA DO ACERVO

Como as normas são classificadas e como entra um setor ou uma UF nova.

---

## O acervo tem duas dimensões, não uma

Toda norma é classificada por **setor** e por **jurisdição**. Um cliente é sempre um cruzamento das duas: *transportadora do RJ*, *indústria de SP*.

### Setor

| valor | significado |
|---|---|
| `transversal` | vale para qualquer setor — **sempre incluída em toda consulta** |
| `trc` | transporte rodoviário de cargas |
| *(novos)* | um valor novo por setor atacado |

### Jurisdição

| valor | significado |
|---|---|
| `federal` | União |
| `nacional` | CONFAZ, CGIBS e notas técnicas de âmbito nacional (convênio ICMS depende de internalização estadual) |
| `rj` | Rio de Janeiro |
| *(novas)* | uma por UF atacada |

---

## Como consultar

Para um cliente de setor **X** na UF **Y**, o acervo aplicável é:

```
setor IN ('transversal', 'X')   E   jurisdicao IN ('federal', 'nacional', 'Y')
```

O `transversal` entra **sempre**. É o que evita duplicar a LC 214 em cada setor.

---

## Regra de classificação (importante)

**Classifica-se a norma, não o dispositivo que usamos dela.**

A Lei 10.833/2003 (COFINS) é `transversal`, ainda que o §19 do art. 3º trate do crédito presumido de subcontratação de TAC. A lei serve a todos os setores; o dispositivo é que é setorial.

Se classificássemos pelo dispositivo, toda lei geral acabaria etiquetada com todos os setores — e a taxonomia perderia utilidade.

O elo entre *dispositivo* e *setor* não mora aqui: mora na tabela de **regras** do sistema, onde cada regra aponta para seu dispositivo, seu parecer de origem e seu grau de segurança.

---

## Por que arquivos soltos, e não pastas por setor

Uma norma pode servir a vários setores ao mesmo tempo. Pasta obriga a escolher **um** lar — e a LC 214 não tem um lar só.

Duplicar o arquivo em duas pastas seria pior: duas cópias divergem, e um dia alguém cita a errada. É exatamente o que o MANIFESTO existe para impedir.

Por isso: **arquivo único, classificação como metadado.**

> Se o acervo passar de ~60 arquivos, vale reavaliar e agrupar por hierarquia (`02-complementar/`, `04-decreto/`). Agrupar por *hierarquia* é seguro, porque uma norma tem só uma. Por *setor*, não.

---

## Como entra um setor novo

1. Levantar as normas específicas do setor e normalizar com o `normalizar.py`.
2. Acrescentar uma linha em `fontes.tsv` para cada uma, com o novo valor de setor.
3. Acrescentar cada arquivo à tabela de integridade do `MANIFESTO.md`, com SHA-256.
4. Rodar `python3 validar.py` — deve fechar sem falhas.
5. As normas `transversal` **já estão prontas** e não se tocam.

**Teste de acerto do desenho:** se a chegada de um setor novo exigir mudar a *estrutura* (colunas, scripts, esquema do banco), o desenho estava errado. Se bastar **acrescentar linhas**, estava certo.

## Como entra uma UF nova

Mesmo procedimento, com dois cuidados que o RJ ensinou:

- **A lei do ICMS estadual e o adicional de pobreza são `transversal`** naquela UF — servem a qualquer cliente de lá, não só ao setor atacado.
- **Verificar fundos estaduais que corroem benefícios** (no RJ, o FOT). Costumam ser `transversal` e passam despercebidos porque não estão na lei do imposto.

---

## Estado atual

16 normas: **12 transversais** e **4 de TRC**.

| jurisdição | total | transversal | trc |
|---|---:|---:|---:|
| federal | 8 | 7 | 1 |
| nacional | 3 | 1 | 2 |
| rj | 5 | 4 | 1 |

Leitura prática: um cliente de **outro setor no RJ** já encontra **12 das 16 normas prontas e auditadas**. Só faltam as específicas do setor dele.
