#Faça um programa que pergunte o preço de três produtos e informe qual
#produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


print("Hello World")

preco_produto_01 = float(input("Digite o valor do primeiro produto\n"))
preco_produto_02 = float(input("Digite o valor do segundo produto\n"))
preco_produto_03 = float(input("Digite o valor do terceiro produto\n"))



if preco_produto_01 < preco_produto_02:
    menor = preco_produto_01
else:
    menor = preco_produto_02
if preco_produto_03 < menor:
    menor = preco_produto_03


print(f"O produto mais em conta é o {menor}")





