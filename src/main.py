import pygame

largura = 800
altura = 600
speed = 5
fps = 60

player = {
    "positionX": 0.0, 
    "positionY": 0.0,
    "width": 100,
    "height": 100,
    "color": (255, 0, 0)
}

player["positionX"] = (largura - player["width"]) / 2
player["positionY"] = altura - player["height"]

pygame.init()

tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

pygame.display.set_caption("Chicken Invaders")


def move_player(player, keys, speed):
    # limita a area jogavel
    if keys[pygame.K_LEFT] and player["positionX"] > 0:
        player["positionX"] -= speed

    if keys[pygame.K_RIGHT] and (player["positionX"] + player["width"]) < largura:
        player["positionX"] += speed

    if keys[pygame.K_UP] and player["positionY"] > 0:
        player["positionY"] -= speed

    if keys[pygame.K_DOWN] and (player["positionY"] + player["height"] < altura):
        player["positionY"] += speed

    # reseta a posicao do player caso ele ultrapasse os limites
    if (player["positionX"] < 0):
        player["positionX"] = 0
    elif player["positionX"] + player["width"] > largura:
        player["positionX"] = (largura - player["width"])


rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F5:
                print("Aumentando velocidade")
                speed += 2
            

    keys = pygame.key.get_pressed()

    move_player(player, keys, speed)

    tela.fill((30, 30, 30))

    pygame.draw.rect(tela, player["color"], (player["positionX"], player["positionY"], player["width"], player["height"]))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()   


