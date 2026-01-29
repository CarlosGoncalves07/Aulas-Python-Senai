# Crie uma função contar_pares(inicio,fim) que conte quantos numeros pares existem no intervalo.

print("Hello, World!")
def contar_pares(inicio,fim):
    contador = 0

    for i in range(inicio,fim+1):
        if i % 2 == 0:
            contador += 1
            print(i)
    return contador

print(contar_pares(1,10))


