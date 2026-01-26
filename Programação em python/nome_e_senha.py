#Faça um programa que leia um nome de usuário e a sua senha e não aceite a 
# senha igual ao nome do usuário, mostrando uma mensagem de erro e voltandoa pedir as informações.


nome = str(input("Digite o seu nome:\n"))
senha = str(input("Digite sua senha:\n"))


while senha == nome:
    print("Valor invalido")
    nome = str(input("Digite o seu nome:\n"))
    senha = str(input("Digite sua senha:\n"))
print("Bem vindo")