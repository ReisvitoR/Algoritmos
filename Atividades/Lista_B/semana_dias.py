#Q26. Ler um número inteiro de dias, calcular e escrever quantas semanas e quantos dias ele corresponde

#entrada
dias = int(input("Digite o numero de dias: "))
#processamento
calculo_semanas = dias // 7
calculo_dias = dias % 7

#saida
print("{0} dias tem {1:.0f} semanas e {2} dias.".format(dias, calculo_semanas, calculo_dias))