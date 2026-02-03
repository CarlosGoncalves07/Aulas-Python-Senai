print("Hello, World!")

def somar(a,b):
    return(a+b)
a = int(input("Digite o primeiro número:\n"))
b = int(input("Digite o segundo número:\n  "))
resultado = somar(a,b)
try:
    a,b !=int
    print("O resultado é", resultado)
except Exception as erro:    
    print("Ocorreu um erro:",erro )

print(somar(a,b))

    
