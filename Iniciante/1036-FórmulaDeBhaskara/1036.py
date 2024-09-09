# -*- coding: utf-8 -*-
import math

A, B, C = map(float, input().strip().split())
delta = B * B - 4 * A * C

if A != 0 and delta >= 0:
    X1 = (-B + math.sqrt(delta)) / (2 * A)
    X2 = (-B - math.sqrt(delta)) / (2 * A)
    print(f'R1 = {X1:.5f}')
    print(f'R2 = {X2:.5f}')
else:
    print('Impossivel calcular')