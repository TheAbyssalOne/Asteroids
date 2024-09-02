from circleshape import *
import pygame
import random
from constants import *  # Assumes there's a base_velocity defined

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)
        for x in Asteroid.containers:
                x.add(self)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20, 50)
            new_velocity1 = self.velocity.copy().rotate(random_angle)
            new_velocity2 = self.velocity.copy().rotate(-random_angle)
            new_velocity1 *= 1.2 
            new_velocity2 *= 1.2 
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = new_velocity1
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = new_velocity2