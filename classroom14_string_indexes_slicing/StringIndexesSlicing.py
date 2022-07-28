"""
Manipulando strings

* String indices
* Fatiamento de strings (inicio: fim: passo)
* Funções buitt-in len, abs, type, print, etc...

Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso cm:
https:2/docs.python.org/3/library/stdtypes.html(tiposbuilt-in)
https://docs.python.org/3/Library/tunctions.html(funçõesbuflt-in)

"""

# Positivos         [01234567]
text_1         =    "python 3"
print(text_1[7]) # 3

# Negativos       -[87654321]
text_2        =     "python 3"
print(text_2[:-7]) # p

# fatiamento - slicing de string
new_string = text_1[1:6] # corta a string dentro do intervalo dos indices
print(new_string) # ython

new_string = text_1[:6] # cortar a string desde o inicio 0
print(new_string) # python

# Pulando indices na string de acordo com o segundo :
new_string = text_1[0:6:2] # cortar a string desde o inicio 0
print(new_string) # pto