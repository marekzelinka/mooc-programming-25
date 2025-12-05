# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
dt = 0

robot = pygame.image.load("robot.png")
velocity_x = 300
velocity_y = 0
robot_pos = pygame.Vector2(0, 0)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    screen.blit(robot, robot_pos)

    pygame.display.flip()

    robot_pos.x += velocity_x * dt
    robot_pos.y += velocity_y * dt

    # Reached the top right corner, stop moving right and start moving down
    if velocity_x > 0 and robot_pos.x + robot.get_width() >= 640:
        velocity_x = 0
        velocity_y = 300

    # Reached the bottom right corner, stop moving down and start moving left
    if velocity_y > 0 and robot_pos.y + robot.get_height() >= 480:
        velocity_x = -300
        velocity_y = 0

    # Reached the bottom left corner, stop moving left and start moving up
    if velocity_x < 0 and robot_pos.x <= 0:
        velocity_x = 0
        velocity_y = -300

    # Reached the top left corner, stop moving up and start moving right
    if velocity_y < 0 and robot_pos.y <= 0:
        velocity_x = 300
        velocity_y = 0

    dt = clock.tick(60) / 1000

pygame.quit()
