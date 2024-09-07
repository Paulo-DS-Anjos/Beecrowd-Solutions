# 1015 - Distância Entre Dois Pontos

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1015)

Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, `p1(x1,y1)` e `p2(x2,y2)` e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

Distancia = <img src="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}\sqrt[2]{(x2-x1)^{2}+(y2-y1)^{2}}" title="\bg_white Raiz Quadrada" /> 

### Entrada:
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de `ponto flutuante: x1 y1` e a segunda linha contém dois valores de `ponto flutuante x2 y2`.

### Saída:
Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.

## Solução

Aplicação direta da fórmula apresentada no enunciado. Para a maioria das linguagens, é necessário recorrer a uma biblioteca externa para usar a operação da raiz quadrada.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
import math
x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())
print(f'{(math.sqrt((x2-x1)**2 + (y2-y1)**2)):.4f}')
```
