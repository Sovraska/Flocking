from random import randint, uniform

import pygame
import math
import pygame.math as pmath
from setup import WIDTH, HEIGHT, WHITE, screen, flocks


def random_direction():
    a = math.radians(randint(0, 360))
    return pygame.Vector2(math.cos(a), math.sin(a))


def random_place():
    x = randint(5, WIDTH - 5)
    y = randint(5, HEIGHT - 5)
    return x, y


class Boid():
    def __init__(self):
        self.position = pmath.Vector2(random_place())
        self.velocity = random_direction()
        self.velocity = self.set_mag(self.velocity, uniform(0, 1) + 1)
        self.acceleration = pmath.Vector2()
        self.max_force = 0.5
        self.max_speed = 4

    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration
        if self.velocity.magnitude() > self.max_speed:
            self.velocity = self.set_mag(self.velocity, self.max_speed)
        self.acceleration *= 0

    def edges(self):
        if self.position.x > WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = WIDTH
        if self.position.y > HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = HEIGHT
        return 123

    def show(self):
        r = int(abs(self.velocity.x * 50))
        g = int(abs((self.position.x / 12)))
        b = int(abs(self.velocity.y * 50))
        print((r, g, b))
        pygame.draw.circle(screen, (r, g, b), self.position.xy, 10)

    def flock(self, boids, align_value, cohesion_value, separation_value):
        alignment = self.align(boids)
        cohesion = self.cohesion(boids)
        separation = self.separation(boids)
        if align_value:
            alignment = alignment * (align_value / 2000)
        if cohesion_value:
            cohesion = cohesion * (cohesion_value / 2000)
        if separation_value:
            separation = separation * (separation_value / 2000)
        self.acceleration = self.acceleration + alignment
        self.acceleration = self.acceleration + cohesion
        self.acceleration = self.acceleration + separation

    def align(self, boids):
        perception_radius = 60
        steering = pmath.Vector2()
        total = 0
        for other in boids:
            d = self.position.distance_to(
                other.position
            )
            if other != self and d < perception_radius:
                steering += other.velocity
                total += 1
        if total > 0:
            steering = steering / total

            steering = self.set_mag(steering, self.max_speed)

            steering = steering - self.velocity

            steering = self.set_limit(steering, self.max_force)

        return steering

    def cohesion(self, boids):
        perception_radius = 100
        steering = pmath.Vector2()
        total = 0
        for other in boids:
            d = self.position.distance_to(
                other.position
            )
            if other != self and d < perception_radius:
                steering += other.position
                total += 1
        if total > 0:
            steering = steering / total
            steering = steering - self.position
            steering = self.set_mag(steering, self.max_speed)
            steering = steering - self.velocity
            steering = self.set_limit(steering, self.max_force)
        return steering

    def separation(self, boids):
        perception_radius = 50
        steering = pmath.Vector2()
        total = 0
        for other in boids:
            d = self.position.distance_to(
                other.position
            )
            if other != self and d < perception_radius:
                diff = self.position - other.position
                diff = diff / d
                steering = steering + diff
                total += 1
        if total > 0:
            steering = steering / total
            steering = self.set_mag(steering, self.max_speed)
            steering = steering - self.velocity
            steering = self.set_limit(steering, self.max_force)
        return steering

    def set_mag(self, obj, new_Mag):

        new_x = obj.x * new_Mag / obj.magnitude()
        new_y = obj.y * new_Mag / obj.magnitude()
        obj.x = new_x
        obj.y = new_y
        return obj

    def set_limit(self, obj, limit):
        if obj.magnitude() > limit:
            obj = self.set_mag(obj, limit)
        return obj
