import pygame

pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

active_color = BLACK
shape_mode = None
background_color = WHITE
start_pos = None
drawing = False
temp_surface = None
free_drawing = False

# Shape drawing functions
def draw_right_triangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    points = [(x1, y1), (x2, y1), (x1, y2)]
    pygame.draw.polygon(surface, color, points)

def draw_equilateral_triangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    size = abs(x2 - x1)
    height = (3 ** 0.5 / 2) * size
    points = [(x1, y1 + height), (x1 + size / 2, y1), (x1 + size, y1 + height)]
    pygame.draw.polygon(surface, color, points)

def draw_rhombus(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    points = [(x1 + width // 2, y1), (x2, y1 + height // 2), (x1 + width // 2, y2), (x1, y1 + height // 2)]
    pygame.draw.polygon(surface, color, points)

# Button setup
buttons = {
    "square": pygame.Rect(10, 10, 100, 40),
    "right_triangle": pygame.Rect(120, 10, 100, 40),
    "equilateral_triangle": pygame.Rect(230, 10, 100, 40),
    "rhombus": pygame.Rect(340, 10, 100, 40)
}

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(background_color)

running = True
while running:
    screen.fill(GRAY)
    screen.blit(canvas, (0, 50))
    if drawing and temp_surface:
        screen.blit(temp_surface, (0, 50))
    
    # Draw buttons
    for shape, rect in buttons.items():
        color = GREEN if shape_mode == shape else WHITE
        pygame.draw.rect(screen, color, rect)
        text = pygame.font.Font(None, 24).render(shape.replace("_", " ").title(), True, BLACK)
        screen.blit(text, (rect.x + 10, rect.y + 10))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for shape, rect in buttons.items():
                    if rect.collidepoint(event.pos):
                        shape_mode = shape if shape_mode != shape else None
                        break
                else:
                    start_pos = event.pos
                    if shape_mode:
                        drawing = True
                        temp_surface = canvas.copy()
                    else:
                        free_drawing = True

        elif event.type == pygame.MOUSEMOTION:
            if free_drawing and pygame.mouse.get_pressed()[0]:
                pygame.draw.circle(canvas, active_color, event.pos, 3)
            elif drawing:
                temp_surface = canvas.copy()
                end_pos = event.pos
                if shape_mode == "square":
                    width = abs(end_pos[0] - start_pos[0])
                    pygame.draw.rect(temp_surface, active_color, (*start_pos, width, width))
                elif shape_mode == "right_triangle":
                    draw_right_triangle(temp_surface, active_color, start_pos, end_pos)
                elif shape_mode == "equilateral_triangle":
                    draw_equilateral_triangle(temp_surface, active_color, start_pos, end_pos)
                elif shape_mode == "rhombus":
                    draw_rhombus(temp_surface, active_color, start_pos, end_pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if drawing:
                    end_pos = event.pos
                    if shape_mode == "square":
                        width = abs(end_pos[0] - start_pos[0])
                        pygame.draw.rect(canvas, active_color, (*start_pos, width, width))
                    elif shape_mode == "right_triangle":
                        draw_right_triangle(canvas, active_color, start_pos, end_pos)
                    elif shape_mode == "equilateral_triangle":
                        draw_equilateral_triangle(canvas, active_color, start_pos, end_pos)
                    elif shape_mode == "rhombus":
                        draw_rhombus(canvas, active_color, start_pos, end_pos)
                    drawing = False
                    temp_surface = None
                free_drawing = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                active_color = RED
            elif event.key == pygame.K_2:
                active_color = GREEN
            elif event.key == pygame.K_3:
                active_color = BLUE
            elif event.key == pygame.K_4:
                active_color = BLACK
    
    pygame.display.flip()

pygame.quit()
