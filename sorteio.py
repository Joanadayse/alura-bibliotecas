from random import randint
# Um programa deve ser escrito para sortear uma pessoa seguidora de 
# uma rede social para ganhar um prêmio. 
# A lista de participantes é numerada e devemos escolher aleatoriamente 
# um número de acordo com a quantidade de participantes. 
# Peça à pessoa usuária para fornecer o número de participantes do sorteio
#  e devolva para ela o número sorteado.
n= int(input("Digite o numero de participantes para o sorteio: "))
print(f"O numero sorteado foi : {randint(1,n)}")