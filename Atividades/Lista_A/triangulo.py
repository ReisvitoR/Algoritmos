#Q.15 Ler o valor da base e altura de um triângulo, calcular e escrever a área.

#entrada
base = float(input("Digite a o valor da base do triangulo(m): "))
altura = float(input("Digite o valor da altura do triangulo(m): "))

#processamento
area =  (base * altura) /2

#saida
print("A altura do triangulo mede {0}m e a base {1}m , tendo uma aréa de {2} m²".format(base,altura, area))