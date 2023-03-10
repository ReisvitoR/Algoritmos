#Calcular velocidade km/h em velocidade m/s

#entrada
velocidade_kmh = float(input("Digite a velocidade em (km/h): "))

#processamento
velocidade_ms = velocidade_kmh / 3.6

#saida
print("A velocidade {0} km/h é igual á velocidade {1:.2f} em m/s".format(velocidade_kmh, velocidade_ms))