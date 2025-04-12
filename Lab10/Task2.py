import pygame
import psycopg2
import csv

pygame.init()

WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PhoneBook GUI")
font = pygame.font.Font(None, 30)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)


def connect_db():
    return psycopg2.connect(
        database="phonebook_db1",
        user="postgres",
        password="loaded12345",
        host="localhost",
        port="5432"
    )

input_boxes = [pygame.Rect(150, 100, 300, 30), pygame.Rect(150, 160, 300, 30)]
current_input = ["", ""]
active_box = 0

def draw_gui():
    screen.fill(WHITE)
    title = font.render("PhoneBook Entry", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

    labels = ["Name:", "Phone:"]
    for i, label in enumerate(labels):
        txt = font.render(label, True, BLACK)
        screen.blit(txt, (50, 100 + i * 60))
        pygame.draw.rect(screen, GRAY if active_box == i else BLACK, input_boxes[i], 2)
        input_text = font.render(current_input[i], True, BLACK)
        screen.blit(input_text, (input_boxes[i].x + 5, input_boxes[i].y + 5))

    btn = font.render("[Enter] Add  |  [F1] Update  |  [F2] Delete", True, BLACK)
    screen.blit(btn, (WIDTH // 2 - btn.get_width() // 2, 250))
    pygame.display.flip()

def insert_entry(name, phone):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    conn.close()

def update_entry(name, phone):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
    conn.commit()
    conn.close()

def delete_entry(name_or_phone):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (name_or_phone, name_or_phone))
    conn.commit()
    conn.close()


running = True
clock = pygame.time.Clock()

while running:
    draw_gui()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, box in enumerate(input_boxes):
                if box.collidepoint(event.pos):
                    active_box = i
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                active_box = (active_box + 1) % 2
            elif event.key == pygame.K_RETURN:
                insert_entry(current_input[0], current_input[1])
                current_input = ["", ""]
            elif event.key == pygame.K_F1:
                update_entry(current_input[0], current_input[1])
                current_input = ["", ""]
            elif event.key == pygame.K_F2:
                delete_entry(current_input[0])
                current_input = ["", ""]
            elif event.key == pygame.K_BACKSPACE:
                current_input[active_box] = current_input[active_box][:-1]
            else:
                current_input[active_box] += event.unicode
    clock.tick(30)

pygame.quit()
