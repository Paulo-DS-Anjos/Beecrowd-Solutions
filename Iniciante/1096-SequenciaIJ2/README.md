# 1096 - Sequencia IJ 2

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1096)

Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

### Entrada:
Não há nenhuma entrada neste problema.

### Saída:
Imprima a sequencia conforme exemplo abaixo

| Exemplos de Entrada | Exemplos de Saída |
|---------------------|-------------------|
|                     |       I=1 J=7     |
|                     |       I=1 J=6     |
|                     |       I=1 J=5     |
|                     |       I=3 J=7     |
|                     |       I=3 J=6     |
|                     |       I=3 J=5     |
|                     |         ...       |
|                     |       I=9 J=7     |
|                     |       I=9 J=6     |
|                     |       I=9 J=5     |

## Solução

Pelo que podemos enxergar, temos o valor de `I` começando com 1 e somando de 2 em 2, mas sendo impresso diversas vezes com o mesmo valor, mas com o valor de `J` indo sempre de 7 a 5. Com isso, pode-se fazer dois *loops* onde no mais externo muda-se o valor de `I` e no interno muda-se o valor de `J`, sempre com a mesma variação de 7 a 5.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
for i in range(1, 10, 2):
    for j in range(7, 4, -1):
        print(f'I={i} J={j}')
```
