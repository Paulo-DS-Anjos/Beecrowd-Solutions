# 1043 - Triângulo

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1043)

Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

### Entrada:
A entrada contém três valores reais.

### Saída:
O resultado deve ser apresentado com uma casa decimal.

## Solução

Podemos pensar em alguns exemplos de tamanhos de lados que não podem formar triângulo (como por exemplo, dois lados muito pequenos e um lado muito grande). Para que os lados `A`, `B` e `C` sejam capazes de formar um triângulo, é necessário que a soma de dois dos lados seja sempre maior que o terceiro lado, ou seja, `$A < B + C$, $B < A + C$ e $C < A + B$`. Cumprindo essas três inequações, temos três lados de um triângulo.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
A,B,C = map(float,input().strip().split())
if (A < B + C) and (B < A + C) and (C < A + B):
    print(f'Perimetro = {(A+B+C):.1f}')
else:
    print(f'Area = {((A + B)/2 * C):.1f}')
```
