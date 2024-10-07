# -*- coding: utf-8 -*-
par = 0
impar = 0
positivo = 0
negativo = 0
for i in range (1,6):
    valor = int(input())
    if valor > 0:
        positivo += 1
    elif valor < 0:
        negativo += 1
    if valor % 2 == 0:
        par += 1
    elif valor % 2 != 0:
        impar += 1
print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
