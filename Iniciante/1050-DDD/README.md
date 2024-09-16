# 1050 - DDD

## [Descrição](https://judge.beecrowd.com/pt/problems/view/1050)

Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:

![1050-DDD Beecrowd](https://resources.beecrowd.com/gallery/images/problems/UOJ_1050.png)

Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD nao cadastrado

### Entrada:
A entrada consiste de um único valor inteiro.

### Saída:
Imprima o nome da cidade correspondente ao DDD existente na entrada. Imprima DDD nao cadastrado caso não existir DDD correspondente ao número digitado.

## Solução

Para este problema, basta usar sequência de ifs, switches ou dicionários dependendo da linguagem utilizada, e python optei por utilizar dicionários, porém utilizar ifs também soluciona o problema.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
dicionario = {
    61 : 'Brasilia',
    71 : 'Salvador',
    11 : 'Sao Paulo',
    21 : 'Rio de Janeiro',
    32 : 'Juiz de Fora',
    19 : 'Campinas',
    27 : 'Vitoria',
    31 : 'Belo Horizonte',
    }

ddd = int(input())
print('DDD nao cadastrado' if not ddd in dicionario else dicionario[ddd])
```
