# 1059 - Números Pares

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1059)

Faça um programa que mostre os números pares entre 1 e 100, inclusive.

### Entrada:
Neste problema extremamente simples de repetição não há entrada.

### Saída:
Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha.

## Solução

Usando while, você pode começar o número a ser impresso valendo 2 e ir somando 2 até o número for maior que 100. Usando for, você pode colocar toda a lógica dentro da instrução for e deixar o lado de dentro apenas para a lógica do que fazer em cada for.

## Python 3.9

### Método 1:

```Python
# -*- coding: utf-8 -*-
par = 2

while(par <= 100):
    print(par)
    par += 2
```

### Método 2:

```Python
# -*- coding: utf-8 -*-
for i in range(2, 102, 2):
    print(i)
```
