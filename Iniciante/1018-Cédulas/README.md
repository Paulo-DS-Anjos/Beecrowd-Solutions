# 1018 - Cédulas

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1018)

Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de `100, 50, 20, 10, 5, 2 e 1`. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro `N (0 < N < 1000000)`.

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: `Presentation Error`.

## Solução

A ideia deste problema é ir utilizando divisões e restos de divisão para ir dividindo o número recebido em pedaços adequados de acordo com o enunciado, mais ou menos como faríamos se fôssemos resolver esse problema na vida real.

Por exemplo, com o número 576, seguimos o seguinte raciocínio:

1. R$ 576,00 precisa de 5 notas de R$ 100,00 porque 576/100 = 5 (divisão inteira);
2. Beleza, representamos 500, então agora sobra 76;
3. R$ 76,00 precisa de 1 nota de R$ 50,00 porque 76/50 = 1;
4. OK, agora temos 26;
5. R$ 26,00 precisa de 1 nota de R$ 20,00 porque 26/20 = 1;
6. Temos 6;
7. R$ 6,00 precisa de 0 nota de R$ 10,00 porque 6/10 = 0;
8. Continuamos com 6;
9. R$ 6,00 precisa de 1 nota de R$ 5,00 porque 6/5 = 1;
10. Agora só sobrou 1;
11. R$ 1,00 precisa de 0 nota de R$ 2,00 porque 1/2 = 0;
12. Continua sobrando 1;
13. Agora o que sobrou é o que dá para representar com 1 nota de R$ 1,00.

Dessa maneira, nossa resposta final são 5 notas de R$ 100,00, 1 nota de R$ 50,00, 1 de R$ 20,00, 1 de R$ 5,00 e 1 de R$ 1,00. Experimente com outros valores de `N` e veja que pegar as divisões inteiras e seus respectivos restos forma um raciocínio interessante para a resolução deste e dos próximos problemas subsequentes.

## Python

```Python
# -*- coding: utf-8 -*-
N = int(input())

print(N)
print(f'{N//100} nota(s) de R$ 100,00')
N %= 100
print(f'{N//50} nota(s) de R$ 50,00')
N %= 50
print(f'{N//20} nota(s) de R$ 20,00')
N %= 20
print(f'{N//10} nota(s) de R$ 10,00')
N %= 10
print(f'{N//5} nota(s) de R$ 5,00')
N %= 5
print(f'{N//2} nota(s) de R$ 2,00')
N %= 2
print(f'{N//1} nota(s) de R$ 1,00')
```
