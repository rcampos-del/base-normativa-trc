#!/usr/bin/env python3
"""
mapear.py — tabela de correspondência entre a LC 214 e seus regulamentos.
O Decreto 12.955 e a Res. CGIBS 6 citam o artigo de origem da LC entre parênteses.
Uso: python3 scripts/mapear.py texto/DEC-12955-2026.txt > caderno/mapa-LC214-DEC12955.tsv
"""
import re, sys
t = open(sys.argv[1], encoding='utf-8').read()
print('art_regulamento\tart_LC214')
atual = None
for linha in t.split('\n'):
    m = re.match(r'Art\.\s*(\d+)', linha)
    if m: atual = m.group(1)
    for o in re.finditer(r'\(\s*Art\.\s*(\d+)[^)]*?Lei Complementar n[ºo°]\s*214[^)]*\)', linha):
        if atual: print(f'{atual}\t{o.group(1)}')
