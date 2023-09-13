import random

import py5

mag = round(random.uniform(2, 4), 1)


class Boid():
    def __init__(self):
        self.position = py5.vector.Py5Vector2D(random.uniform(0, py5.width), random.uniform(0, py5.height))
        self.velocity = py5.vector.Py5Vector2D.random()
        self.velocity.set_mag(mag)
        self.acceleration = py5.vector.Py5Vector2D()
        self.max_force = 0.2
        self.max_speed = 4

    def align(self, boids):
        perception_radius = 60
        steering = py5.vector.Py5Vector2D()
        total = 0
        for other in boids:
            d = py5.dist(
                self.position.x,
                self.position.y,
                other.position.x,
                other.position.y
            )
            if other != self and d < perception_radius:
                steering += other.velocity
                total += 1
        if total > 0:
            steering = steering / total
            steering.set_mag(self.max_speed)
            steering = steering - self.velocity
            steering.set_limit(self.max_force)
        return steering

    def cohesion(self, boids):
        perception_radius = 50
        steering = py5.vector.Py5Vector2D()
        total = 0
        for other in boids:
            d = py5.dist(
                self.position.x,
                self.position.y,
                other.position.x,
                other.position.y
            )
            if other != self and d < perception_radius:
                steering += other.position
                total += 1
        if total > 0:
            steering = steering / total
            steering = steering - self.position
            steering.set_mag(self.max_speed)
            steering = steering - self.velocity
            steering.set_limit(self.max_force)
        return steering

    def separation(self, boids):
        perception_radius = 50
        steering = py5.vector.Py5Vector2D()
        total = 0
        for other in boids:
            d = py5.dist(
                self.position.x,
                self.position.y,
                other.position.x,
                other.position.y
            )
            if other != self and d < perception_radius:
                diff = self.position - other.position
                diff = diff / d
                steering = steering + diff
                total += 1
        if total > 0:
            steering = steering / total
            steering.set_mag(self.max_speed)
            steering = steering - self.velocity
            steering.set_limit(self.max_force)
        return steering

    def flock(self, boids):
        alignment = self.align(boids)
        cohesion = self.cohesion(boids)
        separation = self.separation(boids)
        self.acceleration = self.acceleration + alignment
        self.acceleration = self.acceleration + cohesion
        self.acceleration = self.acceleration + separation

    def show(self):
        py5.stroke(255)
        py5.circle(self.position.x, self.position.y, 8)

    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration
        self.velocity.set_limit(self.max_speed)
        self.acceleration.set_mag(0)

    def edges(self):
        if self.position.x > py5.width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = py5.width
        if self.position.y > py5.height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = py5.height
