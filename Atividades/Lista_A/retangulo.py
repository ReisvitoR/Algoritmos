#Q.17 Ler o valor da base e altura de um retângulo, calcule e escreva sua área.

#entrada
base = float(input("Digite o valor da base do retangulo(m): "))
altura = float(input("Digite a altura do retangulo(m): "))

#processamento 
area = base * altura

#saida
print("A altura do retangulo é {}m e a base {}m, a área do retangulo vale {}m²".format(base, altura, area))