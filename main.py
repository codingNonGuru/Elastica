from node import *
from vector import *
import pygame

nodes = []

center = Vector(640.0, 360.0)

nodes.append(Node(center + Vector(-40.0, 20.0), (255, 255, 255)))
nodes.append(Node(center + Vector(0.0, 30.0), (255, 0, 0)))
nodes.append(Node(center + Vector(40.0, 20.0), (0, 255, 255)))
nodes.append(Node(center + Vector(40.0, -20.0), (255, 128, 0)))
nodes.append(Node(center + Vector(0.0, -30.0), (255, 0, 0)))
nodes.append(Node(center + Vector(-40.0, -20.0), (255, 255, 255)))

nodes.append(Node(center + Vector(0.0, 0.0), (0, 0, 255)))

nodes[0].connect(nodes[1])
nodes[1].connect(nodes[2])
nodes[2].connect(nodes[3])
nodes[3].connect(nodes[4])
nodes[4].connect(nodes[5])
nodes[5].connect(nodes[0])

nodes[6].connect(nodes[0])
nodes[6].connect(nodes[1])
nodes[6].connect(nodes[2])
nodes[6].connect(nodes[3])
nodes[6].connect(nodes[4])
nodes[6].connect(nodes[5])

nodes[0].drag(Vector(0.0, 50.0))
#nodes[1].drag(Vector(0.0, 4.0))

screenSize = Vector(1280, 720)

pygame.init()

screen = pygame.display.set_mode((screenSize.x, screenSize.y), pygame.DOUBLEBUF)

while True:
    for x in range(0, 4):
        for node in nodes:
            node.disperse()

        for node in nodes:
            node.applyDeltas()

    for node in nodes:
        node.updatePosition()

    for node in nodes:
        node.draw(screen)

    screen.fill((0, 0, 0))

    for node in nodes:
        node.draw(screen)

    pygame.display.flip()