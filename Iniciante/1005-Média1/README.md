# 1005 - Média 1

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1005)

Leia 2 valores de ponto flutuante de dupla precisão `A` e `B`, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota `A` tem peso `3.5` e a nota `B` tem peso `7.5` (A soma dos pesos portanto é `11`). Assuma que cada nota pode ir de `0` até `10.0`, sempre com uma casa decimal.

### Entrada:
O arquivo de entrada contém 2 valores com uma casa decimal cada um.

### Saída:
Imprima a mensagem `MEDIA` e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá `Presentation Error`.

## Solução

Só precisamos aqui fazer o cálculo direto da média ponderada, ou seja, calcular a expressão <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;\text{Media}&space;=&space;\frac{3,5&space;\times&space;A&space;+&space;7,5&space;\times&space;B}{11}" title="\bg_white \text{Media} = \frac{3,5 \times A + 7,5 \times B}{11}" />.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
A = float(input())
B = float(input())
MEDIA = ((A*3.5) + (B*7.5))/11
print(f'MEDIA = {MEDIA:.5f}')
```
