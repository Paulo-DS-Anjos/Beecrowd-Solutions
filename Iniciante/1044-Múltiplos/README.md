# 1044 - Múltiplos

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1044)

Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

### Entrada:
A entrada contém valores inteiros.

### Saída:
A saída deve conter uma das mensagens conforme descrito acima.

## Solução

Uma forma bem fácil de vermos se um número é múltiplo de outro número é verificando se o resto da divisão entre o maior e o menor número dá zero, o que pode ser verificado com o operador `mod` (`%`).

> Para esse problema, certifique-se que o maior valor fique armazenado na variável `A`, assim quando for-mos verificar se `A % B == 0` vamos sempre dividir o maior pelo menor valor, usei a condicional `if` pra garantir que o maior valor esteja armazenado em `A`, não é necessário verificar se um dos dois valores é 0.

## Pyrhon 3.9

```Python
# -*- coding: utf-8 -*-
A,B = map(int,input().split())
if B > A:
    A,B = B,A
if A % B == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
```
