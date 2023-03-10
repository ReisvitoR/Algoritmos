#Q.5 Dividir o numero em unidade, dezena e centenas

#entrada
numero = int(input("Digite um numero de até 3 digitos: "))

#processamento
centena  = (numero // 100)
resto = (numero % 100)
dezena = int(resto / 10)
unidade = (resto % 10)

soma = (centena + dezena + unidade)

#saida
print("O número {0}, tem como Centena {1}, Dezena {2} e unidade {3}. Suas somas são {4} .".format(numero, centena, dezena, unidade, soma))

