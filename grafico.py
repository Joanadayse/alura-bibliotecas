import matplotlib.pyplot as plt


estudantes= ["maria", "jose", "joao"]
notas=[10,5,8.9]

plt.bar(x=estudantes , height=notas)

plt.xlabel("Estudantes")
plt.ylabel("Notas")
plt.title("Notas dos Estudantes")




plt.show();