import pygame
import time
import math

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
ball_x, ball_y = 250, 250
radius = 25
speed = 20

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), radius)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - speed - radius >= 0:
                ball_y -= speed
            elif event.key == pygame.K_DOWN and ball_y + speed + radius <= 500:
                ball_y += speed
            elif event.key == pygame.K_LEFT and ball_x - speed - radius >= 0:
                ball_x -= speed
            elif event.key == pygame.K_RIGHT and ball_x + speed + radius <= 500:
                ball_x += speed
    
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
