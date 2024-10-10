# 1080 - Maior e Posição

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1080)

Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

### Entrada:
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

### Saída:
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

## Solução

Você não precisa ter o vetor inteiro como uma variável para resolver este problema, você pode ler um número de cada vez e ir verificando se o valor é maior do que o maior valor que você tem em mãos. Com isso, o primeiro valor de `maior` ou precisa ser um número muito pequeno ou pode ser o primeiro número que você imprimir. Para seguir com essa segunda alternativa, pode ser interessante ler o primeiro elemento separadamente e fazer o `for` até 99 em vez de 100.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
maior,posicao = -1,1
for i in range(1,101):
    x = int(input())
    if x > maior:
        maior,posicao = x,i
print(maior)
print(posicao)
```
