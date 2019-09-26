# -*- coding: utf-8 -*-
import sys
import string
import hashlib

arquivo = open('texto.txt')
rotacao = 12
alfabeto = string.ascii_lowercase
alfabeto = alfabeto.lower()
resultado = ''

for letra in arquivo.read():    
    if letra in alfabeto:        
        posicao = alfabeto.find(letra)
        posicao = (posicao-rotacao) % 26
        resultado = (resultado)+(alfabeto[posicao])
    else:
        resultado = resultado + letra
print (resultado)
print hashlib.sha1(resultado).hexdigest()