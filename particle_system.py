#!/usr/bin/env python
""" generated source for module particle_system """
from math import floor
from particle import Particle


class ParticleSystem(object):
    """ generated source for class ParticleSystem """
    cells = []
    img = PImage()
    cellWidth = int()
    cellHeight = int()

    def __init__(self, app="", img=""):
        """ generated source for method __init__ """
        self.cellWidth = width / int(CELL_SIZE)
        self.cellHeight = height / int(CELL_SIZE)
        self.img = img
        self.cells = [None]*self.cellWidth
        x = 0
        while x < self.cellWidth:
            while y < self.cellHeight:
                self.cells[x][y] = Cell(self, x, y)
                y += 1
            x += 1
        x = 0
        while x < self.cellWidth:
            while y < self.cellHeight:
                self.cells[x][y].neighbors = self.neighbors(x, y)
                y += 1
            x += 1

    def plan(self):
        """ generated source for method plan """
        for row in self.cells:
            for cell in row:
                cell.plan()

    def move(self):
        """ generated source for method move """
        for row in self.cells:
            for cell in row:
                cell.move()

    def draw(self):
        """ generated source for method draw """
        for row in self.cells:
            for cell in row:
                cell.draw()

    def add(self, x, y):
        """ generated source for method add """
        p = Particle(x, y)
        self.place(p)

    def place(self, p):
        """ generated source for method place """
        cell_x = floor(p.origin.x / CELL_SIZE)
        cell_y = floor(p.origin.y / CELL_SIZE)
        if cell_x < 0 or cell_x >= self.cellWidth:
            return
        if cell_y < 0 or cell_y >= self.cellHeight:
            return
        cell = self.cells[cell_x][cell_y]
        cell.add(p)

    def neighbors(self, x, y):
        """ generated source for method neighbors """
        cells = [self.getCell(x - 1, y - 1), self.getCell(x, y - 1), self.getCell(x + 1, y - 1), self.getCell(x - 1, y), self.getCell(x + 1, y), self.getCell(x - 1, y + 1), self.getCell(x, y + 1), self.getCell(x + 1, y + 1)]
        return cells

    def getCell(self, x, y):
        """ generated source for method getCell """
        if x < 0 or x >= self.cellWidth or y < 0 or y >= self.cellWidth:
            return None
        return self.cells[x][y]

    def getColor(self, x, y):
        """ generated source for method getColor """
        _x = floor(map(x, 0, width, 0, self.img.width))
        _y = floor(map(y, 0, height, 0, self.img.height))
        return self.img.pixels[_y * self.img.width + _x]
