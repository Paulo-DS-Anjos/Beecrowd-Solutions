# 1051 - Imposto de Renda

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1051)

Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.

![1051-ImpostoDeRenda-Beecrowd](https://resources.beecrowd.com/gallery/images/problems/UOJ_1051_pt.png)

Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.

### Entrada:
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

### Saída:
Imprima o texto "R$" seguido de um espaço e do valor total devido de Imposto de Renda, com duas casas após o ponto. Se o valor de entrada for menor ou igual a 2000, deverá ser impressa a mensagem "Isento".

## Solução

O cálculo do imposto de renda, tanto nesse exercício quanto na vida real, não é uma taxa que é aplicada ao salário inteiro de acordo com a faixa a qual ele pertence. Se esse fosse o caso, um salário de R$ 10500,00 teria que pagar R$ 2940,00 de imposto e um salário de R$ 4000,00 pagaria R$ 720,00.

Só que, na verdade, o imposto é aplicado à parte do salário que se encaixa na faixa, ou seja, a parte do salário que é de R$ 2000,00 a R$ 3000,00 é cobrada 8% dessa parte. Seguem os exemplos com os dois salários mencionados acima.

---

R$ 4000,00:

| Faixa | Parte do salário que cabe na faixa | Taxa | Imposto devido |
| - | - | - | -: |
| de R$ 2000,01 até R$ 3000,00 | R$ 1000,00 | 8% | R$ 800,00 |
| de R$ 3000,01 até R$ 4500,00 | R$ 1000,00 | 18% | R$ 180,00 |

**Imposto total:** R$ 980,00

---

R$ 10500,00:

| Faixa | Parte do salário que cabe na faixa | Taxa | Imposto devido |
| - | - | - | -: |
| de R$ 2000,01 até R$ 3000,00 | R$ 1000,00 | 8% | R$ 800,00 |
| de R$ 3000,01 até R$ 4500,00 | R$ 1500,00 | 18% | R$ 270,00 |
| acima de R$ 4500,00 | R$ 6000,00 | 28% | R$ 1680,00 |

**Imposto total:** R$ 2750,00

---

## Python 3.9

```Python
# -*- coding: utf-8 -*-
salario = float(input())
if salario <= 2000:
    print("Isento")
elif salario <= 3000:
    imposto = (salario-2000)*0.08
    print(f"R$ {imposto:.2f}")
elif salario <= 4500:
    imposto = 1000*0.08 + (salario-3000)*0.18
    print(f"R$ {imposto:.2f}")
else:
    imposto = 1000*0.08 + 1500*0.18 + (salario-4500)*0.28
    print(f"R$ {imposto:.2f}")
```
