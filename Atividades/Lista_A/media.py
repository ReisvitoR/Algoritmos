#Q.14   Ler 3 notas de um aluno e o peso de cada nota, calcular e escrever a média ponderada

#entrada
nota1 = float(input("Digite sua primeira nota: "))
peso1 = float(input("Digite o peso da nota1: "))
nota2 = float(input("Digite sua segunda nota: "))
peso2 = float(input("Digite o peso da nota2: "))
nota3 = float(input("Digite sua terceira nota: " ))
peso3 = float(input("Digite o peso da nota3: "))

#processamento
soma = peso1 + peso2 + peso3
media = ((peso1*nota1) + (peso2 * nota2) + (peso3 * nota3)) / soma

#saida
print("A primeira nota foi {:.2f} a segunda {:.2f} e a ultima {:.2f}, a média deu {:.2f} .".format(nota1, nota2, nota3, media))