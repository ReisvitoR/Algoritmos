#Q13 Ler um valor em real R$ e calcula 70% deste valor. 

#entrada
numero = float(input("Digite um valor(R$): "))

#processamento
valor = numero * (70/100)  #ou 0.70

#saida
print("Os 70%"  "do valor {:.2f} R$ é de {:.2f} R$".format(numero, valor))
