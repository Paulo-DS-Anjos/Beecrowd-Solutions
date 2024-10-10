# -*- coding: utf-8 -*-
n = int(input())
lista =[]
for i in range (n):
    x1,x2,x3 = map(float , input().split())
    media = (x1*2 + x2*3 + x3*5)/10
    lista.append(media)
for i in lista:
    print(f'{i:.1f}')
