# WRITE YOUR SOLUTION HERE:
import math
from datetime import datetime

import pygame

pygame.init()
width, height = size = (640, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
dt = 0


def draw_line(
    start_pos: tuple[float, float],
    length: int,
    thickness: int,
    proportion: float,
):
    middle_x, middle_y = start_pos

    angle = 2 * math.pi * proportion - math.pi / 2
    end_x = middle_x + math.cos(angle) * length
    end_y = middle_y + math.sin(angle) * length

    pygame.draw.line(screen, "black", (middle_x, middle_y), (end_x, end_y), thickness)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.now()
    hours = now.hour % 12
    minutes = now.minute
    seconds = now.second

    title = datetime.strftime(now, "%H:%M:%S")
    pygame.display.set_caption(title)

    screen.fill("white")

    middle_x = width / 2
    middle_y = height / 2

    # clock
    pygame.draw.circle(screen, "lightgray", (middle_x, middle_y), 200)
    # inner space
    pygame.draw.circle(screen, "white", (middle_x, middle_y), 195)
    # middle dot
    pygame.draw.circle(screen, "black", (middle_x, middle_y), 10)

    # hour hand
    draw_line(
        (middle_x, middle_y), 150, 5, (hours + minutes / 60 + seconds / 3600) / 12
    )
    # minute hand
    draw_line((middle_x, middle_y), 180, 2, (minutes + seconds / 60) / 60)
    # seconds hand
    draw_line((middle_x, middle_y), 185, 1, seconds / 60)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
