# 1066 - Pares, Ímpares, Positivos e Negativos

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1066)

Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

### Entrada:
O arquivo de entrada contém 5 valores inteiros quaisquer.

### Saída:
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.

## Solução

Não é preciso contar o número de pares neste problema porque a quantidade de números pares é sempre 5 - números ímpares. Já os números positivos e negativos precisam estar separados porque 0 é considerado um número nulo, nem positivo nem negativo.

## Python 3.9
```Python
# -*- coding: utf-8 -*-
par = 0
impar = 0
positivo = 0
negativo = 0
for i in range (1,6):
    valor = int(input())
    if valor > 0:
        positivo += 1
    elif valor < 0:
        negativo += 1
    if valor % 2 == 0:
        par += 1
    elif valor % 2 != 0:
        impar += 1
print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
```
