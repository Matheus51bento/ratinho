# Example file showing a basic pygame "game loop"
import pygame
from caminho import Pilha, Caminho
from time import sleep

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
walking = True
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


def walk(x: int, y: int):
    novo_caminho = Caminho(x, y)
    infos = labirinto[x][y]
    pygame.draw.rect(screen, "blue", pygame.Rect(infos['x'] + 5, infos['y'] + 5, 30, 30))

    infos = labirinto[posicao_atual.x][posicao_atual.y]
    pygame.draw.rect(screen, "green", pygame.Rect(infos['x'] + 5, infos['y'] + 5, 30, 30))
    pilha.empilhar(novo_caminho)
    labirinto[x][y]['color'] = 'blue'


def end_game(x: int, y: int):
    if labirinto[x][y]['color'] == 'yellow':
        return False
    walk(x, y)
    return True


while walking:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    posicao_atual = pilha.top

    if labirinto[posicao_atual.x - 1][posicao_atual.y]['color'] in ['black', 'yellow']:
        walking = end_game(posicao_atual.x - 1, posicao_atual.y)
        labirinto[posicao_atual.x][posicao_atual.y]['color'] = 'green'

    elif labirinto[posicao_atual.x + 1][posicao_atual.y]['color'] in ['black', 'yellow']:
        walking = end_game(posicao_atual.x + 1, posicao_atual.y)
        labirinto[posicao_atual.x][posicao_atual.y]['color'] = 'green'

    elif labirinto[posicao_atual.x][posicao_atual.y - 1]['color'] in ['black', 'yellow']:
        walking = end_game(posicao_atual.x, posicao_atual.y - 1)
        labirinto[posicao_atual.x][posicao_atual.y]['color'] = 'green'

    elif labirinto[posicao_atual.x][posicao_atual.y + 1]['color'] in ['black', 'yellow']:
        walking = end_game(posicao_atual.x, posicao_atual.y + 1)
        labirinto[posicao_atual.x][posicao_atual.y]['color'] = 'green'

    else:
        labirinto[posicao_atual.x][posicao_atual.y]['color'] = 'white'
        infos = labirinto[posicao_atual.x][posicao_atual.y]
        pygame.draw.rect(screen, "white", pygame.Rect(infos['x'] + 5, infos['y'] + 5, 30, 30))

        last_step = pilha.top.previous
        infos = labirinto[last_step.x][last_step.y]
        labirinto[last_step.x][last_step.y]['color'] = 'blue'
        pygame.draw.rect(screen, "blue", pygame.Rect(infos['x'] + 5, infos['y'] + 5, 30, 30))
        pilha.desempilhar()

    pygame.display.flip()

    sleep(0.5)

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

sleep(5)

pygame.quit()
