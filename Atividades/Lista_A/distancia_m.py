#Q.22 Ler um valor em km, calcular e escrever o equivalente em metros.

#entrada
quilometros = float(input("Digite o valor em (km): "))

#processamento
distancia = quilometros * 1000

#saida
print("{0:.2f}km equivale à {1:.2f}m".format(quilometros, distancia))