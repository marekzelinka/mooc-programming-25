from random import randint

import pygame

pygame.init()
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0


robot = pygame.image.load("robot.png")
robots = []
robot_count = 20
for i in range(robot_count):
    # causes the new random start position to be drawn immediately
    robots.append([-1000, screen_height])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for i in range(robot_count):
        if robots[i][1] + robot.get_height() < screen_height:
            # the robot falls downwards
            robots[i][1] += 1
        else:
            if robots[i][0] < -robot.get_width() or robots[i][0] > screen_width:
                # new random start point
                robots[i][0] = randint(0, screen_width - robot.get_width())
                robots[i][1] = -randint(100, 1000)
            elif robots[i][0] + robot.get_width() / 2 < screen_width / 2:
                # the robot moves to the left
                robots[i][0] -= 1
            else:
                # the robot moves to the right
                robots[i][0] += 1

    for i in range(robot_count):
        screen.blit(robot, (robots[i][0], robots[i][1]))

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
