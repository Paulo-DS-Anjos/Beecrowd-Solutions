# -*- coding: utf-8 -*-
inteiro,fracao = [int(x) for x in input().strip().split('.')]
cedula = [100,50,20,10,5,2,100,50,25,10,5,1]
print('NOTAS:')
for x in cedula[:6]:
    print(f'{(inteiro // x):.0f} nota(s) de R$ {x:.2f}')
    inteiro %= x
fracao += inteiro*100
print('MOEDAS:')
for x in cedula[6:]:
    print(f'{(fracao//x):.0f} moeda(s) de R$ {(x/100):.2f}')
    fracao %= x
