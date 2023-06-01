import pygame
import sys
from bilinear_interpolation import bilinear_interpolation


pygame.init()

fps = 60
window_size = (500, 500)
px = 5

window = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

arr = [[(255, 255, 255) for i in range(window_size[0])] for j in range(window_size[1])]

x1 = 0
y1 = 0
x2 = window_size[0] - 1
y2 = window_size[1] - 1

f = [
    [(255, 0, 0), (0, 255, 0)],
    [(0, 0, 255), (255, 120, 0)]
]

for y in range(window_size[1]):
    for x in range(window_size[0]):
        if arr[y][x] == (255, 255, 255):
            color = [0, 0, 0]
            for i in range(3):
                f0 = [
                    [0, 0],
                    [0, 0]
                ]
                for a in 0, 1:
                    for b in 0, 1:
                        f0[a][b] = f[a][b][i]

                color[i] = bilinear_interpolation((x1, x2), (y1, y2), f0, x, y)
                color[i] = int(max(min(color[i], 255), 0))

            arr[y][x] = tuple(color)


while True:

    for y in range(window_size[1]):
        for x in range(window_size[0]):
            pygame.draw.rect(window, arr[y][x], (x, y, 1, 1))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    clock.tick(fps)
    pygame.display.update()
