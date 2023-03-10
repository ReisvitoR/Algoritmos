#Q.11 escrever o numero 3 digitos de forma inversa ex: 233 fica 332.

#entrada
numero1 = int(input("Digite um numero inteiro de até 3 digitos: "))

#processo                

centena = numero1 // 100
resto = numero1 % 100
dezena =  resto // 10                           #separa os numero por casas e dps inverte a ordem. ex: Unidade, dezena e centena!
unidade =  resto % 10

#saida
print("O numero {0}, invertido fica {3}{2}{1}".format(numero1, centena, dezena, unidade))