

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.font import Font

def fps_counter(window: Surface, clock: Clock, font: Font):
    fps = "FPS: " + str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    window.blit(fps_t,(0,0))