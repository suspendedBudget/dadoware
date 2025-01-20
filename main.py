#!/usr/bin/env python3

import random
import argparse

parser = argparse.ArgumentParser(description='gets the number of words')
parser.add_argument('num_of_words', type=int)
args = parser.parse_args()


rnd = random.SystemRandom()

dadoware = {}
with open('7776palavras-numeradas-2e.txt', encoding='utf8') as fp:
    dadoware.update(lin.strip().split() for lin in fp)

passphrase = []
for i in range(args.num_of_words):
    # sequência de f{num_of_words} dados randomizados
    dados = ''.join(str(rnd.randint(1, 6)) for i in range(5))

    # seleciona a palavra com a correspondente sequência de dados em dadoware.txt
    passphrase.append(dadoware[dados])

print(f'Sua frase secreta é: {' '.join(passphrase)}')

with open("passphrase.txt", "w", encoding="utf-8") as file:
    file.write(f'Sua frase secreta é:\n\n{' '.join(passphrase)}')

