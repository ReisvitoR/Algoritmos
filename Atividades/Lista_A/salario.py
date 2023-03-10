#Q.12 Escrever um salario que teve aumento de 25%

#entrada
salario = float(input("Digite o seu Salario R$: "))

#processamento
aumento = (salario * (25/100))
salario_novo = aumento + salario

#saida
print("Seu salario no valor de {0:.2f}R$ ,ganhou um acressimo de {1:.2f}R$ e aumentou para: {2:.2f}R$85 ".format(salario, aumento, salario_novo))