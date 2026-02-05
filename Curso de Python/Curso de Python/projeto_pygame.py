# import pygame

# # Inicializar o pygame
# pygame.init()

# # Configurações da janela
# # Letras garrafais maiusculas são usadas para indicar constantes no codigo (algo que não será alterado)
# LARGURA = 800
# ALTURA = 600
# tela = pygame.display.set_mode((LARGURA,ALTURA))
# pygame.display.set_caption("Exemplo com Pygame.")

# # Definindo um clock para controlar FPS (Frames por Segundo)
# clock = pygame.time.Clock()
# FPS = 60

# # Definindo a posição x e y do retângulo.
# posicao_x_retangulo = LARGURA // 2
# posicao_y_retangulo = ALTURA // 2
# # Definindo a posição y do retângulo.
# velocidade_x_retangulo = 5
# velocidade_y_retangulo = 5

# rodando = True
# while rodando:
#     # Procurando por eventos
#     for evento in pygame.event.get():
#         # Se o evento fechar o jogo existir
#         if evento.type == pygame.QUIT:
#             # Muda a variavel rodando para False (fecha o loop)
#             rodando = False
            
#     # Fim do Loop de eventos

#     # Logica de movimento do retangulo
#     posicao_x_retangulo += velocidade_x_retangulo
#     posicao_y_retangulo += velocidade_y_retangulo


#     # Pinta a tela toda de branco
#     tela.fill((255,255,255))
#                     #(tela, cor, (coord_x, coord_y, largura,altura))
#     pygame.draw.rect(tela, (0,0,0), (400,300,50,50))

#     # Aqui desenhamos elementos gráficos.

#     pygame.display.flip()
#     clock.tick(FPS)

#     # Atualiza a tela
#     pygame.display.update()

# pygame.quit()

#_________________________________________________________________

import pygame
import random

def mudar_cores():
    vermelho = random.randint(0,255)
    verde = random.randint(0,255)
    azul = random.randint(0,255)
    return(vermelho,verde,azul)

#Inicializa o pygame
pygame.init()

# Variaveis para as cores
vermelho = 0
verde = 0
azul = 0

#Configurações da janela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Exemplo com Pygame.")


#Definindo um clock para controlar FPS (Frames por Segundo)
clock = pygame.time.Clock()
FPS = 60


#Definindo a posição x e y como no centro da tela
posicao_x_retangulo = LARGURA // 2
posicao_y_retangulo = ALTURA // 2
#Definindo a velocidade em x e y do retângulo.
velocidade_x_retangulo = 7
velocidade_y_retangulo = 7


rodando = True
while rodando:
    #INICIO LOOP - PROCURANDO POR EVENTOS
    for evento in pygame.event.get():
        #Se o evento fechar o jogo existir
        if evento.type == pygame.QUIT:
            #Muda a variável rodando para False (fecha o loop)
            rodando = False
    #FIM DO LOOP DE EVENTOS
    
    #Lógica de movimento do retângulo.
    posicao_x_retangulo += velocidade_x_retangulo
    posicao_y_retangulo += velocidade_y_retangulo

    # Detecção com as bordas da tela
    if posicao_x_retangulo >= LARGURA or posicao_x_retangulo <= 0:
        velocidade_x_retangulo *= -1
        vermelho,verde,azul = mudar_cores()
    if posicao_y_retangulo >= ALTURA or posicao_y_retangulo <= 0:
        velocidade_y_retangulo *= -1
        vermelho,verde,azul = mudar_cores()

    #Pinta a tela toda de branco
    tela.fill((255,255,255))
                    
    pygame.draw.rect(tela, (vermelho,verde,azul), (posicao_x_retangulo,posicao_y_retangulo,50,50))


    #Atualizando com FPS.
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()