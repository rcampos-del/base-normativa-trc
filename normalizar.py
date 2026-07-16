#!/usr/bin/env python3
"""
normalizar.py — converte texto de norma (Planalto/DOU) em formato versionável.

REGRA DE OURO: não reescreve nada. Só remove ruído de impressão e quebra linha
nos limites de dispositivo, para que o `git diff` mostre exatamente o que mudou.

Uso:  python3 scripts/normalizar.py fontes/complementar/LC-214-2025.txt texto/LC-214-2025.txt
"""
import re, sys, unicodedata

# cabeçalho/rodapé de impressão do Planalto: "16/07/2026, 14:38 Lcp214compilado https://... 111/142"
RUIDO = re.compile(r'\d\d/\d\d/\d{4},\s*\d\d:\d\d\s+\S+\s+https?://\S+\s+\d+/\d+')

# limites de dispositivo — o ponto de quebra
QUEBRAS = [
    # só quebra em artigo de verdade: não pode vir depois de '(' nem de palavra (remissão)
    (re.compile(r'(?<![\(\w\-àâãáéêíóôõúçÀÂÃÁÉÊÍÓÔÕÚÇ])(Art\.\s*\d+[º°]?(?:-[A-Z])?)(?=\s*[\.\-º°A-ZÀ-Ú])'), r'\n\n\1'),
    (re.compile(r'\s(§\s*\d+[º°]?(?:-[A-Z])?\s)'),                    r'\n\1'),     # parágrafo
    (re.compile(r'\s(Parágrafo único\.)'),                            r'\n\1'),
    (re.compile(r'\s((?:[IVXLC]+)\s+-\s)'),                           r'\n\1'),     # inciso
    (re.compile(r'\s(([a-z])\)\s)'),                                  r'\n\1'),     # alínea
    (re.compile(r'\s((?:LIVRO|TÍTULO|CAPÍTULO|Seção|Subseção|ANEXO)\s+[IVXLC0-9])'), r'\n\n\1'),
]

# Corrupções herdadas da conversão da fonte. NÃO são lixo: são caracteres
# reais que se perderam. Apagá-los CORROMPE o texto ("ano-calendário" viraria
# "anocalendário"). Verificado caso a caso em 16/07/2026 sobre os 83 ocorrências
# do acervo — 100% eram hífen não-separável (U+2011) ou marcador de lista.
REPAROS = {
    '\u0002': '-',   # hífen não-separável corrompido (65x): ano-calendário, considera-se
    '\uF0B7': '\u2022',  # marcador de lista da fonte Symbol (16x)
    '\uF0FC': '\u2713',  # visto da fonte Wingdings (2x)
    '\u00ad': '',    # hífen de sílaba (soft hyphen): invisível, remover
    '\ufeff': '',    # BOM
}

def reparar(t: str) -> str:
    """Restaura caracteres corrompidos e remove os de controle remanescentes."""
    for ruim, bom in REPAROS.items():
        t = t.replace(ruim, bom)
    restantes = {ch for ch in t
                 if ch not in '\n\t' and unicodedata.category(ch) in ('Cc','Cf','Co','Cs')}
    if restantes:
        raise ValueError('caractere de controle não mapeado: '
                         + ', '.join(f'U+{ord(c):04X}' for c in sorted(restantes)))
    return t

def normalizar(bruto: str) -> str:
    t = unicodedata.normalize('NFC', bruto)
    t = reparar(t)
    t = RUIDO.sub(' ', t)
    t = t.replace('\r', ' ')
    t = re.sub(r'[ \t\u00a0]+', ' ', t)
    t = re.sub(r'\s*\n\s*', ' ', t)          # tudo em uma linha primeiro
    for padrao, sub in QUEBRAS:
        t = padrao.sub(sub, t)
    linhas = [l.strip() for l in t.split('\n')]
    saida, anterior_vazia = [], False
    for l in linhas:
        if not l:
            if not anterior_vazia and saida: saida.append('')
            anterior_vazia = True
        else:
            saida.append(l); anterior_vazia = False
    return '\n'.join(saida).strip() + '\n'

def conferir(bruto: str, saida: str):
    """Garante que nenhuma palavra foi perdida ou alterada."""
    pal = lambda s: re.findall(r'[0-9A-Za-zÀ-ÿ]+', RUIDO.sub(' ', s))
    a, b = pal(bruto), pal(saida)
    return a == b, len(a), len(b)

if __name__ == '__main__':
    ent, sai = sys.argv[1], sys.argv[2]
    bruto = open(ent, 'rb').read().decode('utf-8', 'replace')
    out = normalizar(bruto)
    ok, na, nb = conferir(bruto, out)
    if not ok:
        sys.exit(f'ERRO: divergência de conteúdo ({na} -> {nb} palavras). Abortado.')
    open(sai, 'w', encoding='utf-8').write(out)
    print(f'{ent} -> {sai} | {len(out.splitlines()):,} linhas | {na:,} palavras íntegras')
