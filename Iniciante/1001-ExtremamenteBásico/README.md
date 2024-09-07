# 1001 - Extremamente Básico

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1001)

Leia 2 valores inteiros e armazene-os nas variáveis `A` e `B`. Efetue a soma de `A` e `B` atribuindo o seu resultado na variável `X`. Imprima `X` conforme exemplo apresentado abaixo. Não apresente mensagem alguma além daquilo que está sendo especificado e não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá `Presentation Error`.

### Entrada:
A entrada contém 2 valores inteiros.

### Saída:
Imprima a mensagem `X = ` (letra X maiúscula) seguido pelo valor da variável `X` e pelo final de linha. Cuide para que tenha um espaço antes e depois do sinal de igualdade, conforme o exemplo abaixo.

## Solução

Um problema bem simples que envolve ler dois valores e imprimir a soma dos dois valores lidos. Nesta [página da beecrowd](https://www.beecrowd.com.br/judge/pt/faqs/about/examples) ela oferece as soluções deste problema para diversas linguagens.

A diferença entre os exemplos apresentados acima e o apresentado abaixo é que no link acima é criada uma variável `X` que armazena a soma de `A` e `B`, não né algo obrigatório porém, para fins de aprendizado é algo bem interesante de se usar.

### Python 3.9

```python
A = int(input())
B = int(input())

print(f"X = {A + B}")
```
