# 1012 - Área

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1012)

Escreva um programa que leia três valores com ponto flutuante de dupla precisão: `A, B e C`. Em seguida, calcule e mostre:

a) a área do `triângulo` retângulo que tem `A por base` e `C por altura`.

b) a área do `círculo` de `raio C`. (`pi = 3.14159`)

c) a área do `trapézio` que tem `A e B por bases` e `C por altura`.

d) a área do `quadrado` que tem `lado B`.

e) a área do `retângulo` que tem `lados A e B`.

### Entrada:
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

### Saída:
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.

## Solução

As fórmulas que você pode usar são:

<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;\text{Area&space;do&space;Triangulo}&space;=&space;\frac{A&space;\times&space;C}{2}" title="\bg_white \text{Area do Triangulo} = \frac{A \times C}{2}" />

<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;\text{Area&space;do&space;Circulo}&space;=&space;\pi&space;\times&space;C^{2}" title="\bg_white \text{Area do Circulo} = \pi \times C^{2}" />

<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;\text{Area&space;do&space;Trapezio}&space;=&space;\frac{A&space;&plus;&space;B}{2}&space;\times&space;C" title="\bg_white \text{Area do Trapezio} = \frac{A + B}{2} \times C" />

<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;\text{Area&space;do&space;Quadrado}&space;=&space;B&space;\times&space;B" title="\bg_white \text{Area do Quadrado} = B \times B" />

<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;\text{Area&space;do&space;Retangulo}&space;=&space;A&space;\times&space;B" title="\bg_white \text{Area do Retangulo} = A \times B" />

## Python 3.9

```Python
# -*- coding: utf-8 -*-
a,b,c = map(float,input().split())
print(f'TRIANGULO: {((a*c)/2):.3f}')
print(f'CIRCULO: {((c**2)*3.14159):.3f}')
print(f'TRAPEZIO: {(((a+b)*c)/2):.3f}')
print(f'QUADRADO: {(b**2):.3f}')
print(f'RETANGULO: {(a*b):.3f}')
```
