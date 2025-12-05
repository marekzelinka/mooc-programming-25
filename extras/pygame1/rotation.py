import math

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
dt = 0

robot = pygame.image.load("robot.png")
velocity = 300
angle = 0
robot_pos = pygame.Vector2(0, 0)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("green")

    robot_pos.x = 320 + math.cos(angle) * 100 - robot.get_width() / 2
    robot_pos.y = 240 + math.sin(angle) * 100 - robot.get_height() / 2

    screen.blit(robot, robot_pos)

    pygame.display.flip()

    angle += 0.01
    dt = clock.tick(60) / 1000

pygame.quit()
