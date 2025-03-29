import pygame
import random

pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
HEADER_HEIGHT = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Evolution")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# Initial snake setup
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)

# Game parameters
score = 0
level = 1
speed = 10
food_eaten = 0
clock = pygame.time.Clock()
game_active = True

# Food class
class Food:
    def __init__(self):
        self.spawn()
        self.start_time = pygame.time.get_ticks()

    def spawn(self):
        self.position = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(HEADER_HEIGHT // CELL_SIZE, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
        self.value = random.choice([1, 2, 3])
        self.size = CELL_SIZE if self.value == 3 else CELL_SIZE * self.value
        self.start_time = pygame.time.get_ticks()

    def draw(self):
        color = ORANGE if self.value == 2 else RED if self.value == 3 else (255, 255, 0)
        pygame.draw.rect(screen, color, (*self.position, self.size, self.size))

    def is_expired(self):
        return pygame.time.get_ticks() - self.start_time > 7000

food = Food()

while game_active:
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEADER_HEIGHT))
    display_text = pygame.font.Font(None, 30).render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(display_text, (10, 10))

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

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    # Check for collisions
    if new_head in snake or new_head[0] < 0 or new_head[1] < HEADER_HEIGHT or new_head[0] >= WIDTH or new_head[1] >= HEIGHT:
        pygame.quit()
        exit()
    
    snake.insert(0, new_head)

    # Check for food collision
    food_rect = pygame.Rect(food.position[0], food.position[1], food.size, food.size)
    head_rect = pygame.Rect(new_head[0], new_head[1], CELL_SIZE, CELL_SIZE)
    
    if head_rect.colliderect(food_rect):
        score += food.value
        food.spawn()
        food_eaten += 1
        
        if food_eaten % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    if food.is_expired():
        food.spawn()

    food.draw()

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
