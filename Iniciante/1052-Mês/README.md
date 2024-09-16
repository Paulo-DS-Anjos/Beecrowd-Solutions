# 1052 - Mês

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1052)

Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

### Entrada:
A entrada contém um único valor inteiro.

### Saída:
Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.

## Solução

Vide problema [1050 - DDD](./1050-DDD).

## Python 3.9

```Python
# -*- coding: utf-8 -*-
mes = int(input())
meses = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']

print(meses[mes - 1])
```
