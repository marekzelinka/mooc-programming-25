# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))


def draw_row(start_x_pos, start_y_pos):
    for x_pos in range(
        start_x_pos,
        start_x_pos + ((robot.get_width() - 10) * 10),
        robot.get_width() - 10,
    ):
        window.blit(robot, (x_pos, start_y_pos))


curr_x_pos = 50
curr_y_pos = 100

for y in range(10):
    draw_row(curr_x_pos, curr_y_pos)
    curr_x_pos += 10
    curr_y_pos += 20

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
