#Q.27 Ler um número inteiro de segundos, calcular e escrever quantas horas, quantos minutos e quantos segundos ele corresponde.

#entrada 
segundos = int(input("Digite um numero inteiro correspondente aos segundos: "))

#processamento
horas = segundos // 3600
minutos = segundos // 60
resto_segundos = segundos % 60
 
#saida
print("{0} segundos tem {2}hrs, {1}min e {3}segundos".format(segundos, minutos, horas, resto_segundos))