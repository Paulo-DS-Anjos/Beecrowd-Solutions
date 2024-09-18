# 1065 - Pares entre Cinco Números

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1065)

Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

### Entrada:
O arquivo de entrada contém 5 valores inteiros quaisquer.

### Saída:
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

## Solução

Vide problema [1066 - Pares, Ímpares, Positivos e Negativos](../1066-ParesÍmparesPositivosENegativos), uma versão muito mais difícil desse problema.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
resultado = sum([float(input()) % 2 == 0 for _ in range (5)])
print(f'{resultado} valores pares')
```
