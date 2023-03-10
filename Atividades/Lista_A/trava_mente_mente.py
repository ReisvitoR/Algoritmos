#Q.8 Ler 2 números, calcular e escrever a divisão da soma pela subtração dos números lidos.
#entrada
numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite um outro numero: "))

#processamento
soma = numero1 + numero2
subtracao = numero1 - numero2
divisao = soma / subtracao

#saida
print("A soma dos dados foi: {:.2f}, a subtração {:.2f}, e a divisão desses resultados é {:.2f}.".format(soma, subtracao, divisao))