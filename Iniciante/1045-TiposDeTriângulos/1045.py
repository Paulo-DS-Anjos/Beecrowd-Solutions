# -*- coding: utf-8 -*-
lados = list(map(float, input().split()))
lados.sort(reverse = True)
A,B,C = lados
if (A >= (B + C)):
    print('NAO FORMA TRIANGULO')
else:
    if ((A * A) == (B * B + C * C)):
        print('TRIANGULO RETANGULO')
    elif ((A * A) > (B * B + C * C)):
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')

    if (A == B and B == C):
        print('TRIANGULO EQUILATERO')
    elif(A == B or A == C or B == C):
        print('TRIANGULO ISOSCELES')