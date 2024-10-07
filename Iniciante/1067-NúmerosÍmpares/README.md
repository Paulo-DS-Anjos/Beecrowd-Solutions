# 1067 - Números Ímpares

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1067)

Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

### Entrada:
O arquivo de entrada contém 1 valor inteiro qualquer.

### Saída:
Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

## Solução

Podemos começar lendo um valor `x`, depois criamos um laço for que começa de `1` e vá até `X+1`. Com isso, começando pelo número 1 e pulando de 2 em 2, garantimos que `i` sempre será ímpar.

## Python 3.9

```Python
X = int(input())
for i in range(1, X + 1, 2):
    print(i)
```
