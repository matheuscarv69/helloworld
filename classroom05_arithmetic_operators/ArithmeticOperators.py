"""
Arithmetic Operators

// -> divisao inteira(arredonda o resultado)
** -> potenciacao
%  -> modulo (resto da divisao)

"""
print('Operacoes Comuns')

print('Adicao: 2 + 2 ', 2 + 2, sep=' = ')
print('Subtracao: 10 - 4 ', 10 - 4, sep=' = ')
print('Multiplicacao: 5 * 5', 5 * 5, sep=' = ')
print('Divisao: 25 / 5', 25 / 5, sep=' = ')

print('\nOrdem de Precedencia')
print('Equacao: 5 * 10 + 20', 'expected = 70 -> result', 5 * 10 + 20, sep=' = ')
print('Equacao: 5 * (10 + 20)', 'expected = 150 -> result', 5 * (10 + 20), sep=' = ')

"""
Abaixo, segue uma lista mais precisa de quais operadores tem maior prioridade na 
hora de realizar contas mais complexas (de maior para menor precedência).

1. ( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são 
realizadas primeiro

2. ( ** ) - Depois vem a exponenciação

3. ( * / //  % )-> Na sequência multiplicação, divisão, divisão inteira e módulo

4. ( +  - ) -> Por fim, soma e subtração

Contas com operadores de mesma precedência são realizadas da esquerda para a direita.

Observação: existem muito mais operadores do que estes em Python e todos eles 
também têm precedência, você pode ver a lista completa em 
https://docs.python.org/3/reference/expressions.html#operator-precedence
(sempre utilize a documentação oficial como reforço caso necessário).

"""

print('\nOutras Operacoes')
print('Potenciacao: 2ˆ2', 2 ** 2, sep=' = ')
# Divisao Inteira arredonda o resultado caso ele tenha casa decimais
print('Divisao Inteira: 10//3', 10 // 3, sep=' = ')
print('Modulo: 45 % 4', 45 % 4, sep=' = ')

print('\nOutras Particularidades')
print('Multiplicacao com tipo string: "3 * matheus"', 3 * 'matheus ', sep=' - ')
