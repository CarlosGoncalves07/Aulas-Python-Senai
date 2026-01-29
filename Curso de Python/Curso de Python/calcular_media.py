# Crie uma função calcular_media(n1,n2,n3) que calcule a média e informe se é maior ou igual a 7.
print("Hello, World")
def calcular_media(nota1,nota2,nota3):
    n1 = int(input("Digite a primeira nota:\n"))
    n2 = int(input("Digite a segunda nota:\n"))
    n3 = int(input("Digite a terceira nota:\n"))
    if resultado >= 7:
        print(f"O resultado é maior do que 7:\n Resultado: {resultado:.2f}")
    else:
        print(f"O resultado é menor do que 7:\n Resultado {resultado:.2f}")

resultado = (n1 + n2 + n3)/3

print("Hello, World!")
def contar_ate_n(numero):
    for i in range(1,numero+1):
        print(i)
contar_ate_n(10)
