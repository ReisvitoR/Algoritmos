#Q1, ler uma velocidade em metros por segundo e transformar em km por hr

#Entrada
velocidade_ms = float(input('Digite uma velocidade em m/s: '))

#Processamento
velocidade_kmh = (velocidade_ms * 3.6)

#Saida
print("A velocidade {0} em m/s equivale a {1} km/h ".format(velocidade_ms, velocidade_kmh))