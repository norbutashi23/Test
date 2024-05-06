# pingpong.py

from ast import main
import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define game constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20

class Ball:
    def __init__(self):
        """Initialize the ball object."""
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x = random.choice([-3, 3])
        self.speed_y = 2

    def move(self):
        """Update the ball's position based on its speed."""
        self.x += self.speed_x
        self.y += self.speed_y

    def check_collision(self):
        """Check for collisions with the walls and reverse the ball's speed accordingly."""
        if self.x <= BALL_RADIUS or self.x >= WIDTH - BALL_RADIUS:
            self.speed_x = -self.speed_x
        if self.y <= BALL_RADIUS:
            self.speed_y = -self.speed_y

class Paddle:
    def __init__(self):
        """Initialize the paddle object."""
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - self.height - 10

    def move(self, direction: str):
        """Move the paddle left or right based on the provided direction."""
        if direction == "left" and self.x > 0:
            self.x -= 10
        elif direction == "right" and self.x < WIDTH - self.width:
            self.x += 10

class Game:
    def __init__(self):
        """Initialize the game object."""
        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False

    def handle_events(self):
        """Handle events like quitting the game."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True

    def update(self):
        """Update the game state."""
        self.ball.move()
        self.ball.check_collision()
        if self.ball.y >= HEIGHT - BALL_RADIUS - PADDLE_HEIGHT:
            if self.paddle.x <= self.ball.x <= self.paddle.x + PADDLE_WIDTH:
                self.ball.y = HEIGHT - BALL_RADIUS - PADDLE_HEIGHT - 1
                self.ball.speed_y = -self.ball.speed_y
                self.score += 1
            else:
                self.game_over = True

    def draw(self, screen):
        """Draw the game objects on the screen."""
        screen.fill(BLACK)
        pygame.draw.circle(screen, WHITE, (self.ball.x, self.ball.y), BALL_RADIUS)
        pygame.draw.rect(screen, WHITE, (self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height))
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        if self.game_over:
            game_over_text = self.font.render(f"Your score: {self.score}", True, WHITE)
            game_over_rect = game_over_text.get_rect ()
            game_over_rect.center = (WIDTH // 2, HEIGHT // 2)
            screen.bit(game_over_text, game_over_rect)
            
    def main():
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ping Pong")
        clock = pygame.time.Clock()
        game = Game()
        
        while not game.game_over:
            game.handle_events()
            
            keys = pygame.key.get_pressed()
            if keys [pygame.K_LEFT]:
                game.paddle.move("left")
            if keys [pygame.K_RIGHT]:
                game.paddle.move("right")
                
            game.update()
            game.draw(screen)
            
            pygame.display.flip()
            clock.tick(60)
            pygame.quit()
        main()