# Instruções para o Claude neste acervo

## Contexto

Escritório: Nahid, De Vitto & Campos Advogados. Sócios tributaristas.
Projeto: consultoria em Reforma Tributária, entregue por setor.

**Primeiro setor atacado: transporte rodoviário de cargas (TRC).** O acervo, porém, é
multissetorial: das 16 normas, **12 são transversais** e servem a qualquer setor. Ver
`TAXONOMIA.md` antes de acrescentar norma nova.

## Regra inegociável

**Nenhuma afirmação sem dispositivo lido.** Antes de responder qualquer coisa sobre o regime
jurídico, faça `grep` nos arquivos deste acervo e cite artigo, parágrafo e inciso. Se o
dispositivo não estiver aqui, diga que falta — não preencha por memória.

`grep` acha string, não dispositivo. **Ler o artigo inteiro** antes de afirmar.

Já aconteceu de uma síntese afirmar que o teto de 26,5% estava no art. 18 da LC 214. Está no
**art. 475, §§ 10-12**, e **não é teto**: é dever do Executivo de propor PLP. A alíquota pode
legalmente superar 26,5%. Esse é o padrão de erro a evitar.

## Como pesquisar

Os arquivos estão **na raiz** do repositório (não em `texto/`).

    grep -n "transporte de carga" LC-214-2025.txt
    grep -n -A 12 "^Art. 169" LC-214-2025.txt
    python3 mapear.py DEC-12955-2026.txt | awk -F'\t' '$2==169'

A numeração da LC **não** bate com a dos regulamentos. LC art. 169 → Decreto arts. 250,
252-255 (cinco artigos, mais o 251, que trata da obrigação do TAC). LC art. 180 → Decreto
art. 267. Sempre consultar o mapa.

## Antes de acrescentar norma

1. Normalizar com `python3 normalizar.py bruto.txt NOME.txt` — ele **aborta** se perder palavra.
2. Classificar em `fontes.tsv` (setor e jurisdição — ver `TAXONOMIA.md`).
3. Registrar no `MANIFESTO.md` com o SHA-256.
4. `python3 validar.py` — deve fechar sem falhas.

Norma estadual de imposto geral (lei do ICMS, adicional de pobreza, fundos que corroem
benefício) é **transversal** naquela UF, não do setor que motivou a busca.

## Pontos em aberto (não afirmar como resolvidos)

- **Art. 169, §1º, I** — "contribuinte que adquire bens *e* serviços": o beneficiário é só o
  embarcador (FOB), ou também a ETC que subcontrata TAC? O Decreto 12.955, art. 250, reproduz
  o texto literalmente e **não resolve**. Adotamos a leitura ampla (o §8º, sobre cooperativas,
  é o argumento decisivo), mas a controvérsia é real — consulta à RFB recomendada.
- **Percentuais do art. 169 (§4º)**, alíquotas de referência do IBS e alíquota específica do
  diesel: **pendentes de ato**. Sem eles não há quantificação — só cenário condicional.
- **Crédito de diesel no ano-teste de 2026**: o art. 267 do Decreto não está diferido para
  2027, mas a articulação com os arts. 346/348 **não foi examinada**.
- **Art. 82-C do Livro IX do RICMS-RJ** afasta o Convênio 106/96 na subcontratação e no TAC.
  A modelagem disso no simulador é **simplificada** e carece de validação.

## Estilo

Português. Citação no formato "art. 169, § 1º, I, da LC 214/2025". Separar sempre
**o que está normatizado** do **que ainda é indefinido**. Nenhum número dependente de ato
pendente vai a cliente como previsão — só como cenário condicional, com a premissa à vista.
