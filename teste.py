# Example file showing a basic pygame "game loop"
import pygame
from caminho import Pilha, Caminho

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 'm', 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 'e', 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

start_x = 0
start_y = 0

actual_x = start_x
actual_y = start_y

screen.fill("white")
start_caminho = None
for i in range(0, len(labirinto)):
    for j in range(len(labirinto)):
        color = ""
        if labirinto[i][j] == 1:
            color = "pink"
        elif labirinto[i][j] == 'm':
            color = "blue"
            start_caminho = Caminho(x=i, y=j)
        elif labirinto[i][j] == 'e':
            color = "yellow"
        else:
            color = "black"
        pygame.draw.rect(screen, color, pygame.Rect(actual_x + 5, actual_y + 5, 30, 30))
        labirinto[i][j] = {
            "value": str(labirinto[i][j]),
            "color": color,
            "x": actual_x,
            "y": actual_y
        }
        actual_x += 32
    actual_x = start_x
    actual_y += 32

pilha = Pilha(start_caminho)

pygame.display.flip()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    posicao_atual = pilha.top

    if labirinto[posicao_atual.x - 1][posicao_atual.y]['color']=='black':
    elif labirinto[posicao_atual.x + 1][posicao_atual.y]['color']=='black':
    elif labirinto[posicao_atual.x][posicao_atual.y - 1]['color']=='black':
    elif labirinto[posicao_atual.x][posicao_atual.y + 1]['color']=='black':


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()