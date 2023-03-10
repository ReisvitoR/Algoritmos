#Q.21 Ler uma temperatura em °F, calcular e escrever a equivalencia em °C.

#entrada
temperatura_fahrenheit = float(input("Digite o valor em °F: "))

#processamento
temperatura_celsius = ((temperatura_fahrenheit * 5) - 160) / 9

#saida
print("A temperatura em fahrenheit {0:.2f}°F equivale a temperatura em Celsius {1:.2f}°C.".format(temperatura_fahrenheit, temperatura_celsius))