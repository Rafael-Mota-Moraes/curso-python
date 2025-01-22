"""
Strings - São textos entre aspas

Podem ser declaradas tanto dentro de aspas
duplas quanto de aspas simples.
"isso é uma string" 'isso é uma string'

Caracter de escape: "Minha \"string\""

É melhor fazer: 'Minha "string"' ou "Minha 'string'"

Isso aqui tbm é uma string: "123"
E isso aqui tbm é uma string: '123.99'
E isso aqui tbm é uma string: '''123.99'''


Métodos úteis:
upper() - deixa tudo maiúsculo
lower() - deixa tudo minúsculo
split() - retorna uma lista (mais tarde vamos ver sobre listas)
replace() - substitui as coisas

Slice de strings
nome = "Rafael"
nome[0:3]
nome[1:3]
nome[0:6:2]

Uma forma de inverter a string:
nome[::-1]

"""

#               0123456789... 
minha_string = 'Minha "String"'
print(minha_string)
print(type(minha_string))
print(type("""123"""))

print("Métodos Úteis:")
outra_string = minha_string.upper()
print(outra_string)
print(outra_string)
print(outra_string.lower())
print(minha_string.split())
print(minha_string.replace('a', '#'))

print(minha_string[1])
print(minha_string[3:5])
print(minha_string[0:9:2])
print(minha_string[::-1])