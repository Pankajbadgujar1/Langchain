import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
SPEED = 10

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the snake and food variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE, random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]

# Set up the direction
direction = "RIGHT"

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Move the snake
    if direction == "UP":
        snake_pos[1] -= BLOCK_SIZE
    elif direction == "DOWN":
        snake_pos[1] += BLOCK_SIZE
    elif direction == "LEFT":
        snake_pos[0] -= BLOCK_SIZE
    elif direction == "RIGHT":
        snake_pos[0] += BLOCK_SIZE

    # Check for collision with food
    if snake_pos == food_pos:
        food_pos = [random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE, random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
    else:
        snake_body.append(list(snake_pos))
        if len(snake_body) > 100:
            snake_body.pop(0)

    # Check for collision with self or wall
    if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT or
            snake_pos in snake_body[:-1]):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)
    for x in snake_body:
        pygame.draw.rect(screen, WHITE, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])
    pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE])

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(SPEED)