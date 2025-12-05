# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
dt = 0

ball = pygame.image.load("ball.png")
velocity_x = 150
velocity_y = 150
ball_pos = pygame.Vector2(640 / 2 - ball.get_width(), 340)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    screen.blit(ball, ball_pos)

    ball_pos.x += velocity_x * dt
    ball_pos.y += velocity_y * dt

    if ball_pos.x + ball.get_width() >= 640:
        velocity_x = -velocity_x

    if ball_pos.y + ball.get_height() >= 480:
        velocity_y = -velocity_y

    if ball_pos.y < 0:
        velocity_y = -velocity_y

    if ball_pos.x < 0:
        velocity_x = -velocity_x

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
