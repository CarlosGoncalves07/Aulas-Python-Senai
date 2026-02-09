#  Faça um Programa que leia 4 notas, mostre as notas e a média na tela
lista_notas = []
for i in range(4):
    nota = int(input(f"Digite a nota {i+1} do aluno:\n "))
    lista_notas.append(nota)
            #sum() -> soma todas as notas #len() -> devolve o tamanho da lista
media_notas = sum(lista_notas)/len(lista_notas)
print(media_notas)
