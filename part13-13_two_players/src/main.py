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
robot1_pos = pygame.Vector2(50, 50)
robot2_pos = pygame.Vector2(500, 300)
robot1_moving_dir = [False, False, False, False]
robot2_moving_dir = [False, False, False, False]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                robot1_moving_dir[0] = True

            if event.key == pygame.K_RIGHT:
                robot1_moving_dir[1] = True

            if event.key == pygame.K_DOWN:
                robot1_moving_dir[2] = True

            if event.key == pygame.K_LEFT:
                robot1_moving_dir[3] = True

            if event.key == pygame.K_w:
                robot2_moving_dir[0] = True

            if event.key == pygame.K_d:
                robot2_moving_dir[1] = True

            if event.key == pygame.K_s:
                robot2_moving_dir[2] = True

            if event.key == pygame.K_a:
                robot2_moving_dir[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                robot1_moving_dir[0] = False

            if event.key == pygame.K_RIGHT:
                robot1_moving_dir[1] = False

            if event.key == pygame.K_DOWN:
                robot1_moving_dir[2] = False

            if event.key == pygame.K_LEFT:
                robot1_moving_dir[3] = False

            if event.key == pygame.K_w:
                robot2_moving_dir[0] = False

            if event.key == pygame.K_d:
                robot2_moving_dir[1] = False

            if event.key == pygame.K_s:
                robot2_moving_dir[2] = False

            if event.key == pygame.K_a:
                robot2_moving_dir[3] = False

    if robot1_moving_dir[0]:
        robot1_pos.y -= velocity * dt
    if robot1_moving_dir[1]:
        robot1_pos.x += velocity * dt
    if robot1_moving_dir[2]:
        robot1_pos.y += velocity * dt
    if robot1_moving_dir[3]:
        robot1_pos.x -= velocity * dt

    if robot2_moving_dir[0]:
        robot2_pos.y -= velocity * dt
    if robot2_moving_dir[1]:
        robot2_pos.x += velocity * dt
    if robot2_moving_dir[2]:
        robot2_pos.y += velocity * dt
    if robot2_moving_dir[3]:
        robot2_pos.x -= velocity * dt

    screen.fill("black")

    screen.blit(robot, robot1_pos)
    screen.blit(robot, robot2_pos)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
