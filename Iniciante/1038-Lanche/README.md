# 1038 - Lanche

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1038)

Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.



### Entrada:
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

### Saída:
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

## Solução

Podemos abordar o problema de várias maneiras, vou mostrar duas bem simples, uma delas é utilizando as condicionais `if`, `elif` e `else`, para todas as linguagens que suportam a diretiva `switch`, aqui está um exemplo bem simples de como ele funciona na prática, em python não temos essa condicional. Outra maneira de resolver é guardar os preços em vetores e acessá-los diretamente, o que resultou num código bem mais curto. Também é possível seguir essa abordagem do Python em outras linguagens.

## Python

### Método 1:

```Python
# -*- coding: utf-8 -*-
p1 , p2 = map(int, input().split())
if p1 == 1:
    print(f'Total: R$ {(p2*4):.2f}')
elif p1 == 2:
    print(f'Total: R$ {(p2*4.5):.2f}')
elif p1 == 3:
    print(f'Total: R$ {(p2*5):.2f}')
elif p1 == 4:
    print(f'Total: R$ {(p2*2):.2f}')
elif p1 == 5:
    print(f'Total: R$ {(p2*1.5):.2f}')
```

### Método 2:

```Python
# -*- coding: utf-8 -*-
codigo, quantidade = [int(x) for x in input().strip().split(' ')]
precos = [4.00, 4.50, 5.00, 2.00, 1.50]

total = quantidade * precos[codigo - 1]

print(f"Total: R$ {total:.2f}")
```
