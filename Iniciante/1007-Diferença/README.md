# 1007 - Diferença

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1007)

Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada:
O arquivo de entrada contém 4 valores inteiros.

Saída:
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

## Solução

Problema muito parecido com os problemas [1001-ExtremamenteBásico](../1001-ExtremamenteBásico), [1003-SomaSimples](../1003-SomaSimples) e [1004-ProdutoSimples](../1004-ProdutoSimples).

## Python

```Python
# -*- coding: utf-8 -*-
A = int(input())
B = int(input())
C = int(input())
D = int(input())
print(f'DIFERENCA = {A*B - C*D}')
```
