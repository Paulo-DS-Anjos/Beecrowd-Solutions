# 1036 - Fórmula de Bhaskara

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1036)

Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

### Entrada:
Leia três valores de ponto flutuante (double) A, B e C.

### Saída:
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

## Solução

O enunciado já dá as dicas para gente, nós teremos resultados válidos se essas duas coisas acontecerem juntas:

* O valor de A tem que ser diferente de zero;
* O valor de delta tem que ser não-negativo.

Não há necessidade alguma de imprimir apenas um R1 caso delta seja igual a zero, até no ponto de vista matemático. Quando delta é igual a zero, significa que temos duas raízes com o mesmo valor, não só uma raiz, então você pode imprimir as duas com o mesmo valor corretamente.

> Você pode perceber que eu deixei para testar se A é diferente de zero depois do cálculo do delta, fiz isso apenas para simplificar o código.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
import math

A, B, C = map(float, input().strip().split())
delta = B * B - 4 * A * C

if A != 0 and delta >= 0:
    X1 = (-B + math.sqrt(delta)) / (2 * A)
    X2 = (-B - math.sqrt(delta)) / (2 * A)
    print(f'R1 = {X1:.5f}')
    print(f'R2 = {X2:.5f}')
else:
    print('Impossivel calcular')
```
