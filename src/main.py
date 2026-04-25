import pygame

from constants.constants import FPS, PLAYER_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH

player = {
    "positionX": 0.0, 
    "positionY": 0.0,
    "width": 100,
    "height": 100,
    "color": (255, 0, 0)
}

player["positionX"] = (SCREEN_WIDTH - player["width"]) / 2
player["positionY"] = SCREEN_HEIGHT - player["height"]

pygame.init()

tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial" , 18 , bold = True)

pygame.display.set_caption("Chicken Invaders")


def move_player(player, keys, speed: int, dt: float):
    # limita a area jogavel
    if keys[pygame.K_LEFT] and player["positionX"] > 0:
        print(speed * dt)
        player["positionX"] -= speed * dt

    if keys[pygame.K_RIGHT] and (player["positionX"] + player["width"]) < SCREEN_WIDTH:
        player["positionX"] += speed * dt

    if keys[pygame.K_UP] and player["positionY"] > 0:
        player["positionY"] -= speed * dt

    if keys[pygame.K_DOWN] and (player["positionY"] + player["height"] < SCREEN_HEIGHT):
        player["positionY"] += speed * dt

    # reseta a posicao do player caso ele ultrapasse os limites
    if (player["positionX"] < 0):
        player["positionX"] = 0
    elif player["positionX"] + player["width"] > SCREEN_WIDTH:
        player["positionX"] = (SCREEN_WIDTH - player["width"])


def fps_counter(window: pygame.Surface, clock: pygame.time.Clock):
    fps = "FPS: " + str(int(clock.get_fps()))
    fps_t = font. render(fps , 1, pygame.Color("RED"))
    window.blit(fps_t,(0,0))

bullet = {
    "positionX": 0.0, 
    "positionY": 0.0,
    "color": (255, 255, 255),
    "width": 5,
    "height": 10,
}

bullets = []

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F5:
                PLAYER_SPEED += 2
            if event.key == pygame.K_SPACE:
                nova_bala = bullet.copy()

                nova_bala["positionX"] = player["positionX"] + (player["width"] / 2)
                nova_bala["positionY"] = player["positionY"]
                bullets.append(nova_bala)
            

    dt = clock.tick(FPS) / 1000.0
            

    keys = pygame.key.get_pressed()

    move_player(player, keys, PLAYER_SPEED, dt)

    tela.fill((30, 30, 30))

    for b in bullets:
        b["positionY"] -= 5
        pygame.draw.rect(tela, b["color"], (b["positionX"], b["positionY"], b["width"], b["height"]))
        if b["positionY"] < 0:
            bullets.remove(b)

    pygame.draw.rect(tela, player["color"], (player["positionX"], player["positionY"], player["width"], player["height"]))

    fps_counter(tela, clock)
    pygame.display.flip()


pygame.quit()   


