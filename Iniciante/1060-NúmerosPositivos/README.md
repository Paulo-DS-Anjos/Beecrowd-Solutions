# 1060 - Números Positivos

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1060)

Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

### Entrada:
Seis valores, negativos e/ou positivos.

### Saída:
Imprima uma mensagem dizendo quantos valores positivos foram lidos.

## Solução

Leia cada número de cada vez e conte apenas os números que são maiores que zero incrementando uma variável de contagem.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
positivos = sum([float(input()) > 0 for _ in range(6)])
print(f"{positivos} valores positivos")
```
