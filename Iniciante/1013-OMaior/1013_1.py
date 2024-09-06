# -*- coding: utf-8 -*-
A,B,C = map(int,input().split())
maior = lambda A, B: (A + B + abs(A - B))//2
print(f'{maior(A, maior(B, C))} eh o maior')