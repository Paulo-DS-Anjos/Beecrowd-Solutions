# -*- coding: utf-8 -*-
n = int(input())
in = 0
for i in range (n):
    x = int(input())
    if x > 9 and x < 21:
        in += 1
out = n - in
print(f'{in} in')
print(f'{out} out')
