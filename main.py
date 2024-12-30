import pygame
from constants import *

def main():
  pygame.init()

  # Crear la pantalla
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  while True:
     # Listener de eventos
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
           return quit
     # Rellenar de negro la pantalla
     screen.fill((0,0,0))

     # Actualizar la pantalla
     pygame.display.flip()

if __name__ == "__main__":
    main()