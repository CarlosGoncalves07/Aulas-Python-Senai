#Faça um Programa que pergunte em que turno você estuda. Peça para digitar
#M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!",
#"Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print("Hello World")

turno_estudo = input("Digite o turno que você estuda:\
                     \n(M-Matutino)\
                     \n (V-Vespertino)\
                     \n(N-Noturno)\n").upper()
if turno_estudo == "M":
    print("Bom Dia!")
elif turno_estudo == "V":
    print("Boa tarde!")
elif turno_estudo == "N":
    print("Boa noite!")
else:
    print("Valor invalido!")

                     