# Criando uma matriz 3x3
import random
"""""
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
"""
matriz_2 = []

#print(f"{matriz}")

for i in range(4):
    linha = []
    for j in range (7):
        #linha.appende(random.randint(0,100))
        elemento = random.randint(0,100)
        linha.append(elemento)
    matriz_2.append(linha)


#print(f"{matriz_2[0]}")
for linha in matriz_2:
    print(f"{linha}")        
