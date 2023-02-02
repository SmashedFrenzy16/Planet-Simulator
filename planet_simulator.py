import pygame
import sys
from pygame.math import Vector2
from random import randrange
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

pygame.init()

black = (0, 0, 0)

white = [255, 255, 255]

fps = 60

fps_clock = pygame.time.Clock()

windowsize = Vector2(1000, 1000)

screen = pygame.display.set_mode((int(windowsize.x), int(windowsize.y)))

planets = []


class Planet():

    def __init__(self, pos, delta=Vector2(0, 0), radius=10, imovable=False):

        self.pos = pos

        self.radius = radius

        self.delta = delta

        self.imovable = imovable

        self.is_eatable = False

        planets.append(self)

    def generator(self):

        if not self.imovable:

            for i in planets:

                if not i is self:

                    try:

                        if self.is_eatable:

                            if self.pos.distance_to(i.pos) < self.radius + i.radius:

                                print("Destroyed")

                                i.radius += self.radius

                                planets.remove(self)

                        direction_from_obj = (
                            i.pos - self.pos).normalize() * 0.01 * (i.radius / 10)

                        self.delta += direction_from_obj

                    except:

                        print("In the same spot")

            self.pos += self.delta

        pygame.draw.circle(screen, white, self.pos, self.radius)


Planet(Vector2(400, 400), radius=50, imovable=True)

Planet(Vector2(400, 200), delta=Vector2(4, 0), radius=10)

Planet(Vector2(440, 200), delta=Vector2(4, 0), radius=5)

running = True

while running:

    screen.fill(black)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    for i in planets:

        i.generator()

    pygame.display.flip()

    fps_clock.tick(fps)
