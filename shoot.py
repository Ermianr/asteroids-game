from circleshape import *
from constants import SHOOT_RADIUS

class Shoot(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, SHOOT_RADIUS )
  
  def draw(self, screen):
    pygame.draw.circle(screen, (255,255,255), (self.position), self.radius, 2)
  
  def update(self, dt):
    self.position += self.velocity * dt