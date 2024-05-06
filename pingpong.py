# pingpong.py

import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define game constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20

class Ball:
    def __init__(self) -> None:
        """Initialize the ball object."""
        self.x_position = SCREEN_WIDTH // 2
        self.y_position = SCREEN_HEIGHT // 2
        self.x_speed = random.choice([-3, 3])
        self.y_speed = 2

    def move(self) -> None:
        """Update the ball's position based on its speed."""
        self.x_position += self.x_speed
        self.y_position += self.y_speed

    def check_collision(self) -> None:
        """Check for collisions with the walls and reverse the ball's speed accordingly."""
        if self.x_position <= BALL_RADIUS or self.x_position >= SCREEN_WIDTH - BALL_RADIUS:
            self.x_speed = -self.x_speed
        if self.y_position <= BALL_RADIUS:
            self.y_speed = -self.y_speed

class Paddle:
    def __init__(self) -> None:
        """Initialize the paddle object."""
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.x_position = (SCREEN_WIDTH - self.width) // 2
        self.y_position = SCREEN_HEIGHT - self.height - 10

    def move(self, direction: str) -> None:
        """Move the paddle left or right based on the provided direction."""
        if direction == "left" and self.x_position > 0:
            self.x_position -= 10
        elif direction == "right" and self.x_position < SCREEN_WIDTH - self.width:
            self.x_position += 10

class Game:
    def __init__(self) -> None:
        """Initialize the game object."""
        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False

    def handle_events(self) -> None:
        """Handle events like quitting the game."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True

    def update(self) -> None:
        """Update the game state."""
        self.ball.move()
        self.ball.check_collision()
        if self.ball.y_position >= SCREEN_HEIGHT - BALL_RADIUS - PADDLE_HEIGHT:
            if self.paddle.x_position <= self.ball.x_position <= self.paddle.x_position + PADDLE_WIDTH:
                self.ball.y_position = SCREEN_HEIGHT - BALL_RADIUS - PADDLE_HEIGHT - 1
                self.ball.y_speed = -self.ball.y_speed
                self.score += 1
            else:
                self.game_over = True

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the game objects on the screen."""
        screen.fill(BLACK)
        pygame.draw.circle(screen, WHITE, (self.ball.x_position, self.ball.y_position), BALL_RADIUS)
        pygame.draw.rect(screen, WHITE, (self.paddle.x_position, self.paddle.y_position, self.paddle.width, self.paddle.height))
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        if self.game_over:
            game_over_text = self.font.render(f"Your score: {self.score}", True, WHITE)
            game