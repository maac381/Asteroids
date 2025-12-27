import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position = self.position +(self.velocity*dt)


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        vc1 = self.velocity.rotate(angle)
        vc2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        astrd1 = Asteroid(self.position.x, self.position.y, new_radius)
        astrd1.velocity = 1.2 * vc1
        astrd2 = Asteroid(self.position.x, self.position.y, new_radius)
        astrd2.velocity = 1.2 * vc2
        return astrd1, astrd2