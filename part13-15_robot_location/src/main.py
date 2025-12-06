# WRITE YOUR SOLUTION HERE:
import random

import pygame

pygame.init()
width, height = size = (640, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
dt = 0


def random_robot_pos():
    x = random.randint(0, width - robot.get_width())
    y = random.randint(0, height - robot.get_height())

    return x, y


robot = pygame.image.load("robot.png")
velocity = 150
robot_pos = pygame.Vector2(*random_robot_pos())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            cross_x = (
                mouse_x >= robot_pos.x and mouse_x <= robot_pos.x + robot.get_width()
            )
            cross_y = (
                mouse_y >= robot_pos.y and mouse_y <= robot_pos.x + robot.get_height()
            )

            if cross_x and cross_y:
                robot_pos.update(*random_robot_pos())

    screen.fill("black")
    screen.blit(robot, robot_pos)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
