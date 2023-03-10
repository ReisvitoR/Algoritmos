#Q.3 Minutos em horas e minutos

#entrada
minutos = int(input("Digite o valor total em minutos: "))

#processamento
horas = (minutos // 60)                              #apenas o todo da divisão
resto_minutos = (minutos % 60)                       #o resto da divisão

#saida
print("{0}min equivale a {1}hrs e {2} minutos.".format(minutos, horas, resto_minutos))
