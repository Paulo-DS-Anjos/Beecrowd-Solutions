# 1079 - Médias Ponderadas

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1079)

Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

### Entrada:
O arquivo de entrada contém um valor inteiro N na primeira linha. Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.

### Saída:
Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.

## Solução

Vide problema [1006 - Média 2](../1006-Média2).

## Python 3.9

```Python
# -*- coding: utf-8 -*-
n = int(input())
lista =[]
for i in range (n):
    x1,x2,x3 = map(float , input().split())
    media = (x1*2 + x2*3 + x3*5)/10
    lista.append(media)
for i in lista:
    print(f'{i:.1f}')
```
