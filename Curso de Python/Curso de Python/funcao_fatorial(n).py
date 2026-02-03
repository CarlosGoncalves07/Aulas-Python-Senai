print("Hello, World!")

def somar():
    while True:
        a = input("Digite o primeiro número:\n")
        b = input("Digite o segundo número:\n  ")
        try:
            numero_a = int(a)
            numero_b = int(b)
            return(numero_a + numero_b)
        except:
            print("Entrada inválida. Por favor digite um número:\n")


resultado = somar()
print(resultado)