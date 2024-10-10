# 1097 - Sequencia IJ 3

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1097)

Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

### Entrada:
Não há nenhuma entrada neste problema.

### Saída:
Imprima a sequencia conforme exemplo abaixo.

| Exemplos de Entrada | Exemplos de Saída |
|---------------------|-------------------|
|                     |       I=1 J=7     |
|                     |       I=1 J=6     |
|                     |       I=1 J=5     |
|                     |       I=3 J=9     |
|                     |       I=3 J=8     |
|                     |       I=3 J=7     |
|                     |         ...       |
|                     |       I=9 J=15    |
|                     |       I=9 J=14    |
|                     |       I=9 J=13    |

## Solução

Mais uma sequência... Dessa vez, bem parecida com a anterior (vide problema [1096 - Sequencia IJ 2](../1096-SequenciaIJ2)), mas eu aconselharia usar uma variável adicionar para auxiliar no cálculo do valor inicial de `J` a cada *loop* externo.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
I = 1
J_start = 7

while I <= 9:
    for J in range(J_start, J_start - 3, -1):
        print(f'I={I} J={J}')
    I += 2
    J_start += 2
```
