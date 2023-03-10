#Q28. Ler um número inteiro de horas, calcular e escrever quantas semanas, quantos dias e quantas horas ele corresponde.

#entrada
horas = int(input("Digite um valor inteiro em (hrs): "))

#processamento
semanas = horas // 168
dias = horas // 24
resto_horas = horas % 24

#saida
print("{}hrs têm: {}semanas, {}dias e {}hrs.".format(horas, semanas, dias, resto_horas))