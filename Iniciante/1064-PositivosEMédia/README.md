# 1064 - Positivos e Média

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1064)

Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

### Entrada:
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

### Saída:
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.

## Solução

Pode-se usar uma variável para acumular as somas de todos os valores positivos para dividir depois pela quantidade de valores capturados. O `if` para decidir se o contador é maior que zero não é necessário para a resolução deste problema em específico, mas é sempre legal testar se não haverá uma divisão por zero.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
cont = 0
valores = 0
for i in range (6):
    x = float(input())
    if x > 0:
        cont += 1
        valores += x
print(f'{cont} valores positivos')
print(f'{valores/cont:.1f}')
```
