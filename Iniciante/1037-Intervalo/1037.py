# -*- coding: utf-8 -*
NUMERO = float(input())

if 0 <= NUMERO <= 25:
    print('Intervalo [0,25]')
elif 25 < NUMERO <= 50:
    print('Intervalo (25,50]')
elif 50 < NUMERO <= 75:
    print('Intervalo (50,75]')
elif 75 < NUMERO <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')