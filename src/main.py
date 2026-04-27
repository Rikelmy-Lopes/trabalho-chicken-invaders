import pygame

from constants.constants import DT_DIVISOR, FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from entities.Player import Player
from utils.utils import fps_counter

all_sprites = pygame.sprite.Group()
bullets: pygame.sprite.Group = pygame.sprite.Group()

player = Player((SCREEN_WIDTH - 100) / 2, SCREEN_HEIGHT - 100)
all_sprites.add(player)

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial" , 18 , bold = True)

pygame.display.set_caption("Chicken Invaders")

JOGO_PAUSADO_TEXT = font.render("JOGO PAUSADO!" , 1, pygame.Color("RED"))

rodando = True
paused = False
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F5:
                player.speed += 20
            if event.key == pygame.K_p:
                paused = not paused
            if event.key == pygame.K_SPACE:
                player.shoot(bullets)
            

    dt = clock.tick(FPS) / DT_DIVISOR

    window.fill((30, 30, 30))

    if paused:
        retangulo_texto = JOGO_PAUSADO_TEXT.get_rect()
        retangulo_texto.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        window.blit(JOGO_PAUSADO_TEXT,  retangulo_texto)
    else:
        all_sprites.update(dt)
        bullets.update(dt)
        all_sprites.draw(window)
        bullets.draw(window)


    fps_counter(window, clock, font)
    pygame.display.flip()


pygame.quit()   


