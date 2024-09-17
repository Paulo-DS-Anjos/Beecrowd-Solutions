# -*- coding: utf-8 -*-
cont = 0
valores = 0
for i in range (6):
    x = float(input())
    if x > 0:
        cont += 1
        valores += x
print(f'{cont} valores positivos')
print(f'{valores/cont:.1f}')