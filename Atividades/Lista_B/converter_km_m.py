#Q.25 Ler um número inteiro de metros, calcular e escrever quantos Km e quantos metros ele corresponde.

#entrada
metros = int(input("Digite um numero inteiro em (m): "))

#processamento
calculo_km = metros // 1000
calculo_m = metros % 1000

#saida
print("{0:.2f} metros equivale {1:.2f}km e corresponde a {2:.2f} metros. ".format(metros, calculo_km, calculo_m))