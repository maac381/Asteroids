import pygame
from constants import *
from circleshape import CircleShape

class HomingRocket(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, ROCKET_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        self.target = None
        self.tracking_speed = 5.0 # How fast it turns (0.0 to 10.0+)

    def find_nearest_asteroid(self, asteroids_group):
        nearest = None
        min_dist = float('inf')
        
        for asteroid in asteroids_group:
            dist = self.position.distance_to(asteroid.position)
            if dist < min_dist:
                min_dist = dist
                nearest = asteroid
        return nearest

    def update(self, dt, asteroids_group):
        # 1. Acquire or refresh target
        if self.target is None or not self.target.alive():
            self.target = self.find_nearest_asteroid(asteroids_group)

        if self.target:
            # 2. Calculate the direction to the target
            desired_direction = (self.target.position - self.position).normalize()
            
            # 3. Steering: Smoothly rotate the current velocity toward the target
            # Adjust velocity by lerping (linear interpolation)
            target_velocity = desired_direction * ROCKET_SPEED
            self.velocity = self.velocity.lerp(target_velocity, self.tracking_speed * dt)
        
        # 4. Move the rocket
        self.position += self.velocity * dt

    def draw(self, screen):
        # This draws a white circle. You can change the color to "red" 
        # to distinguish it from regular shots.
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)