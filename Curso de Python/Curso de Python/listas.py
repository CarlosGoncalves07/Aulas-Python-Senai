lista_nomes = []


opcao = -1
while opcao != "0":
    opcao = input("[1] - Cadastrar Pessoa\n[2] - Remover Pessoa\n[0] - Sair\n")


    if opcao == "1":
        nome = input("Digite o nome que deseja cadastrar: ")
        lista_nomes.append(nome)


    elif opcao == "2":
        nome = input("Digite o nome de quem deseja remover: ")
        
    elif opcao == "0":
        print("Saindo do programa")
        #continuamos na próxima aula
    else:
        print("Opção inválida.")


print("A sua lista de nomes é:",lista_nomes)

#_____________________________________________________________-

nomes = ["Joaquim", "Maria", "Ana", "Ana"]
print = (nomes[0])
print = (nomes[1])
print = (nomes[2])
print = (nomes[3])

print[0] = "João" # estava Joaquim
# Apagou o Joaquim

nomes.append("Jãoao")
nomes.append("Joana")
    # Você adiciona novos nomes
    # Ordenar sempre deve ser a ultima ação. Se ele estiver antes do append, o nome não entra em ordem alfabética
lista_nomes.sort() # Ordenando a lista de nomes.

print(lista_nomes)

for indice,nome in enumerate(lista_nomes):
    print(indice,":", nome)
    # Percorrendo uma lista com o enumerate e printando ele com o indice

lista_nomes.pop() 
    # Também serve para remover objetos

lista_nomes.clear() 
    #Ele apaga todos os nomes da lista.

lista_nomes.insert(0,"Amarildo")  
    # Ele adiciona o elemento sem apagar outros

del lista_nomes[2]
    # Deleta um objeto especifico da lista [] ou a lista inteira

lista_nomes.remove("Zelina")

print(lista_nomes)