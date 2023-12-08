import pygame
import random

pygame.init()

LARGURA_TELA = 600
ALTURA_TELA = 900
BLOCO_TAMANHO = 30
ESCALA = 20

LARGURA_TELA_REAL = LARGURA_TELA // ESCALA
ALTURA_TELA_REAL = ALTURA_TELA // ESCALA

COR_FUNDO = (0, 0, 0)
CORES = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]

FORMAS = [
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
        self.x = LARGURA_TELA_REAL // 2 - len(forma[0]) // 2
        self.y = 0

def desenhar_bloco(tela, bloco, offset):
    for i, linha in enumerate(bloco.forma):
        for j, valor in enumerate(linha):
            if valor:
                pygame.draw.rect(tela, bloco.cor, ((bloco.x + j) * BLOCO_TAMANHO, (bloco.y + i) * BLOCO_TAMANHO, BLOCO_TAMANHO, BLOCO_TAMANHO))

def colisao(bloco, offset):
    for i, linha in enumerate(bloco.forma):
        for j, valor in enumerate(linha):
            if valor:
                if (
                    bloco.y + i + offset[1] >= ALTURA_TELA_REAL or
                    bloco.x + j + offset[0] < 0 or
                    bloco.x + j + offset[0] >= LARGURA_TELA_REAL
                ):
                    return True 
    return False 

def criar_novo_bloco():
    return Bloco(random.choice(FORMAS), random.choice(CORES))

def main():
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('Tetris')
    pygame.display.flip()

    clock = pygame.time.Clock()
    jogo_ativo = True 
    bloco_atual = criar_novo_bloco()
    velocidade_queda = 1

    while jogo_ativo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo_ativo = False

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            bloco_atual.x -= 1
            if bloco_atual.x < 0 or colisao(bloco_atual, (0, 0)):
                bloco_atual.x += 1
        if teclas[pygame.K_RIGHT]:
            bloco_atual.x += 1
            if bloco_atual.x + len(bloco_atual.forma[0]) > LARGURA_TELA_REAL or colisao(bloco_atual, (0, 0)):
                bloco_atual.x -= 1
        if teclas[pygame.K_DOWN]:
            if not colisao(bloco_atual, (0, 1)):
                bloco_atual.y += 1

        tela.fill(COR_FUNDO)  

        if not colisao(bloco_atual, (0, 1)):
            bloco_atual.y += velocidade_queda
        else:
            if bloco_atual.y + len(bloco_atual.forma) >= ALTURA_TELA_REAL:
                bloco_atual = criar_novo_bloco()
            else:
                bloco_atual.y += velocidade_queda

        print("Posição do bloco:", bloco_atual.x, bloco_atual.y)

        desenhar_bloco(tela, bloco_atual, (0, 0))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()

