# 1006 - Média 2

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1006)

Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

### Entrada:
O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).

### Saída:
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade. Assim como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

## Solução

Parecido com o problema [1005-Média1](../1005-Média1), só que com os pesos somando 10 dessa vez.

## Python

```Python
# -*- coding: utf-8 -*-
A = float(input())
B = float(input())
C = float(input())
MEDIA = (A*2 + B*3 + C*5) / 10
print(f"MEDIA  = {MEDIA:.1f}")
```
