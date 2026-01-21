#Faça um Programa que pergunte quanto você ganha por hora e o número de
#horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print("Hello World")

valor_hora = float(input("Digite o seu ganho por hora: "))
horas_trabalhadas = float(input("Quantas horas voce trabalha por mes?:"))
valor_total = valor_hora * horas_trabalhadas
print(f"Seu ganho mensal é: {valor_total:.2f}")