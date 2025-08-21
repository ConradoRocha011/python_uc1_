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
 
# codigo do professor ⬇️
produtos = (
    ("Arroz", 5.99),
    ("Feijão", 7.49),
    ("Leite", 4.89),
    ("Óleo", 9.99),
    ("Açúcar", 3.29)
)

print("LISTA DE PRODUTOS")
for nome, preco in produtos:
    print(f"{nome:.<20} R$ {preco:.2f}")

total = 0
produtos = (
    ("Arroz", 5.99,"2Kg"),
    ("Feijão", 7.49,"3Kg"),
    ("Leite", 4.89,"2ML"),
    ("Óleo", 9.99,"1ML"),
    ("Açúcar", 3.29,"1Kg")
)

for produto, valor, peso in produtos:
    total+=valor
    print(f" O produto ->> {produto:*<10} ___ de valor do produto = {valor:.2f} -- Peso = {peso}")

desconto = total * 0.10
total_com_desconto = total - desconto

print(f"total da compra é R${total:.2f}")
print(f"\nTotal sem desconto: R${total:.2f}")
print(f"Desconto 10%: R${desconto:.2f}")
print(f"Total com desconto: R${total_com_desconto:.2f}")



 # faça um codigo que calcule a media do valor aleatorio - KKkkkk não sei se entend a questão mas fiz assim-⬇️

import random 
quantidade = random.randint(0, 100)  
numeros = []
for i in range(quantidade):
    numeros.append(random.randint(0, 100))

soma = sum(numeros)
media = soma / quantidade
print(f"A media de {quantidade} é ->>{media}")
"""
import random
qt_elemento=100
lista=[]
for i in range(qt_elemento):
    list.append(random.randint(1.999))
media=sum(list)/len(list)
print(f"A media dos valores é: {media:.2f}")
maior[]
menor[]
for valor in list:
    if valor > media:
        maiores.append(valor)
    else valor < media:
         menores.append(valor)
print(f"{maiores}")
print(f"{menor}")         