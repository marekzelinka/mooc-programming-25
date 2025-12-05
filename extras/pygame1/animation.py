import pygame

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
dt = 0

# Robot setup
robot = pygame.image.load("robot.png")
robot_pos = pygame.Vector2(0, 0)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the green color to wipe away anything from the last frame
    screen.fill("green")

    # Draw our robot at specific coords
    screen.blit(robot, robot_pos)

    # Flip the display to put new work on screen
    pygame.display.flip()

    # Move our robot one pixel to the right
    robot_pos.x += 300 * dt

    # Limit FPS to 60
    # dt is delta time in seconds since last frame
    # Used for framerate-independent physiscs
    dt = clock.tick(60) / 1000

pygame.quit()
