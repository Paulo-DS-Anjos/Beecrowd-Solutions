# -*- coding: utf-8 -*-
a,b,c = map(float,input().split())
print(f'TRIANGULO: {((a*c)/2):.3f}')
print(f'CIRCULO: {((c**2)*3.14159):.3f}')
print(f'TRAPEZIO: {(((a+b)*c)/2):.3f}')
print(f'QUADRADO: {(b**2):.3f}')
print(f'RETANGULO: {(a*b):.3f}')