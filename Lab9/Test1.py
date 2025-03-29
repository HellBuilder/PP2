import pygame
import random

pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

car = pygame.image.load("Lab8\car.png")
car = pygame.transform.scale(car, (50, 100))
road = pygame.image.load("Lab8\!road.png")
road = pygame.transform.scale(road, (SCREEN_WIDTH, SCREEN_HEIGHT))
coin = pygame.image.load("Lab8\coin.png")
coin = pygame.transform.scale(coin, (30, 30))
large_coin = pygame.transform.scale(coin, (45, 45))
enemy = pygame.image.load("Lab8\enemy.png")
enemy = pygame.transform.scale(enemy, (50, 120))

# Car settings
car_rect = pygame.Rect(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 120, 50, 100)
car_speed = 5

# Coin settings
coins = []
for _ in range(4):
    coins.append([random.randint(50, SCREEN_WIDTH - 50), random.randint(-700, -50), 1, pygame.Rect(0, 0, 30, 30)])
coins.append([random.randint(50, SCREEN_WIDTH - 50), random.randint(-700, -50), 2, pygame.Rect(0, 0, 45, 45)])  # Larger coin worth 2 points
coin_speed = 5
collected_coins = 0

# Enemy settings
enemies = []
for _ in range(2):
    e_x = random.randint(50, SCREEN_WIDTH - 50)
    e_y = random.randint(-1000, -100)
    enemies.append([e_x, e_y, pygame.Rect(e_x, e_y, 70, 120)])
enemy_speed = 4

# Level settings
level = 1
running = True
clock = pygame.time.Clock()
while running:
    screen.blit(road, (0, 0))
    screen.blit(car, (car_rect.x, car_rect.y))
    
    for c in coins:
        c[3].topleft = (c[0], c[1])
        if c[2] == 1:
            screen.blit(coin, (c[0], c[1]))
        else:
            screen.blit(large_coin, (c[0], c[1]))
        c[1] += coin_speed
        if c[1] > SCREEN_HEIGHT:
            c[0], c[1] = random.randint(50, SCREEN_WIDTH - 50), random.randint(-700, -50)
        
        # Collision with car
        if car_rect.colliderect(c[3]):
            collected_coins += c[2]
            c[0], c[1] = random.randint(50, SCREEN_WIDTH - 50), random.randint(-700, -50)
    
    
    for e in enemies:
        e[2].topleft = (e[0], e[1])
        screen.blit(enemy, (e[0], e[1]))
        e[1] += enemy_speed
        if e[1] > SCREEN_HEIGHT:
            e[0], e[1] = random.randint(50, SCREEN_WIDTH - 50), random.randint(-1000, -100)
        
        
        if car_rect.colliderect(e[2]):
            running = False
    
    # Level progression
    if collected_coins >= level * 5:
        level += 1
        enemy_speed += 1
        coin_speed += 0.5
    
    
    font = pygame.font.Font(None, 36)
    text = font.render(f"Coins: {collected_coins}  Level: {level}", True, (255, 255, 255))
    screen.blit(text, (20, 20))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_rect.x > 0:
        car_rect.x -= car_speed
    if keys[pygame.K_RIGHT] and car_rect.x < SCREEN_WIDTH - car_rect.width:
        car_rect.x += car_speed
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
