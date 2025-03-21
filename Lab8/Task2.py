import pygame
import random

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 500
CELL_SIZE = 20
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

snake_body = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)

def generate_food():
    while True:
        food_position = (random.randint(0, (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
        if food_position not in snake_body:
            return food_position

food = generate_food()
points = 0
stage = 1
velocity = 10
frame_rate = pygame.time.Clock()

game_active = True
while game_active:
    window.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    new_position = (snake_body[0][0] + direction[0], snake_body[0][1] + direction[1])
    if new_position in snake_body or new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= SCREEN_WIDTH or new_position[1] >= SCREEN_HEIGHT:
        game_active = False

    snake_body.insert(0, new_position)

    if new_position == food:
        food = generate_food()
        points += 1
        if points % 3 == 0:
            stage += 1
            velocity += 2
    else:
        snake_body.pop()

    pygame.draw.rect(window, RED, (*food, CELL_SIZE, CELL_SIZE))

    for segment in snake_body:
        pygame.draw.rect(window, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    font = pygame.font.Font(None, 30)
    text = font.render(f"Score: {points}  Level: {stage}", True, BLACK)
    window.blit(text, (10, 10))

    pygame.display.flip()
    frame_rate.tick(velocity)

pygame.quit()