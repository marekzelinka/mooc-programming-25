# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

robot_start_x_pos = 50
robot_y_pos = 100
robot_count = 10

for x_position in range(
    robot_start_x_pos, robot.get_width() * (robot_count + 1), robot.get_width()
):
    window.blit(robot, (x_position, robot_y_pos))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
