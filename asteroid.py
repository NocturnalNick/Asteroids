import pygame
from constants import *
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        new_vector_first = self.velocity.rotate(angle)
        new_vector_second = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        new_asteroid.velocity = new_vector_first * 1.2
        new_unsteroid = Asteroid(self.position.x,self.position.y,new_radius)
        new_unsteroid.velocity = new_vector_second * 1.2
