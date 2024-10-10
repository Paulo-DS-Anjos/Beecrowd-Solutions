# -*- coding: utf-8 -*-
N = int(input())
coelho,rato,sapo = 0,0,0
total = coelho+rato+sapo

for _ in range(N):
    quant,tipo = input().strip().split(' ')
    quant = int(quant)
    if tipo == 'C':
        coelho += quant
    elif tipo == 'R':
        rato += quant
    else:
        sapo += quant

total = coelho+rato+sapo

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {coelho/total *100:.2f} %')
print(f'Percentual de ratos: {rato/total *100:.2f} %')
print(f'Percentual de sapos: {sapo/total *100:.2f} %')
