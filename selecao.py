from random import choices

# Para diversificar e atrair novos(as) clientes, uma lanchonete 
# criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". 
# Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor
# a salada de frutas da pessoa cliente. Crie o código que faça 
# essa seleção aleatória de acordo com a lista abaixo:

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

salada= choices(frutas , k=3)

print(f"A salada surpresa é : {salada[0]} , {salada[1]}, {salada[2]}")