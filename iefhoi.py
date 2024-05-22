import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the paddles
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Define the ball
BALL_SIZE = 20
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Set up the game clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= 5
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += 5
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= 5
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += 5

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1

    # Ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
