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


