# 1094 - Experiências

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1094)

Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

### Entrada:
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

### Saída:
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.

## Solução

É necessário apenas guardar as quantidades de coelhos, ratos e sapos, podendo calcular o total e as porcentagens ao final do programa. Ele aparenta ser mais difícil do que realmente é, usar uma abordagem de dividir o problema em passos menores faz toda a diferença pra solucionar esse desafio. 

## Python 3.9

```Python
# -*- coding: utf-8 -*-
N = int(input())
coelho,rato,sapo = 0,0,0
total = coelho+rato+sapo

for _ in range(N):
    quant,tipo = input().strip().split(' ')
    quant = int(quant)
    if tipo == 'C':
        coelho += quant
    elif tipo == 'R':
        rato += quant
    else:
        sapo += quant

total = coelho+rato+sapo

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {coelho/total *100:.2f} %')
print(f'Percentual de ratos: {rato/total *100:.2f} %')
print(f'Percentual de sapos: {sapo/total *100:.2f} %')
```
