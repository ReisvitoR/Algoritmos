#Q.4 Converter dolar em real

#entrada
dolar = float(input("Digite um valor em Dolar($): "))

#processamento
real = (dolar * 5.20)             #cotação atual: 5,20 Reais para 1 dolar.

#saida
print("{0} em dolar($) equivale à {1} em Real (R$)".format(dolar, real))