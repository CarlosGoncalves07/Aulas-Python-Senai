valor_total = float(input("Digite o valor total da compra: "))
valor_porcentagem = float(input("Digite a porcentagem de desconto: "))
valor_desconto = float(valor_total) * float(valor_porcentagem) / 100
print(f"O valor do desconto é: {valor_desconto}")
print(f"{valor_porcentagem}% de {valor_total} é igual a {valor_desconto}")