# 1095 - Sequencia IJ 1

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1095)

Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

### Entrada:
Não há nenhuma entrada neste problema.

### Saída:
Imprima a sequencia conforme exemplo abaixo

| Exemplos de Entrada | Exemplos de Saída |
|---------------------|-------------------|
|                     | I=1 J=60           |
|                     | I=4 J=55   |
|                     |I=7 J=50|
|                     |...|
|                     |I=? J=0|


## Solução

Nesse problema, tudo o que você precisa é identificar o padrão apresentado ali. Podemos ver que o `I` vai aumentando de 3 em 3 e o `J` vai diminuindo de 5 em 5 e que a gente termina quando `J` for 0. A princípio, não sabemos onde `I` vai terminar, então você pode codificar com o critério de parada considerando apenas o valor de `J`.

## Python 3.9

```Python

```
