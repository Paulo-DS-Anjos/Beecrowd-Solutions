# 1070 - Seis Números Ímpares

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1070)

Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

### Entrada:
A entrada será um valor inteiro positivo.

### Saída:
A saída será uma sequência de seis números ímpares.

## Solução

Vide problema [1067 - Números Ímpares](../1067-NúmerosÍmpares/) para entender o raciocínio por trás do `for`. Só é importante ressaltar que é necessário somar um se o número passado for par antes de começar o `for`.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
x = int(input())
if x % 2 ==0:
    x += 1
for i in range (6):
    print(x)
    x += 2
```
