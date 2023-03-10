#Q2- Ler um valor em horas e minutos e converter apenas para minutos

#Entrada
horas = int(input("Digite as Horas: "))
minutos = int(input("Digite os minutos: "))

#Processamento
horas_minutos = (horas * 60)
total = (horas_minutos + minutos)

#saida
print("{0}hrs e {1}min equivale a {2} minutos no total".format(horas, minutos, total))