lista_numeros = []
# Repete 5 vezes
for i in range(5):
    # Peço um valor inteiro ao usuário.
    valor = int(input("Digite um número:\n"))
    # Adicionar a lista de numeros o valor do usuário
    lista_numeros.append(valor)
    
# Mostra a lista toda ao final do loop.
print(lista_numeros)