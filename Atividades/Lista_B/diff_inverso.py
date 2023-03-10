#Q.32 Ler um número inteiro (3 dígitos), calcular e escrever a diferença entre o número e seu inverso.

#entrada
numero = int(input("Digite um numero inteiro com 3 digitos: "))

#processamento
centena = numero // 100
resto = numero % 100
dezena = resto //10 
unidade = resto % 10
diferenca = (numero - centena) + (numero - dezena) + (numero - unidade)

#saida
print("O numero {0} tem valor inverso {3}{2}{1} e sua diferença é {4}".format(numero, centena, dezena, unidade, diferenca))