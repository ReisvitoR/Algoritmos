#Q.20 Ler uma temperatura em °C, calcular e escrever a equivalente em °F.

#entrada
temperatura_celsius = float(input("Digite a temperatura em °C: "))

#processamento
temperatura_fahrenheit = ((temperatura_celsius * 9) + 160) / 5 

#saida
print("{0:.1f}°C equivale à {1:.1f}°F".format(temperatura_celsius, temperatura_fahrenheit))