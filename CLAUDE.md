# Instruções para o Claude neste acervo

## Contexto
Escritório: Nahid, De Vitto & Campos Advogados. Sócios tributaristas.
Projeto: produto de consultoria em Reforma Tributária para transporte rodoviário de cargas.

## Regra inegociável
**Nenhuma afirmação sem dispositivo lido.** Antes de responder qualquer coisa sobre o regime
jurídico, faça `grep` em `texto/` e cite artigo, parágrafo e inciso. Se o dispositivo não
estiver no acervo, diga que falta — não preencha por memória.

Já aconteceu de uma síntese de pesquisa afirmar que o teto de 26,5% estava no art. 18 da
LC 214. Está no **art. 475, §§ 10-12**, e **não é teto**: é dever do Executivo de propor PLP.
A alíquota pode legalmente superar 26,5%. Esse é o padrão de erro a evitar.

## Como pesquisar
    grep -n "transporte de carga" texto/LC-214-2025.txt
    grep -n -A 12 "^Art. 169" texto/LC-214-2025.txt
    awk -F'\t' '$2==169' caderno/mapa-LC214-DEC12955.tsv   # acha o artigo correspondente no regulamento

A numeração da LC **não** bate com a dos regulamentos. LC art. 169 -> Decreto arts. 250, 252-255.
LC art. 11 -> Decreto art. 12. Sempre consultar o mapa.

## Pontos em aberto (não afirmar como resolvidos)
- **Art. 169, §1º, I** — "contribuinte que adquire bens *e* serviços": beneficiário é o
  embarcador (frete FOB) ou também a ETC que subcontrata TAC? O Decreto 12.955, art. 250,
  reproduz o texto literalmente e **não resolve**. Controvérsia real.
- **Art. 169, §3º** — crédito presumido é calculado sobre o valor *líquido* (§2º, III), que
  já é líquido do próprio crédito. Fórmula circular: CP = p × (VO − CP). Confirmar com o
  regulamento e o ato conjunto MF/CGIBS antes de parametrizar ERP.
- Percentuais do art. 169 (§4º), alíquotas de referência, alíquotas do IS, calendário do
  split payment: **pendentes de regulamentação**.

## Estilo
Português. Citação no formato "art. 169, § 1º, I, da LC 214/2025". Separar sempre
"o que está normatizado" de "o que ainda é indefinido".
