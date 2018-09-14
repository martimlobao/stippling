#!/usr/bin/env python
""" generated source for module particle_cell """
from particle import PVector
from particle_system import ParticleSystem


class Cell(object):
    """ generated source for class Cell """
    sys = ParticleSystem()
    particles = ArrayList()
    neighbors = []
    origin = PVector()

    def __init__(self, sys, x, y):
        """ generated source for method __init__ """
        self.sys = sys
        self.particles = ArrayList()
        self.origin = PVector(CELL_SIZE * x, CELL_SIZE * y)

    def plan(self):
        """ generated source for method plan """
        for p in self.particles:
            for cell in self.neighbors:
                if cell == None:
                    continue
                force.add(cell.repel(p))
            force.limit(1.0)
            p.plan(force)

    def move(self):
        """ generated source for method move """
        i = len(self.particles) - 1
        while i >= 0:
            p.move()
            if not self.contains(p.origin.x, p.origin.y):
                self.remove(p)
                self.sys.place(p)
            i -= 1

    def draw(self):
        """ generated source for method draw """
        for p in self.particles:
            p.draw()
        debugDraw()

    def debugDraw(self):
        """ generated source for method debugDraw """
        if not DEBUG:
            return
        noFill()
        stroke(255, 0, 0)
        strokeWeight(1)
        rect(self.origin.x, self.origin.y, CELL_SIZE, CELL_SIZE)

    def add(self, p):
        """ generated source for method add """
        self.particles.add(p)

    def remove(self, p):
        """ generated source for method remove """
        self.particles.remove(p)

    def repel(self, p):
        """ generated source for method repel """
        sum = PVector(0, 0)
        dist = float()
        unit = PVector()
        for other in self.particles:
            if other == p:
                continue
            dist = PVector.dist(p.origin, other.origin)
            if dist > CELL_SIZE:
                continue
            unit = PVector.sub(p.origin, other.origin)
            unit.normalize()
            dist = norm(dist, 0, CELL_SIZE)
            unit.mult((p.mass * other.mass) / (dist * dist))
            sum.add(unit)
        return sum

    def contains(self, x, y):
        """ generated source for method contains """
        dx = x - self.origin.x
        if dx < 0 or dx > CELL_SIZE:
            return False
        dy = y - self.origin.y
        if dy < 0 or dy > CELL_SIZE:
            return False
        return True
