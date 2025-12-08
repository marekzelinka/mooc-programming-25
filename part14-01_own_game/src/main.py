import random

import pygame


class CoinHeist:
    COINS_WIN_COUNT = 100

    def __init__(self) -> None:
        """Initialize the pygame module and sets up necessary resources involved in the game."""

        # Initialize pygame resources
        pygame.init()

        self.load_images()

        self.screen_height = 640
        self.screen_width = 480
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Coin Heist")

        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.SysFont("Arial", 24)
        self.running = True
        self.new_game()

        # Start the main game loop
        self.main_loop()

    def load_images(self) -> None:
        """Loads the images used in the game."""
        try:
            self.robot_image = pygame.image.load("robot.png")
            self.coin_image = pygame.image.load("coin.png")
        except pygame.error as e:
            print(
                f"Error loading images: {e}. Make sure 'robot.png' and 'coin.png' exist."
            )

            self.quit()

    def new_game(self) -> None:
        """Resets the game state for a new game."""
        self.game_over = False

        # Initialize robot position at the bottom center of the screen
        self.robot_x = self.screen_width / 2 - self.robot_image.get_width() / 2
        self.robot_y = self.screen_height - self.robot_image.get_height()
        self.robot_velocity = 5  # Increased velocity slightly for better movement
        self.coins_collected = 0

        # Robot movement flags
        self.move_to_left = False
        self.move_to_right = False

        # Coin setup
        self.coin_spawn_count = 5
        self.coin_positions = []  # Stores the x and y coordinates for each coin
        self.coin_velocity = 3  # Base speed for falling coins

        # Populate the initial coin positions (starting off-screen above)
        for _ in range(self.coin_spawn_count):
            self.coin_positions.append(
                [
                    random.randint(0, self.screen_width - self.coin_image.get_width()),
                    # Start coins at random negative y coordinates to stagger their appearance
                    -random.randint(50, 600),
                ]
            )

    def quit(self) -> None:
        """Stops a running game and cleans up pygame resources."""
        self.running = False

        # Cleanup pygame resources
        pygame.quit()

    def main_loop(self) -> None:
        """Starts the game loop.

        Handles events, updates game state, and draws the screen content for each frame.
        """
        while self.running:
            self.check_events()

            if not self.game_over:
                self.update_game_state()

            self.draw_screen()

            self.clock.tick(60)

    def check_events(self) -> None:
        """Check collected events for every iteration (e.g., keyboard input, quitting the game)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F2:
                    # Restart the game if F2 is pressed
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    # Quit the game when Esc is pressed
                    self.quit()

                if event.key == pygame.K_LEFT:
                    self.move_to_left = True
                if event.key == pygame.K_RIGHT:
                    self.move_to_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.move_to_left = False
                if event.key == pygame.K_RIGHT:
                    self.move_to_right = False

    def update_game_state(self) -> None:
        """Updates the position of game objects and checks for collisions or game conditions."""

        # 1. Update Robot Position based on input flags and screen boundaries
        if self.move_to_right:
            # Ensure robot stays within the right boundary
            if self.robot_x + self.robot_image.get_width() < self.screen_width:
                self.robot_x += self.robot_velocity
        if self.move_to_left:
            # Ensure robot stays within the left boundary
            if self.robot_x > 0:
                self.robot_x -= self.robot_velocity

        # 2. Update Coin Positions and Check Collisions/Misses
        for i in range(self.coin_spawn_count):
            # Move coin down
            self.coin_positions[i][1] += self.coin_velocity

            coin_rect = pygame.Rect(
                self.coin_positions[i][0],
                self.coin_positions[i][1],
                self.coin_image.get_width(),
                self.coin_image.get_height(),
            )
            robot_rect = pygame.Rect(
                self.robot_x,
                self.robot_y,
                self.robot_image.get_width(),
                self.robot_image.get_height(),
            )

            reset_coin_position = False

            # Check if coin has reached the bottom boundary, means the robot missed
            if coin_rect.bottom >= self.screen_height:
                self.coins_collected -= 1
                reset_coin_position = True

                # Reset speed if coin collected is bellow 10
                if self.coins_collected < 10:
                    self.coin_velocity = 3

            if self.coins_collected == CoinHeist.COINS_WIN_COUNT:
                # Game over condition: The required amount has been collected
                self.game_over = True

            # Check for collision with the robot using built-in Pygame collision detection
            if coin_rect.colliderect(robot_rect):
                # The robot caught a coin
                self.coins_collected += 1
                reset_coin_position = True

                # Reset speed as a difficulty curve
                if self.coins_collected % 10 == 0:
                    self.coin_velocity += 0.5

            if reset_coin_position:
                # Reset the coin to a new random position above the screen when its caught or it reached the ground
                self.coin_positions[i][0] = random.randint(
                    0, self.screen_width - self.coin_image.get_width()
                )
                self.coin_positions[i][1] = -random.randint(
                    50, 600
                )  # Reset Y position off-screen for stagger effect

    def draw_screen(self) -> None:
        """Updates the contents of the window by drawing all elements."""
        # Fill the screen with a black background (RGB 0, 0, 0)
        self.screen.fill("black")

        # Draw the robot at its current position
        self.screen.blit(self.robot_image, (self.robot_x, self.robot_y))

        # Draw all active coins
        for i in range(self.coin_spawn_count):
            self.screen.blit(
                self.coin_image, (self.coin_positions[i][0], self.coin_positions[i][1])
            )

        # Render the current score
        score_text = self.game_font.render(
            f"Points: {self.coins_collected}/{CoinHeist.COINS_WIN_COUNT}",
            True,
            "red",
        )
        self.screen.blit(
            score_text, (self.screen_width - score_text.get_width() - 10, 10)
        )

        if self.game_over:
            # Create a semi-transparent overlay surface
            overlay = pygame.Surface(
                (self.screen_width, self.screen_height), pygame.SRCALPHA
            )
            overlay.fill((0, 0, 0, 180))  # Black with 70% transparency
            self.screen.blit(overlay, (0, 0))

            # Display "Game Over" message
            game_font = pygame.font.SysFont("Arial", 48, bold=True)
            game_text = game_font.render("YOU WON", True, "red")
            text_rect = game_text.get_rect(
                center=(self.screen_width / 2, self.screen_height / 2 - 50)
            )
            self.screen.blit(game_text, text_rect)

            # Display info about how to restart the game
            game_font = pygame.font.SysFont("Arial", 20)
            game_text = game_font.render(
                "Press F2 to restart or ESC to quit", True, "white"
            )
            restart_rect = game_text.get_rect(
                center=(self.screen_width / 2, self.screen_height / 2 + 20)
            )
            self.screen.blit(game_text, restart_rect)

        pygame.display.flip()


if __name__ == "__main__":
    CoinHeist()
