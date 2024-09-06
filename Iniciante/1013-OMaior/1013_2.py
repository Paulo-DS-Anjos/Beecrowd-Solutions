# -*- coding: utf-8 -*-
A,B,C = map(int,input().split())
MaiorAB = (A + B + abs(A-B))/2
Maior = (MaiorAB + C + abs(MaiorAB-C))/2
print(f'{Maior:.0f} eh o maior')