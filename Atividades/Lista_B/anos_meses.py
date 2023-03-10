#Q.29 Ler um número inteiro de meses, calcular e escrever quantos anos e quantos meses ele corresponde.

#entrada
meses = int(input("Digite o numero de meses: "))
 
#processamento
anos = meses // 12
resto_meses = meses % 12

#saida
print("{0} meses tem: {1} anos e {2} meses.".format(meses, anos, resto_meses))