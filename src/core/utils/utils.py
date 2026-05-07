

import os
import sys

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.font import Font

def fps_counter(window: Surface, clock: Clock, font: Font):
    fps = "FPS: " + str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("GREEN"))
    window.blit(fps_t,(0,0))


def resolve_path(path) -> str:
    if getattr(sys, "frozen", False):
        resolved_path = os.path.abspath(os.path.join(sys._MEIPASS, path)) # type: ignore
    else:
        resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))

    return resolved_path