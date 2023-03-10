#Q.10 calcular e escrever o quociente e o resto da divisão do primeiro pelo segundo

#entrada
numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite outro numero inteiro: "))

#processamento
coeficiente = numero1 // numero2
resto = numero1 % numero2

#saida
print("O Coeficiente de {0}/{1} é {2} e o resto da divisão é {3} .".format(numero1, numero2, coeficiente, resto))