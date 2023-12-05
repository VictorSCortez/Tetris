import pygame
import random

pygame.init()

largura_tela = 600
altura_tela = 900
bloco_tamanho = 30
escala = 20

largura_tela_real = largura_tela // escala
altura_tela_real = altura_tela // escala

cor_fundo = (0, 0, 0)
cores = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]

formas = [
    [[1, 1, 1],
     [0, 0, 0]],

    [[1, 1, 1],
     [0, 1, 0]],
    
    [[1, 1, 0],
     [0, 1, 1]],

    [[0, 1, 1],
     [1, 1, 0]],

    [[1, 1, 1, 1]],

    [[1, 1, 1],
     [1, 0, 0]],
     
    [[1, 1, 1],
     [0, 0, 1]]
]

class Bloco:
    def __init__(self, forma, cor):
        self.forma = forma
        self.cor = cor
        self.x = largura_tela_real // 2 - len(forma[0]) // 2
        self.y = 0

def desenhar_bloco(bloco, offset):
    for i, linha in enumerate(bloco.forma):
        for j, valor in enumerate(linha):
            if valor:
                pygame.draw.rect(tela, bloco.cor, ((bloco.x + j) * bloco_tamanho, (bloco.y + i) * bloco_tamanho, bloco_tamanho, bloco_tamanho))

def colisao(bloco, offset):
    for i, linha in enumerate(bloco.forma):
        for j, valor in enumerate(linha):
            if valor:
                if (
                    bloco.y + i + offset[1] >= altura_tela_real or
                    bloco.x + j + offset[0] < 0 or
                    bloco.x + j + offset[0] >= largura_tela_real
                ):
                    return True 
    return False 

def main():
    global tela
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption('Tetris')

    clock = pygame.time.Clock()
    jogo_ativo = True 
    bloco_atual = Bloco(random.choice(formas), random.choice(cores))
    velocidade_queda = 1  # Defina a velocidade de queda desejada

    while jogo_ativo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo_ativo = False

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            bloco_atual.x -= 1
            if colisao(bloco_atual, (0, 0)):
                bloco_atual.x += 1
        if teclas[pygame.K_RIGHT]:
            bloco_atual.x += 1
            if colisao(bloco_atual, (0, 0)):
                bloco_atual.x -= 1
        if teclas[pygame.K_DOWN]:
            if not colisao(bloco_atual, (0, 1)):
                bloco_atual.y += 1

        if not colisao(bloco_atual, (0, 1)):
            bloco_atual.y += velocidade_queda
        else:
            bloco_atual = Bloco(random.choice(formas), random.choice(cores))

        tela.fill(cor_fundo)  # Preencher a tela no início do loop

        desenhar_bloco(bloco_atual, (0, 0))

        pygame.display.flip()
        clock.tick(10)  # Reduzi a taxa de atualização para 10 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
