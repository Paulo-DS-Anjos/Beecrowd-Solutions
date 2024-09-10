# 1019 - Conversão de Tempo

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1019)

Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato `horas:minutos:segundos`.

### Entrada:
O arquivo de entrada contém um valor inteiro `N`.

### Saída:
Imprima o tempo lido no arquivo de entrada (segundos), convertido para `horas:minutos:segundos`, conforme exemplo fornecido.

## Solução

Para calcular o número de horas cheias que existem em um tempo em segundos, basta pegar a divisão inteira deste tempo por 3600, a quantidade de segundos em uma hora. Após pegar o número de horas cheias, a única informação que permanece relevante é o resto da divisão por 3600, já que o resto você já converteu em horas. Seguindo um raciocínio similar para os minutos, podemos calcular rapidamente os valores que precisamos. Vamos testar nossa ideia com 140153 segundos.

1. Tem 38 horas completas em 140153 segundos, que calculamos dividindo 140153/3600;
2. Fora dessas 38 horas completas, temos 3353 segundos que podemos continuar convertendo (resto da divisão de 140153 por 3600);
3. Tem 55 minutos nestes 3353, pois 3353/60 = 55;
4. Fora desses 55 minutos completos, sobraram 53 segundos;
5. Logo, nossa resposta é 38 horas, 55 minutos e 53 segundos.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
N = int(input())

horas = N//3600
N %= 3600
minutos = N//60
segundos = N%60

print(f'{horas}:{minutos}:{segundos}')
```
