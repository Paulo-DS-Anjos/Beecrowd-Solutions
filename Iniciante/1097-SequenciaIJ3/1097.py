# -*- coding: utf-8 -*-
I = 1
J_start = 7

while I <= 9:
    for J in range(J_start, J_start - 3, -1):
        print(f'I={I} J={J}')
    I += 2
    J_start += 2
