# 1074 - Par ou Ímpar

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1074)

Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá imprimir apenas NULL.

### Entrada:
A primeira linha da entrada contém um valor inteiro N(N < 10000) que indica o número de casos de teste. Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).

### Saída:
Para cada caso, imprima uma mensagem correspondente, de acordo com o exemplo abaixo. Todas as letras deverão ser maiúsculas e sempre deverá haver um espaço entre duas palavras impressas na mesma linha.

## Solução

Eu escolhi primeiro testar se é positivo ou negativo porque para algumas linguagens, é problemático conseguir o módulo de um número negativo. Desta maneira, eu pude pegar o valor absoluto do número para fazer o teste de par ou ímpar corretamente.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
x = int(input())
for _ in range (x):
    num = int(input())
    if num == 0:
        print('NULL')
    elif num % 2 == 0:
        if num > 0:
            print('EVEN POSITIVE')
        else:
            print('EVEN NEGATIVE')
    else:
        if num > 0:
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')
```
