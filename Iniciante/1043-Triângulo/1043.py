# -*- coding: utf-8 -*-
A,B,C = map(float,input().strip().split())
if (A < B + C) and (B < A + C) and (C < A + B):
    print(f'Perimetro = {(A+B+C):.1f}')
else:
    print(f'Area = {((A + B)/2 * C):.1f}')