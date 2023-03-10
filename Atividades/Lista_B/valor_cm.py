#Q.24 Ler um valor em m, calcular e escrever o equivalente em centimetros.

#entrada
metros = float(input("Digite o valor em (m): "))

#processamento
centimetros = metros * 100

#saida
print("Os {0:.2f}m equivale {1:.2f}cm.".format(metros, centimetros))
