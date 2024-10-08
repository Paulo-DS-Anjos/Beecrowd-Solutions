# 1075 - Resto 2

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1075)

Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.

### Entrada:
A entrada contém um valor inteiro N (N < 10000).

### Saída:
Imprima todos valores que quando divididos por N dão resto = 2, um por linha.

## Solução

O número 2 dividido por qualquer número acima de 2 dá resto 2. Com isso, começamos a imprimir o número 2 e depois para sabermos o próximo número que dá resto 2, basta somarmos por $X$, já que $X \mod X = 0$ e isso implica em $(X + 2) \mod 0 = 2$, o que indica que somar $X$ não afeta o resultado do cálculo do resto da divisão do número por $X$. Com isso, tudo o que precisamos fazer é um `for` que começa em 2 e vai somando 2 até 10000.

Simplesmente não tratei o caso de $X$ menor ou igual a 2, o que indica que não teremos nenhum caso de teste com esses valores, então tudo certo.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
N = int(input())
for i in range(2, 10000, N):
    print(i)
```
