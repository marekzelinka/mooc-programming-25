import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Great Adventure")
running = True

game_font = pygame.font.SysFont("Arial", 24)
text = game_font.render("Hello there!", True, (255, 0, 0))
screen.blit(text, (100, 50))

pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
