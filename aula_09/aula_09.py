#Criando e imprimindo uma lista

# exemplo de vetor
#vetor = [10, 20, 30, 40, 50]
#print=(f"dados do vetor:" {vetor[5]})
#for elemento in vetor:
    # print(f"valor do Elemento: {elemento}")

     #valor do primeiro elemento



"""for i in range(21):
    if i == 10:
        print(f"o primeiro valor é: {i}")
    elif i == 20:
        print(f"o valor agora é: {i}")


# Se você quer apenas imprimir números de 0 a 49:
for i in range(50):
    soma = sum(range(50))
print(f"Soma total: {soma}")




import random  
numeros = []
for i in range(1000):
     numeros.append(random.randint(1, 1000)) 
     
soma=sum(numeros)
maior=max(numeros)
menor=min(numeros)
qt_elementos=len(numeros)
media=soma/qt_elementos
print(f"media dos numeros é >>{media}<< - sua soma é >>{soma}<< - o maior entre eles é >>{maior}<< - o menor entre eles é >>{menor}<< - a quantidade de elementos igual a >>{qt_elementos}<<")
"""
import random 
numero = []

numero=random.randint(1,1200)
print(f"o range é: >>>>{numero}")

par = []
impar =[]

for i in range(numero):
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f"Numeros pares: \n\t{par}\n")

print(f"Numeros pares: \n\t{impar}\n")

print(f"QT -> Numeros pares: {len(par)}")
      
print(f"QT -> Numeros impares: {len(impar)}")