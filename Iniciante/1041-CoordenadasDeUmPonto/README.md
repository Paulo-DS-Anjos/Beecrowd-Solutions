# 1041 - Coordenadas de um Ponto

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1041)

Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

![1041 Beecrowd](https://resources.beecrowd.com/gallery/images/problems/UOJ_1041.png)

Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

### Entrada:
A entrada contem as coordenadas de um ponto.

### Saída:
A saída deve apresentar o quadrante em que o ponto se encontra.

## Solução

A abordagem que eu usei aqui foi uma baseada em mais ou menos como nós faríamos para identificar um quadrante na vida real. Primeiro testamos a coordenada X e depois a coordenada Y e respondemos de acordo. Há diversas formas diferentes de montar as estruturas de condicionais deste problema (eu mesma resolvi de uma maneira completamente diferente dessa abaixo quando resolvi o exercício pela primeira vez). Tente pensar na forma que faz mais sentido para você.
