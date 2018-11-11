import pygame
from vector import *

DISPERSION_FACTOR = 0.001

class Node:
    def __init__(self, position, color):
        self.position = position
        self.links = []
        self.velocity = Vector(0.0, 0.0)
        self.momentum = 0.0

        self.velocityDelta = Vector(0.0, 0.0)
        self.momentumDelta = 0.0

        self.color = color

    def connect(self, otherNode):
        hasFound = False
        for link in self.links:
            if link is otherNode:
                hasFound = True
                break
        
        if hasFound is False:
            self.links.append(otherNode)
            otherNode.links.append(self)

    def disperse(self):
        self.velocityDelta = Vector(0.0, 0.0)
        self.momentumDelta = 0.0

        for link in self.links:
            direction = link.position - self.position
            distance = direction.normalize()
            tangentialDirection = Vector(-direction.y, direction.x)

            normalFactor = direction.dot(link.velocity)

            tangentialFactor = tangentialDirection.dot(link.velocity)

            self.velocityDelta += direction * normalFactor * DISPERSION_FACTOR
            self.momentumDelta += tangentialFactor * distance * DISPERSION_FACTOR
            self.velocityDelta -= tangentialDirection * (link.momentum / distance) * DISPERSION_FACTOR

            normalFactor = direction.dot(self.velocity)

            tangentialFactor = tangentialDirection.dot(self.velocity)

            self.velocityDelta -= direction * normalFactor * DISPERSION_FACTOR
            self.momentumDelta += tangentialFactor * distance * DISPERSION_FACTOR
            self.velocityDelta -= tangentialDirection * (self.momentum / distance) * DISPERSION_FACTOR

    def applyDeltas(self):
        self.velocity += self.velocityDelta
        self.momentum += self.momentumDelta

    def updatePosition(self):
        self.position += self.velocity * 0.001

    def drag(self, impulse):
        self.velocity += impulse

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), 2, 0)
