import pygame
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

brush_size = 15
shape_mode = "circle"
active_color = BLACK
eraser_enabled = False
background_color = WHITE

display_help = True
help_timer = time.time()

font = pygame.font.SysFont("Arial", 20)
instructions = [
    "Pygame Paint Controls:",
    "Left Mouse - Draw",
    "Right Mouse - Eraser",
    "Mouse Wheel - Resize Brush",
    "+ / -   - Resize Brush",
    "R - Rectangle Brush",
    "C - Circle Brush",
    "1 - Red Color",
    "2 - Green Color",
    "3 - Blue Color",
    "4 - Black Color",
    "E - Toggle Eraser",
    "SPACE - Clear Screen",
    "ESC - Close Help Window"
]

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(background_color)

def render_help_screen():
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(220)
    overlay.fill(WHITE)
    screen.blit(overlay, (0, 0))

    y_position = 100
    for line in instructions:
        text = font.render(line, True, BLACK)
        screen.blit(text, (WIDTH // 3, y_position))
        y_position += 30

running = True
while running:
    screen.blit(canvas, (0, 0))

    if display_help and time.time() - help_timer < 10:
        render_help_screen()
    else:
        display_help = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if shape_mode == "circle":
                    pygame.draw.circle(canvas, WHITE if eraser_enabled else active_color, event.pos, brush_size)
                elif shape_mode == "rectangle":
                    pygame.draw.rect(canvas, WHITE if eraser_enabled else active_color, (*event.pos, brush_size, brush_size))

            elif event.button == 3:
                pygame.draw.circle(canvas, background_color, event.pos, brush_size)

        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            if shape_mode == "circle":
                pygame.draw.circle(canvas, WHITE if eraser_enabled else active_color, event.pos, brush_size)
            elif shape_mode == "rectangle":
                pygame.draw.rect(canvas, WHITE if eraser_enabled else active_color, (*event.pos, brush_size, brush_size))

        elif event.type == pygame.MOUSEWHEEL:
            brush_size = max(5, min(100, brush_size + event.y))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                display_help = False
            elif event.key == pygame.K_SPACE:
                canvas.fill(background_color)
            elif event.key == pygame.K_r:
                shape_mode = "rectangle"
                eraser_enabled = False
            elif event.key == pygame.K_c:
                shape_mode = "circle"
                eraser_enabled = False
            elif event.key == pygame.K_e:
                eraser_enabled = not eraser_enabled
            elif event.key == pygame.K_1:
                active_color = RED
                eraser_enabled = False
            elif event.key == pygame.K_2:
                active_color = GREEN
                eraser_enabled = False
            elif event.key == pygame.K_3:
                active_color = BLUE
                eraser_enabled = False
            elif event.key == pygame.K_4:
                active_color = BLACK
                eraser_enabled = False
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                brush_size = min(100, brush_size + 5)
            elif event.key == pygame.K_MINUS:
                brush_size = max(5, brush_size - 5)

    pygame.display.flip()

pygame.quit()
