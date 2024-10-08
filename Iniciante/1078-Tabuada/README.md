# 1078 - Tabuada

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1078)

Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
|1 x N = N | 2 x N = 2N |    ...    | 10 x N = 10N|

### Entrada:
A entrada contém um valor inteiro N (2 < N < 1000).

### Saída:
Imprima a tabuada de N, conforme o exemplo fornecido.

## Solução

Faça um `for` para escrever cada um dos resultados da tabuada de 1 até 10.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
N = int(input())
for i in range(1,11):
    print(f'{i} x {N} = {i*N}')
```
