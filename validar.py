#!/usr/bin/env python3
"""Confere se cada texto/ normalizado preserva integralmente as palavras da fonte/."""
import re, glob, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from normalizar import normalizar, conferir

falhas = 0
for src in sorted(glob.glob('fontes/*/*.html')):
    nome = os.path.basename(src)[:-5]
    alvo = f'texto/{nome}.txt'
    if not os.path.exists(alvo):
        print(f'  [--] {nome}: sem texto normalizado'); continue
    bruto = open(src, 'rb').read().decode('utf-8', 'replace')
    ok, na, nb = conferir(bruto, open(alvo, encoding='utf-8').read())
    print(f'  [{"ok" if ok else "!!"}] {nome:<18} {na:>8,} palavras')
    falhas += (not ok)
sys.exit(1 if falhas else 0)
