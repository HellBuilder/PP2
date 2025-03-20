import pygame
import time
import math

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
mickey = pygame.image.load("Lab7\mickeyclock.png")
mickey = pygame.transform.scale(mickey, (300, 300))
minute_hand = pygame.image.load("Lab7\minute_hand.png")
second_hand = pygame.image.load("Lab7\second_hand.png")
center = (200, 200)

def rotate_image(image, angle, position):
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=position)
    return rotated_image, new_rect

def skip_time(seconds):
    global t_offset
    t_offset += seconds

t_offset = 0
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(mickey, (50, 50))
    t = time.localtime(time.time() + t_offset)
    sec_angle = 6 * t.tm_sec
    min_angle = 6 * t.tm_min
    
    sec_rotated, sec_rect = rotate_image(second_hand, sec_angle, center)
    min_rotated, min_rect = rotate_image(minute_hand, min_angle, center)
    
    screen.blit(sec_rotated, sec_rect.topleft)
    screen.blit(min_rotated, min_rect.topleft)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                skip_time(60)
            elif event.key == pygame.K_LEFT:
                skip_time(-60)
    
    pygame.display.flip()
    clock.tick(1)
pygame.quit()
