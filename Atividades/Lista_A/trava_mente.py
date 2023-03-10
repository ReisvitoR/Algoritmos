#Q7. Ler 3 numeros somar os 2 primeiros e subtrair os 2 ultimos

#entrada
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite um segundo numero: "))
numero3 = float(input("Digite o ultimo numero: "))

#processamento
soma = numero1 + numero2
diferenca = numero2 - numero3
  
#saida  
print("A soma dos primeiros valores: {0:.0f} e {1:.0f} ,são: {2:.0f}. A subtração dos dois ultimos valores {1:.0f} e {3:.0f}, são: {4:.0f} .".format(numero1, numero2, soma, numero3, diferenca))