"""
string = '0123456789012345678901234567890123456789012345678901234567890123456789'
list_separated_nums = ['0123456789', '0123456789', '0123456789', '0123456789', '0123456789', '0123456789', '0123456789']
last_modification = '0123456789.0123456789.0123456789.0123456789.0123456789.0123456789.0123456789'

"""

string = '0123456789012345678901234567890123456789012345678901234567890123456789'

"""
Usamos o slicing na string para verificar o intervalo de cada grupo de 0 a 9
slicing funciona em tipo iteraveis (string, listas ...)

com isso verificamos que o salto é de 10 em 10 para termos um grupo de 0 a 9
"""
teste = string[0:10]
teste2 = string[10:20]
print(teste)
print(teste2)

"""
Criamos essa variavel para ficar mais simples o entendimento posterior
"""
salto = 10

"""
Criamos essa tupla para simples entendimento da logica de como o slincing ira funcionar 
nessa solucao.

- logica do range
Usando um list_comprehension para criar uma tupla, onde a variavel 'inicio' iremos obter
do range(start, end, step), então passamos para ele o numero de inicio do range, no caso 0
o final desse range será o tamanho da string, e como step passamos o salto que é 10.

Logo esse range irá de 0 até o tamanho da string pulando de 10 em 10

- logica da tupla
Agora na montagem da tupla, vamos querer dois valores, o inicio do grupo e o final do grupo
por conta disso temos (inicio), onde inicio(posicao na string) será 0 por causa do que foi definido no range,
e (inicio + salto), pois queremos pegar a posicao final do grupo que trata-se da posicao de inicio + o salto que 
é o intervalo entre cada grupo de (0123456789)
"""
tupla_de_intervalos_da_string = [(inicio, inicio + salto) for inicio in range(0, len(string), salto)]
print(tupla_de_intervalos_da_string)

"""
- logica de montar a lista com os grupos separados
Com a lógica explicada acima fica facil utilizar o slicing direto na string,
logo dentro do próprio list_comprehension fazemos o slicing diretamente na string
passando as informações de posicao de inicio do grupo - inicio, e a posicao final do grupo
para o slicing inicio + salto.

Dessa forma teremos os grupos separados diretamente da string utilizando o range para definir
as posicões de inicio para cada grupo

"""
lista_com_grupos_separados = [string[inicio: inicio + salto] for inicio in range(0, len(string), salto)]
print(lista_com_grupos_separados)

"""
- logica para montar string com todos os grupos separados por . 


Usamos a função Join das String
Ela basicamente retorna a junção de duas strings, no nosso caso queremos juntar
cada grupo com um .       
"""
string_de_grupos_separados_por_ponto = '.'.join(lista_com_grupos_separados)
print(string_de_grupos_separados_por_ponto)