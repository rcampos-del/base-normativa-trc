#!/usr/bin/env python3
"""
validar.py — confere a integridade do acervo.

O que faz: para cada .txt do repositório, recalcula o SHA-256 e compara com o
registrado no MANIFESTO.md. Acusa arquivo alterado, arquivo sem registro e
registro sem arquivo.

Por que assim: a versão anterior procurava originais em 'fontes/*/*.html', pasta
que não existe no repositório — encontrava zero arquivos e retornava "tudo certo"
sem conferir nada. Falsa segurança. Esta versão valida o que de fato está aqui.
"""
import re, glob, hashlib, sys, os

RAIZ = os.path.dirname(os.path.abspath(__file__))
MAN = os.path.join(RAIZ, "MANIFESTO.md")

if not os.path.exists(MAN):
    print("!! MANIFESTO.md não encontrado."); sys.exit(1)

registrado = {}
for linha in open(MAN, encoding="utf-8"):
    arq = re.search(r"`([^`]+\.txt)`", linha)
    shas = re.findall(r"`([0-9a-f]{12})`", linha)
    if arq and shas:
        registrado[arq.group(1)] = shas[-1]

presentes = {os.path.basename(p) for p in glob.glob(os.path.join(RAIZ, "*.txt"))}
falhas = 0

for arq in sorted(presentes | set(registrado)):
    caminho = os.path.join(RAIZ, arq)
    if arq not in registrado:
        print(f"  [!!] {arq:<34} presente, mas SEM registro no MANIFESTO"); falhas += 1; continue
    if arq not in presentes:
        print(f"  [!!] {arq:<34} registrado, mas AUSENTE do repositório"); falhas += 1; continue
    real = hashlib.sha256(open(caminho, "rb").read()).hexdigest()[:12]
    if real == registrado[arq]:
        print(f"  [ok] {arq:<34} {real}")
    else:
        print(f"  [!!] {arq:<34} ALTERADO — real {real} / manifesto {registrado[arq]}"); falhas += 1

print("")
print(f"{len(presentes)} arquivos · {len(registrado)} registros · {falhas} falha(s)")
sys.exit(1 if falhas else 0)
