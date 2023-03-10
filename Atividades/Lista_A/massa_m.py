#Q23. Ler um valor em kg (quilograma), calcular e escrever o equivalente em g (grama)

#entrada
quilo = float(input("Digite um valor em (kg): "))

#processamento
grama = quilo * 1000

#saida
print("{0:.2f}kg equivale à {1:.2f}gramas.".format(quilo, grama))