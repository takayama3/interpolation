import pygame
import sys
from cubic_interpolation import cubic_interpolation


pygame.init()


def f(dots):
    global dots0

    xs = []
    ys = []
    for i in dots:
        xs += [i[0]]
        ys += [i[1]]

    for x in range(xs[1], xs[2] + 1):
        y = cubic_interpolation(xs, ys, x)
        dots0 += [(x, y)]


def ff():
    global dots
    global dots0
    dots0 = []

    for i in range(len(dots) - 3):
        f(dots[i: i + 4])


fps = 60
window_size = (1000, 700)
background_color = (255, 255, 255)
radius = 5

window = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

dots = []
dots0 = []
clicked = None
show = True

while True:

    window.fill(background_color)

    if len(dots) >= 4:
        if show:
            pygame.draw.aalines(window, (0, 255, 0), False, dots)
        pygame.draw.aalines(window, (0, 0, 255), False, dots0)

    if show:
        for coords in dots:
            pygame.draw.circle(window, (255, 0, 0), coords, radius)

    if not clicked is None:
        dots[i] = pygame.mouse.get_pos()
        if len(dots) >= 4:
            ff()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(len(dots)):
                if (event.pos[0] - dots[i][0]) ** 2 + (event.pos[1] - dots[i][1]) ** 2 <= radius ** 2:
                    clicked = i
                    break
            else:
                dots.append(event.pos)
                if len(dots) >= 4:
                    ff()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            for i in range(len(dots)):
                if (event.pos[0] - dots[i][0]) ** 2 + (event.pos[1] - dots[i][1]) ** 2 <= radius ** 2:
                    dots.pop(i)
                    if len(dots) >= 4:
                        ff()
                    break

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            clicked = None

        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            show = 1 - show

    pygame.display.update()
    clock.tick(fps)
