#aula08_pt02
#>>Crie uma programa python que use a função main() para calcular e imprimir a soma de dois números fornecidos pelo usuário<<
"""""
def saudacao():
    print("\n\n\tOlá, mundo!")

if __name__== "__main__":
    saudacao()
 
def main():

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite um numero novamente: "))
    
    #soma = numero1 + numero2
    
    print(f"A soma de {numero1} e {numero2} é igual a !!>>{soma}<<!!")

if __name__ == "__main__":
    main()


def soma(num1, num2):
   return num1 + num2

def subtracao(num1, num2):
   return num1 - num2

def main():
   resultado_soma = soma(5, 14)
   resultado_subtracao = subtracao(14, 5)
   print(f"Soma: >>{resultado_soma}<<")
   print(f"Subtração: >>{resultado_subtracao}<<")

if __name__ == "__main__":

   main()
"""
   