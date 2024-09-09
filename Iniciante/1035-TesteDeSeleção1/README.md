# 1035 - Teste de Seleção 1

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1035)

Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

### Entrada:
Quatro números inteiros A, B, C e D.

### Saída:
Mostre a respectiva mensagem após a validação dos valores.

## Solução

Para verificar se um número é par, basta verificar se o resto da divisão do número por 2 é 0.

> Independente de você considerar 0 como um número positivo ou um número não-negativo, é possível dar Accepted com as duas abordagens (testando positivo se número > -1 ou número > 0).

## Python 3.9

```Python
# -*- coding: utf-8 -*-
A,B,C,D = map(int,input().split())
if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
    print('Valores aceitos')
else: 
    print('Valores nao aceitos')
```
