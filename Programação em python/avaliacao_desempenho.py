print("Hello World")

nome = str(input("Digite o seu nome: \n"))
nota_01 = float(input("Digite a primeira nota: \n"))
nota_02 = float(input("Digite a segunda nota: \n"))
nota_03 = float(input("Digite a terceira nota: \n"))

media = (nota_01 + nota_02 + nota_03) / 3

if media >= 7:
    print("Parabéns, você foi aprovado!")
elif media >= 4:
    print("Você está em recuperação:")
else:
    print("Reprovado! ")