import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
dt = 0


robot = pygame.image.load("robot.png")
velocity = 150
robot_pos = pygame.Vector2(0, pygame.display.get_window_size()[1] - robot.get_height())
robot_moving = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                robot_moving = "up"
            if event.key == pygame.K_RIGHT:
                robot_moving = "right"
            if event.key == pygame.K_DOWN:
                robot_moving = "down"
            if event.key == pygame.K_LEFT:
                robot_moving = "left"

        if event.type == pygame.KEYUP:
            robot_moving = None

    if robot_moving == "up":
        robot_pos.y -= velocity * dt
    if robot_moving == "right":
        robot_pos.x += velocity * dt
    if robot_moving == "down":
        robot_pos.y += velocity * dt
    if robot_moving == "left":
        robot_pos.x -= velocity * dt

    screen.fill("black")

    screen.blit(robot, robot_pos)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
