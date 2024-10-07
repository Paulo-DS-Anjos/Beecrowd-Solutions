# 1073 - Quadrado de Pares

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1073)

Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.

### Entrada:
A entrada contém um valor inteiro N (5 < N < 2000).

### Saída:
Imprima o quadrado de cada um dos valores pares, de 1 até N, conforme o exemplo abaixo.

Tome cuidado! Algumas linguagens tem por padrão apresentarem como saída 1e+006 ao invés de 1000000 o que ocasionará resposta errada. Neste caso, configure a precisão adequadamente para que isso não ocorra.

## Solução

Vide problema [1067 - Números Ímpares](../1067-NúmerosÍmpares/) para entender o raciocínio do `for`.

## Python 3.9

```Python
# -*- coding: utf-8 -*-

n = int(input())

for i in range(2, n + 1, 2):
    print(f'{i}^2 = {i**2}')
```
