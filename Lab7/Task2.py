import pygame
import time
import math


pygame.init()
screen = pygame.display.set_mode((400, 300))
songs = ["Lab7\music1.mp3", "Lab7\music2.mp3", "Lab7\music3.mp3", "Lab7\music4.mp3"]
current_song = 0
pygame.mixer.init()
pygame.mixer.music.load(songs[current_song])

buttons = {
    "Play": pygame.Rect(50, 200, 80, 40),
    "Stop": pygame.Rect(150, 200, 80, 40),
    "Next": pygame.Rect(250, 200, 80, 40),
    "Prev": pygame.Rect(350, 200, 80, 40)
}

def draw_buttons():
    for text, rect in buttons.items():
        pygame.draw.rect(screen, (0, 200, 0), rect)
        font = pygame.font.Font(None, 24)
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, rect.move(10, 10))

running = True
while running:
    screen.fill((0, 0, 0))
    draw_buttons()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for text, rect in buttons.items():
                if rect.collidepoint(event.pos):
                    if text == "Play":
                        pygame.mixer.music.play()
                    elif text == "Stop":
                        pygame.mixer.music.stop()
                    elif text == "Next":
                        current_song = (current_song + 1) % len(songs)
                        pygame.mixer.music.load(songs[current_song])
                        pygame.mixer.music.play()
                    elif text == "Prev":
                        current_song = (current_song - 1) % len(songs)
                        pygame.mixer.music.load(songs[current_song])
                        pygame.mixer.music.play()
    
    pygame.display.flip()
pygame.quit()
