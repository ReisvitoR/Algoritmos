#Q.30  Ler um número inteiro de minutos, calcular e escrever quantos dias, quantas horas e quantos minutos ele corresponde.

#entrada
minutos = int(input("Digite um valor inteiro em minutos: "))

#processo
dias = minutos // 1440
horas = minutos // 60
resto_minutos =  minutos % 60

#saida
print("{0} minutos tem: {1} dias, {2}hrs e {3} minutos.".format(minutos, dias, horas, resto_minutos))