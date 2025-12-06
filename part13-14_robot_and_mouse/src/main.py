# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
dt = 0


robot = pygame.image.load("robot.png")
velocity = 150
robot_pos = pygame.Vector2(0, 0)

# target_pos = pygame.Vector2(0, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            robot_pos.x = event.pos[0] - robot.get_width() / 2
            robot_pos.y = event.pos[1] - robot.get_height() / 2

    # if robot_pos.x > target_pos.x:
    #     robot_pos.x -= velocity * dt
    # if robot_pos.x < target_pos.x:
    #     robot_pos.x += velocity * dt
    # if robot_pos.y > target_pos.y:
    #     robot_pos.y -= velocity * dt
    # if robot_pos.y < target_pos.y:
    #     robot_pos.y += velocity * dt

    screen.fill("black")
    screen.blit(robot, robot_pos)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
