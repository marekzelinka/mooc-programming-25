import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
dt = 0

robot = pygame.image.load("robot.png")
velocity = 300
robot_pos = pygame.Vector2(0, 0)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("green")

    screen.blit(robot, robot_pos)

    pygame.display.flip()

    robot_pos.x += velocity * dt

    if velocity > 0 and robot_pos.x + robot.get_width() >= 640:
        velocity = -velocity

    if velocity < 0 and robot_pos.x <= 0:
        velocity = -velocity

    dt = clock.tick(60) / 1000

pygame.quit()
