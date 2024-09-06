# 1010 - Cálculo Simples

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1010)

Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

### Entrada:
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

### Saída:
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

## Solução

Para calcular o total da compra dos dois tipos de produtos, basta multiplicar as respectivas quantidades pelos valores dos produtos e somar esses dois valores.

Repare que os códigos dos produtos são inúteis, então em linguagens onde é possível ignorar essas variáveis, Perceba que os códigos dos produtos são inúteis, mas é preciso lê-los mesmo assim. Basta pegar o valor para as variáveis e não as utilizar mais.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
cod_1,num_pecas1,valor_peca1 = map(float,input().split())
cod_2,num_pecas2,valor_peca2 = map(float,input().split())
print(f'VALOR A PAGAR: R$ {(num_pecas1*valor_peca1 + num_pecas2*valor_peca2):.2f}')
```
