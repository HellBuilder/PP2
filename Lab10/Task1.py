import pygame
import random
import psycopg2
import json

def connect_db():
    return psycopg2.connect(
        database="snake_game",
        user="postgres",
        password="loaded12345",
        host="localhost",
        port="5432"
    )

def get_user(username):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    row = cur.fetchone()
    if row:
        user_id = row[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
    conn.close()
    return user_id

def load_game_state(user_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT level, score, saved_state FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return row[0], row[1], row[2]
    return None

def save_game(user_id, level, score, snake, direction, food):
    conn = connect_db()
    cur = conn.cursor()
    data = {
        "snake": snake,
        "direction": direction,
        "food": food.position,
        "food_value": food.value
    }
    cur.execute("""
        INSERT INTO user_score (user_id, level, score, saved_state)
        VALUES (%s, %s, %s, %s)
    """, (user_id, level, score, json.dumps(data)))
    conn.commit()
    conn.close()

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
HEADER_HEIGHT = 40
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Evolution")

username = input("Enter your username: ")
user_id = get_user(username)
resume = input("Resume previous game? (y/n): ").lower() == 'y'

snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)
score = 0
level = 1
speed = 10
food_eaten = 0

class Food:
    def __init__(self, position=None, value=None):
        if position and value:
            self.position = position
            self.value = value
        else:
            self.spawn()
        self.start_time = pygame.time.get_ticks()

    def spawn(self):
        self.position = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(HEADER_HEIGHT // CELL_SIZE, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
        self.value = random.choice([1, 2, 3])
        self.start_time = pygame.time.get_ticks()

    def draw(self):
        color = ORANGE if self.value == 2 else RED if self.value == 3 else (255, 255, 0)
        pygame.draw.rect(screen, color, (*self.position, CELL_SIZE, CELL_SIZE))

    def is_expired(self):
        return pygame.time.get_ticks() - self.start_time > 7000

if resume:
    state = load_game_state(user_id)
    if state:
        level, score, saved_state = state
        snake = saved_state['snake']
        direction = tuple(saved_state['direction'])
        food = Food(position=tuple(saved_state['food']), value=saved_state['food_value'])
        speed = 10 + 2 * (level - 1)
        print(f"Resumed Level {level}, Score {score}")
    else:
        food = Food()
        print("No previous save found. Starting new game.")
else:
    food = Food()

clock = pygame.time.Clock()
game_active = True

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
            elif event.key == pygame.K_p:
                save_game(user_id, level, score, snake, direction, food)
                print("Game paused and saved. Press any key to resume.")
                paused = True
                while paused:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            paused = False
                            game_active = False
                        elif e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_ESCAPE:
                                paused = False
                                game_active = False
                            else:
                                paused = False

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if (
    new_head[0] < 0 or new_head[0] >= WIDTH or     # left or right wall
    new_head[1] < HEADER_HEIGHT or new_head[1] >= HEIGHT or  # top or bottom wall
    new_head in snake                              # snake hits itself
    ):
        save_game(user_id, level, score, snake, direction, food)
        print(f"Game over! Your score ({score}) has been saved.")
        pygame.quit()
        exit()



    snake.insert(0, new_head)

    food_rect = pygame.Rect(food.position[0], food.position[1], CELL_SIZE, CELL_SIZE)
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
