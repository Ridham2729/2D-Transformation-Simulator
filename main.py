
import pygame
import numpy as np
from transformations import (
    translate, scale, rotate, reflect_x, shear
)

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Transformation Simulator")

font = pygame.font.SysFont("Arial", 22)
small_font = pygame.font.SysFont("Arial", 17)

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
BLUE = (40, 130, 255)
RED = (240, 70, 70)
GRAY = (190, 190, 190)

original = np.array([
    [-60, -50],
    [60, -50],
    [0, 70]
], dtype=float)

points = original.copy()

tx, ty = 0, 0
angle = 0
sx, sy = 1, 1
shx, shy = 0, 0

def draw_grid():
    for x in range(0, WIDTH, 50):
        pygame.draw.line(screen, (235, 235, 235),
                         (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 50):
        pygame.draw.line(screen, (235, 235, 235),
                         (0, y), (WIDTH, y))

    pygame.draw.line(screen, BLACK, (0, HEIGHT//2),
                     (WIDTH, HEIGHT//2), 2)
    pygame.draw.line(screen, BLACK, (WIDTH//2, 0),
                     (WIDTH//2, HEIGHT), 2)

def to_screen(p):
    return (
        int(WIDTH//2 + p[0]),
        int(HEIGHT//2 - p[1])
    )

def draw_text(text, x, y):
    screen.blit(font.render(text, True, BLACK), (x, y))

def draw_object():
    transformed = original.copy()

    transformed = scale(transformed, sx, sy)
    transformed = shear(transformed, shx, shy)
    transformed = rotate(transformed, angle)
    transformed = translate(transformed, tx, ty)

    pygame.draw.polygon(
        screen, BLUE,
        [to_screen(p) for p in transformed], 3
    )

    pygame.draw.polygon(
        screen, RED,
        [to_screen(p) for p in original], 2
    )

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                tx -= 10
            elif event.key == pygame.K_RIGHT:
                tx += 10
            elif event.key == pygame.K_UP:
                ty += 10
            elif event.key == pygame.K_DOWN:
                ty -= 10

            elif event.key == pygame.K_r:
                angle += 15
            elif event.key == pygame.K_t:
                angle -= 15

            elif event.key == pygame.K_EQUALS:
                sx *= 1.1
                sy *= 1.1
            elif event.key == pygame.K_MINUS:
                sx *= 0.9
                sy *= 0.9

            elif event.key == pygame.K_f:
                shy = -shy if shy else 0
                points = reflect_x(original)

            elif event.key == pygame.K_h:
                shx += 0.1

            elif event.key == pygame.K_0:
                tx, ty = 0, 0
                angle = 0
                sx, sy = 1, 1
                shx, shy = 0, 0
                points = original.copy()

    draw_object()

    draw_text("2D TRANSFORMATION SIMULATOR", 20, 15)
    draw_text("Arrow Keys: Translation", 20, 60)
    draw_text("R / T: Rotate", 20, 90)
    draw_text("+ / -: Scaling", 20, 120)
    draw_text("H: Shearing", 20, 150)
    draw_text("F: Reflection (X-axis)", 20, 180)
    draw_text("0: Reset", 20, 210)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
