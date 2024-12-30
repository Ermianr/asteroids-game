import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shoot import *

def main():
  pygame.init()

  # Reloj de juego
  clock = pygame.time.Clock()

  # Crear jugador
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT /2

  # Crear la pantalla
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  # Grupo
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable, asteroids)
  AsteroidField.containers = (updatable)
  Shoot.containers = (shots, updatable, drawable)

  player = Player(x, y, PLAYER_RADIUS)
  asteroid_field = AsteroidField()

  dt = 0

  while True:
     # Listener de eventos
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return quit
      
    for obj in updatable:
       obj.update(dt)

    for asteroid in asteroids:
       if asteroid.collides_with(player):
          print("Game over")
          sys.exit()

       for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

    # Rellenar de negro la pantalla
    screen.fill((0,0,0))

    for obj in drawable:
       obj.draw(screen)
  
    # Actualizar la pantalla
    pygame.display.flip()

    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()