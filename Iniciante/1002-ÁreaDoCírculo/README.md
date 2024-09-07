# 1002 - Área do Círculo

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1002)

A fórmula para calcular a área de uma circunferência é: `area = π . raio2`. Considerando para este problema que `π = 3.14159`:

- Efetue o cálculo da `área`, elevando o valor de `raio` ao `quadrado` e `multiplicando por π`.

### Entrada:
A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável `raio`.

### Saída:
Apresentar a mensagem `A=` seguido pelo valor da variável `area`, conforme exemplo abaixo, com `4 casas após o ponto decimal`. Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá `Presentation Error`.

## Solução

Só aplicar a fórmula da área direto, criamos uma variável para armazenar o valor do `raio` informado pelo usuário, logo após criar uma variável para guardar o valor de `pi` dado pelo enunciado ou usando o valor diretamente. Eu só coloquei o valor de `pi` como constante para fins didáticos e para sinalizar que este valor alocado não irá mudar de valor (e com isso, a execução do código se torna mais rápida).

Outro detalhe importante sobre esse problema é a forma como você precisa imprimir a saída com exatas `4 casas decimais`. Em python essa formatação é feita utilizando `:.nf`, onde `n` é o número de casas decimais após a vírgula, neste caso 4 casas.

## Python 3.9

```python
# -*- coding: utf-8 -*-
raio = float(input())
pi = 3.14159
area = pi*(raio**2)
print(f'A={area:.4f}')
```
