import pygame
from constants import *
from player import *

def main():
  pygame.init()

  # Reloj de juego
  clock = pygame.time.Clock()
  dt = 0

  # Crear jugador
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT /2
  player = Player(x, y, PLAYER_RADIUS)

  # Crear la pantalla
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  while True:
     # Listener de eventos
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return quit
      
    player.update(dt)

    # Rellenar de negro la pantalla
    screen.fill((0,0,0))
    # Dibujar jugador
    player.draw(screen)
    # Actualizar la pantalla
    pygame.display.flip()

    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()