from random import randrange

# Você recebeu uma demanda para gerar números de token para acessar o 
# aplicativo de uma empresa. O token precisa ser par e variar de 1000 
# até 9998. Escreva um código que solicita à pessoa usuária o seu nome 
# e exibe uma mensagem junto a esse token gerado aleatoriamente.

# "Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"

nome=input("qual o seu nome: ")
token=randrange(1000,10000,2)
print(f"Ola {nome} seu token de acesso será {token} , Seja Bem vindo(a)")