# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = str(input("Digite o seu nome:\n"))
while len (nome) < 3:
    nome = str(input("Digite o seu nome:\n"))

idade = int(input("Digite a sua idade:\n"))
while (idade) < 0 and (idade) > 150:
   idade = int(input("Digite a sua idade:\n"))

salario = float(input("Digite o seu salário:\n"))
while salario < 0:
    salario = float(input("Digite o seu salário:\n"))

letra = input("Digite a letra: (F-feminino / M-masculino)\n").upper()
if letra == "F":
    print("Feminino")
elif letra == "M":
    print("Masculino")
else:
    print("Sexo invalida")

estado_civil = str(input("Digite seu Estado Civil: (S-Solteiro/C-casado/V-Viuvo/D-Divorciado\n) ")).upper()
while estado_civil == "S" or == "C" == ""/C/V/D":

    if estado_civil == "S":
        print("Solteiro")
    
    elif estado_civil == "C":
        print("Casado")

    elif estado_civil == "V":
        print("Viuvo")

    elif estado_civil == "D":
        print("Divorciado")
        
    else:
    print("Opção invalida")
