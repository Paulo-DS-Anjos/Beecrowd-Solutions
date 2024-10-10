# -*- coding: utf-8 -*-
maior,posicao = -1,1
for i in range(1,101):
    x = int(input())
    if x > maior:
        maior,posicao = x,i
print(maior)
print(posicao)
