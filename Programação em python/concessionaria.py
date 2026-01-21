print("Hello World! ")

veiculo_01 = "Fiat"
modelo_01 = ("\nUno\nPalio\nFiorino")
veiculo_02 = "Volkswagem"
modelo_02 = ("\nGol\nVoyage\nT-cross")
veiculo_03 = "Ford"
modelo_03 = ("\nEcoSport\nFord Ka\nFocus")
cliente = str(input("Qual é o seu nome? \n"))

print(f"Olá {cliente}\nSeja bem vindo a concessionaria Center Autos\nÉ um prazer atende-lo(a)! ")

marca = int(input("Qual é a marca de interesse?\n(1-Fiat / 2-Volkswagem / 3-Ford)\n"))
if marca == 1:
    print("Ótima escolha! ")
    print("Os modelos disponiveis da {veiculo_01} são: {modelo_01}")
    print(input(f"Qual sera o modelo?\\n(1-Uno / 2-Palio / 3-Fiorino):\\n"))
    print("Parabéns pela compra")

elif marca == 2:
    print("Ótima escolha! ")
    print(f"Os modelos disponiveis da {veiculo_02} são: {modelo_02}")
    print(input(f"Qual sera o modelo?\n(1-Gol / 2-Voyage / 3-T-cross):\n"))
    print("Parabéns pela compra")

else:
    print("Ótima escolha! ")
    print(f"Os modelos disponiveis da {veiculo_03} são: {modelo_03}")
    print(input(f"Otima escolha\nQual sera o modelo?\n(1-EcoSport / 2-Ford Ka / 3-Focus):\n"))
    print("Parabéns pela compra")