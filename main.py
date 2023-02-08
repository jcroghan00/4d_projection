# from The Coding Train, translated and modified by myself and not using any 3d drawing functions

import math
import os

import pygame

from Vector4 import Vector4
from matrix import multiply_matrix_vector, multiply_matrix_vector4

os.environ["SDL_VIDEO_CENTERED"] = '1'
width, height = 2560, 1440
black, white, blue = (20, 20, 20), (230, 230, 230), (0, 154, 255)

pygame.init()
pygame.display.set_caption("4D Projection")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60

angle = 0
cube_position = [width / 2, height / 2]
scale = 2000
speed = 0.01

points = [Vector4([-1], [-1], [-1], [1]),
          Vector4([1], [-1], [-1], [1]),
          Vector4([1], [1], [-1], [1]),
          Vector4([-1], [1], [-1], [1]),
          Vector4([-1], [-1], [1], [1]),
          Vector4([1], [-1], [1], [1]),
          Vector4([1], [1], [1], [1]),
          Vector4([-1], [1], [1], [1]),
          Vector4([-1], [-1], [-1], [-1]),
          Vector4([1], [-1], [-1], [-1]),
          Vector4([1], [1], [-1], [-1]),
          Vector4([-1], [1], [-1], [-1]),
          Vector4([-1], [-1], [1], [-1]),
          Vector4([1], [-1], [1], [-1]),
          Vector4([1], [1], [1], [-1]),
          Vector4([-1], [1], [1], [-1])]

projected_2d = []


def draw_points(projected_3d):
    global projected_2d

    distance = 3

    z = 1 / (distance - projected_3d.z[0])
    projection_matrix = [[z, 0, 0], [0, z, 0]]
    projected = multiply_matrix_vector(projection_matrix, projected_3d)

    x = (projected[0][0][0] * scale) + cube_position[0]
    y = (projected[1][0][0] * scale) + cube_position[1]

    projected_2d.append([x, y])

    pygame.draw.circle(screen, blue, (x, y), 10)


def connect_lines(offset, i, j):
    global projected_2d

    a = projected_2d[i + offset]
    b = projected_2d[j + offset]

    pygame.draw.line(screen, white, a, b)


def draw():
    global angle, projected_2d

    clock.tick(fps)
    screen.fill(black)

    projected_3d = []
    projected_2d = []

    for point in points:
        v = point

        rotation_xy = [
            [math.cos(angle), -math.sin(angle), 0, 0],
            [math.sin(angle), math.cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]

        rotation_xz = [
            [math.cos(angle), 0, -math.sin(angle), 0],
            [0, 1, 0, 0],
            [math.sin(angle), 0, math.cos(angle), 0],
            [0, 0, 0, 1]
        ]

        rotation_zw = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, math.cos(angle), -math.sin(angle)],
            [0, 0, math.sin(angle), math.cos(angle)]
        ]

        rotated = multiply_matrix_vector4(rotation_xz, v)
        rotated = multiply_matrix_vector4(rotation_zw, rotated)

        distance = 3
        w = 1 / (distance - rotated.w[0])

        projection = [
            [w, 0, 0, 0],
            [0, w, 0, 0],
            [0, 0, w, 0]
        ]

        projected = multiply_matrix_vector4(projection, rotated)
        projected_3d.append(projected)

        draw_points(projected)

    for i in range(4):
        connect_lines(0, i, (i + 1) % 4)
        connect_lines(0, i + 4, ((i + 1) % 4) + 4)
        connect_lines(0, i, i + 4)

        connect_lines(8, i, (i + 1) % 4)
        connect_lines(8, i + 4, ((i + 1) % 4) + 4)
        connect_lines(8, i, i + 4)

    for i in range(8):
        connect_lines(0, i, i + 8)

    angle += speed
    pygame.display.update()


if __name__ == "__main__":
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    run = False
        draw()

pygame.quit()
