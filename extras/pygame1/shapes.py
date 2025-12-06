import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Great Adventure")
running = True

pygame.draw.rect(screen, (0, 255, 0), (50, 100, 200, 250))
pygame.draw.circle(screen, (255, 0, 0), (200, 150), 75)
pygame.draw.line(screen, (0, 0, 255), (80, 120), (300, 160), 2)

pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
