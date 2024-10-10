# 1098 - Sequencia IJ 4

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1098)

Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

### Entrada:
Não há nenhuma entrada neste problema.

### Saída:
Imprima a sequencia conforme exemplo abaixo.

| Exemplos de Entrada | Exemplos de Saída |
|---------------------|-------------------|
|                     |       I=0 J=1     |
|                     |       I=0 J=2     |
|                     |       I=0 J=3     |
|                     |    I=0.2 J=1.2    |
|                     |    I=0.2 J=2.2    |
|                     |    I=0.2 J=3.2    |
|                     |        .....      |
|                     |       I=2 J=?     |
|                     |       I=2 J=?     |
|                     |       I=2 J=?     |

## Solução

Aqui vemos que o valor de `I` e `J` são acrescidos de 0,2 toda vez, com o valor de `J` indo de 1 até 3.

> Para certas linguagens como: Java, JavaScript e Python, é necessário alguns truques para imprimir os números da forma correta.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
def formatNumber(x):
    if(x % 10 == 0):
        return f'{x//10}'
    else:
        return f'{x//10}.{x%10}'
for i in range(0, 21, 2):
    for j in range(10, 31, 10):
        print(f'I={formatNumber(i)} J={formatNumber(i + j)}')
```
