

import pygame

def fps_counter(window: pygame.Surface, clock: pygame.time.Clock, font: pygame.font.Font):
    fps = "FPS: " + str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    window.blit(fps_t,(0,0))