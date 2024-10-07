# 1071 - Soma de Impares Consecutivos I

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1071)

Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

### Entrada:
O arquivo de entrada contém dois valores inteiros.

### Saída:
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

## Solução

Como essa sequência de números ímpares pode ser considerado uma progressão aritmética e como já sabemos o primeiro e o último elemento de tal sequência, então podemos usar a fórmula de progressão aritmética para calcular a soma com complexidade constante.

O único detalhe é que precisamos saber quantos números há entre `X` e `Y`. Precisamos estipularmos `X` e `Y`, podemos calcular a quantidade de números ímpares entre `X` e `Y` inclusive fazendo `(X - Y)/2 + 1`, já que ambos os valores são ímpares, restando apenas somar 1 para contar o elemento `X` ou `Y`.

## Python 3.9

```Python
def numeroImpares(X, Y):
    return (Y - X)//2 + 1

def somaPA(X, Y):
    return (X + Y) * numeroImpares(X, Y)//2

X = int(input())
Y = int(input())

if X > Y:
    X, Y = Y, X

X += (X % 2) + 1
Y -= (Y % 2) + 1

print(somaPA(X, Y))
```
