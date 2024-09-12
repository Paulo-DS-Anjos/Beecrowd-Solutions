# 1045 - Tipos de Triângulos

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1045)

Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

se A ≥ B+C, apresente a mensagem: `NAO FORMA TRIANGULO`
se A2 = B2 + C2, apresente a mensagem: `TRIANGULO RETANGULO`
se A2 > B2 + C2, apresente a mensagem: `TRIANGULO OBTUSANGULO`
se A2 < B2 + C2, apresente a mensagem: `TRIANGULO ACUTANGULO`
se os três lados forem iguais, apresente a mensagem: `TRIANGULO EQUILATERO`
se apenas dois dos lados forem iguais, apresente a mensagem: `TRIANGULO ISOSCELES`

### Entrada:
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

### Saída
Imprima todas as classificações do triângulo especificado na entrada.

## Solução

Primeiro, verifique se é possível formar triângulo, caso contrário todas as outras verificações se tornam inúteis. Só verificando que é de fato possível formar triângulo que então se faz o resto das verificações, agrupando em `RETANGULO`/`OBTUSANGULO`/`ACUTANGULO` e `EQUILATERO`/`ISOSCELES`.
> OBS.: ordenar eles em ordem decrescente ajuda diminuir o número de condicionais necessárias para solucionar o problema.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
lados = list(map(float, input().split()))
lados.sort(reverse = True)
A,B,C = lados
if (A >= (B + C)):
    print('NAO FORMA TRIANGULO')
else:
    if ((A * A) == (B * B + C * C)):
        print('TRIANGULO RETANGULO')
    elif ((A * A) > (B * B + C * C)):
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')

    if (A == B and B == C):
        print('TRIANGULO EQUILATERO')
    elif(A == B or A == C or B == C):
        print('TRIANGULO ISOSCELES')
```
