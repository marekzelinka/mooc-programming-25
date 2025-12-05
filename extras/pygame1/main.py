import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
# window.blit(robot, (0, 0))
# window.blit(robot, (300, 0))
# window.blit(robot, (0, 300))
# window.blit(robot, (100, 200))
window.blit(robot, (320 - robot.get_width() / 2, 240 - robot.get_height() / 2))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
