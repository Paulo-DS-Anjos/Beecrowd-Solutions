# 1072 - Intervalo 2

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1072)

Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

### Entrada:
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 
### Saída:
Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.

## Solução

Só é preciso contar o número de `in`, já que o `out` pode ser calculado como `N - in`.

## Python 3.9

```Python
# -*- coding: utf-8 -*-

n = int(input())
in = 0
for i in range (n):
    x = int(input())
    if x > 9 and x < 21:
        in += 1
out = n - in
print(f'{in} in')
print(f'{out} out')
```
