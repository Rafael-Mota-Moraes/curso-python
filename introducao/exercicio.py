"""
Crie um programa que:

1 - (x) Mostre uma mensagem de boas-vindas na tela. 
2 - (x) Crie as seguintes variáveis:
    Nome do cliente (recebido com input);
    Idade do cliente (recebido com input e convertido para inteiro);
    Saldo disponível (recebido com input e convertido para float);
    Preço de um item da loja (valor fixo, por exemplo, 1500).
3 - (x) Mostre o tipo de cada variável utilizando a função type.
4 - (x) Faça um cálculo para verificar quanto sobra no saldo do cliente após a compra do item.
5 - (x) Exiba o resultado do cálculo utilizando f-strings.
6 - Crie uma lista de itens disponíveis na loja e mostre essa lista.
"""

print("Boas vindas a nossa loja.")

nome = input("Digite o nome do cliente: ")
idade = int(input("Digite a idade do cliente: "))
saldo = float(input("Digite o saldo disponível: "))
preco = float(input("Digite o preço do item: "))

print("\n")
print("#" * 20)
print("\n")

print(f"Tipo de nome: {type(nome)}")
print(f"O tipo de idade: {type(idade)}")
print(f"O tipo de saldo: {type(saldo)}")
print(f"O tipo do preço: {type(preco)}")

print("\n")
print("#" * 20)
print("\n")

restante = saldo - preco
print(f"Após a compra sobrou {restante} na sua conta")

print("\n")
print("#" * 20)
print("\n")

itens_disponiveis = ["Tênis", "Camisa", "Bermuda"]

print("Itens disponíveis.")
print(itens_disponiveis)