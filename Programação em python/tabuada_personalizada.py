print("Hello World! ")
numero = float(input("Digite um numero:\n "))
inicio = int(input("Qual sera o inicio da tabuada? \n"))
final = int(input("Até qual numero o multiplicador deve ir? \n"))


for multiplicador in range(inicio,final+1):
    print(f"{numero} x {multiplicador} = {numero*multiplicador}")



numero = int(input("Digite o número da tabuada que deseja: "))
inicio_tabuada = int(input("Digite o início da tabuada: "))
fim_tabuada = int(input("Digite o final da tabuada: "))


while inicio_tabuada <= fim_tabuada:
    print(f"{numero * inicio_tabuada}")
    inicio_tabuada += 1

#numero = int(input("Digite o número da tabuada que deseja: "))
#inicio_tabuada = int(input("Digite o início da tabuada: "))
#fim_tabuada = int(input("Digite o final da tabuada: "))


#for variavel_temporaria in lista_elementos
#for multiplicador in range(inicio_tabuada, fim_tabuada + 1):
#   print(f"{numero} X {multiplicador} = {numero*multiplicador}")