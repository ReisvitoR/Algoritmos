#Q19. Ler o valor do raio de uma esfera, calcular e escrever seu volume

#entrada
raio = float(input("Digite o valor do raio de uma esfera (cm): "))

#processamento
volume = 4/3 * ((raio**3) * 3.14)

#saida
print("A esfera com o raio de {0:.2f}cm tem um volume de {1:.2f}cm³".format(raio, volume))