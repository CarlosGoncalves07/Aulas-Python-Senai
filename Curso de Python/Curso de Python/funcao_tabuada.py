# Crie uma função tabuada que imprima a tabuada de 1 a 10.
def tabuada(numero):
    for i in range(1,11):
        print(f"{numero}X{i}={numero*i}")
numero_usuario = int(input("Digite um numero"))
tabuada(numero_usuario)