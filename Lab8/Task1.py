import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 700))

car = pygame.image.load("Lab8\car.png")
car = pygame.transform.scale(car, (50, 100))
road = pygame.image.load("Lab8\!road.png")
road = pygame.transform.scale(road, (500, 700))
coin = pygame.image.load("Lab8\coin.png")
coin = pygame.transform.scale(coin, (30, 30))

# Car settings
car_x, car_y = 500 // 2 - 25, 700 - 120
car_speed = 5

# Coin settings
coins = []
for _ in range(5):
    coins.append([random.randint(50, 500 - 50), random.randint(-700, -50)])
coin_speed = 5
collected_coins = 0

running = True
clock = pygame.time.Clock()
while running:
    screen.blit(road, (0, 0))
    screen.blit(car, (car_x, car_y))
    
    for c in coins:
        screen.blit(coin, (c[0], c[1]))
        c[1] += coin_speed
        if c[1] > 700:
            c[0], c[1] = random.randint(50, 500 - 50), random.randint(-700, -50)
        
        # Collision with car
        if car_x < c[0] < car_x + 50 and car_y < c[1] < car_y + 100:
            collected_coins += 1
            c[0], c[1] = random.randint(50, 500 - 50), random.randint(-700, -50)
    
    # Display coin count
    font = pygame.font.Font(None, 36)
    text = font.render(f"Coins: {collected_coins}", True, (255, 255, 255))
    screen.blit(text, (500 - 120, 20))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < 500 - 50:
        car_x += car_speed
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
