# 1021 - Notas e Moedas

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1021)

Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de `100, 50, 20, 10, 5, 2`. As moedas possíveis são de `1, 0.50, 0.25, 0.10, 0.05 e 0.01`. A seguir mostre a relação de notas necessárias.

### Entrada:
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

### Saída:
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

## Solução

Para entender o raciocínio para resolver este problema, consulte [1018 - Cédulas](../1018-Cédulas).

Entretanto, temos alguns detalhes aqui: é um pouco problemático obter o resto da divisão para números não inteiros. Por isso, eu decidi que seria uma boa armazenartodos os valores em um vetor e multiplicar por 100 todos os valores de moedas para transforma-los em inteiros para me certificar de que só faria manipulação com números inteiros.

Também simplifiquei o código para evitar repetições, fazendo com que na hora de imprimir os valores, também seja necessário dividir por 100 para tranformar os valores das moedas em números reais. Perceba que essas simplifações também podem ser usadas no exercício mencionado anteriormente.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
inteiro,fracao = [int(x) for x in input().strip().split('.')]
cedula = [100,50,20,10,5,2,100,50,25,10,5,1]
print('NOTAS:')
for x in cedula[:6]:
    print(f'{(inteiro // x):.0f} nota(s) de R$ {x:.2f}')
    inteiro %= x
fracao += inteiro*100
print('MOEDAS:')
for x in cedula[6:]:
    print(f'{(fracao//x):.0f} moeda(s) de R$ {(x/100):.2f}')
    fracao %= x
```


 
