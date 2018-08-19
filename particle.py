#!/usr/bin/env python
class PVector(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

""" generated source for module particle """
class Particle(object):
    """ generated source for class Particle """
    origin = PVector()
    forces = PVector()
    velocity = PVector()
    mass = float()

    def __init__(self, x, y):
        """ generated source for method __init__ """
        self.origin = PVector(x, y)
        self.mass = 1.0
        self.velocity = PVector(0, 0)

    def plan(self, force):
        """ generated source for method plan """
        self.velocity.mult(0.9)
        force.div(self.mass)
        self.velocity.add(force)

    def move(self):
        """ generated source for method move """
        self.origin.add(self.velocity)
        if self.outOfBounds():
            return
        x = floor(map(self.origin.x, 0, width, 0, img.width))
        y = floor(map(self.origin.y, 0, height, 0, img.height))
        c = img.pixels[y * img.width + x]
        targetMass = CELL_SIZE * norm(brightness(c), 256, 0)
        if targetMass > self.mass:
            self.mass = min(self.mass * 1.1, targetMass)
        else:
            self.mass = max(self.mass * 0.9, targetMass)

    def outOfBounds(self):
        """ generated source for method outOfBounds """
        if self.origin.x < 0 or self.origin.x >= width:
            return True
        if self.origin.y < 0 or self.origin.y >= height:
            return True
        return False

    def draw(self):
        """ generated source for method draw """
        noStroke()
        fill(64)
        n = norm(self.mass, 0, CELL_SIZE)
        r = CELL_SIZE * n * n
        ellipse(self.origin.x, self.origin.y, r, r)
