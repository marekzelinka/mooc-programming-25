# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
dt = 0

robot = pygame.image.load("robot.png")
robot1_velocity = 150
robot1_pos = pygame.Vector2(0, 50)
robot2_velocity = 300
robot2_pos = pygame.Vector2(0, 150)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    screen.blit(robot, robot1_pos)
    screen.blit(robot, robot2_pos)

    pygame.display.flip()

    robot1_pos.x += robot1_velocity * dt

    if robot1_velocity > 0 and robot1_pos.x + robot.get_width() >= 640:
        robot1_velocity = -robot1_velocity

    if robot1_velocity < 0 and robot1_pos.x <= 0:
        robot1_velocity = -robot1_velocity

    robot2_pos.x += robot2_velocity * dt

    if robot2_velocity > 0 and robot2_pos.x + robot.get_width() >= 640:
        robot2_velocity = -robot2_velocity

    if robot2_velocity < 0 and robot2_pos.x <= 0:
        robot2_velocity = -robot2_velocity

    dt = clock.tick(60) / 1000

pygame.quit()
