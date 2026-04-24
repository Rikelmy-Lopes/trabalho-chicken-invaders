import pygame

largura, altura = 800, 600
positionX, positionY = 350, 250
speed = 2
fps = 60

pygame.init()

tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

pygame.display.set_caption("Chicken Invaders")


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        positionX -= speed
    if keys[pygame.K_RIGHT]:
        positionX += speed
    if keys[pygame.K_UP]:
        positionY -= speed
    if keys[pygame.K_DOWN]:
        positionY += speed



    tela.fill((30, 30, 30))

    pygame.draw.rect(tela, (255, 0, 0), (positionX, positionY, 100, 100))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()   