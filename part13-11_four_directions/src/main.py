# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen_width, screen_height = pygame.display.get_window_size()
clock = pygame.time.Clock()
running = True
dt = 0


robot = pygame.image.load("robot.png")
velocity = 150
robot_pos = pygame.Vector2(
    screen_width / 2 - robot.get_width(),
    screen_height / 2 - robot.get_height(),
)
robot_moving_dir = [False, False, False, False]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                robot_moving_dir[0] = True

            if event.key == pygame.K_RIGHT:
                robot_moving_dir[1] = True

            if event.key == pygame.K_DOWN:
                robot_moving_dir[2] = True

            if event.key == pygame.K_LEFT:
                robot_moving_dir[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                robot_moving_dir[0] = False

            if event.key == pygame.K_RIGHT:
                robot_moving_dir[1] = False

            if event.key == pygame.K_DOWN:
                robot_moving_dir[2] = False

            if event.key == pygame.K_LEFT:
                robot_moving_dir[3] = False

    if robot_moving_dir[0]:
        robot_pos.y -= velocity * dt
    if robot_moving_dir[1]:
        robot_pos.x += velocity * dt
    if robot_moving_dir[2]:
        robot_pos.y += velocity * dt
    if robot_moving_dir[3]:
        robot_pos.x -= velocity * dt

    screen.fill("black")

    screen.blit(robot, robot_pos)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
