import pygame
import random
import math

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("RACEY")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

player_x = 370
player_y = 480
player_x_change = 0

enemy_x = random.randint(0, 735)
enemy_y = random.randint(50, 150)
enemy_y_change = 4

stick_radius = 10
stick_length = 80

def draw_stick_ball(x, y, color):
    pygame.draw.line(screen, color, (x, y - stick_length), (x, y))
    pygame.draw.circle(screen, color, (x, y), stick_radius)

def check_collision(player_x, player_y, enemy_x, enemy_y):
    distance = math.sqrt((player_x - enemy_x) ** 2 + (player_y - enemy_y) ** 2)
    if distance < 2 * stick_radius:
        return True
    return False

def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def display_menu(font, background_color):
    screen.fill(background_color)
    display_text("RACEY", font, WHITE, 300, 200)
    display_text("Нажмите SPACE чтобы начать", font, WHITE, 250, 300)
    display_text("Нажмите ESC чтобы выйти", font, WHITE, 250, 350)
    pygame.display.update()

font = pygame.font.Font(None, 36)

game_over = False
collision = False
menu = True

score = 0

clock = pygame.time.Clock()

background_color_start = (0, 0, 0)
background_color_end = (255, 255, 255)

while not game_over:
    t = pygame.time.get_ticks() / 4000.0
    r = int((1 + math.sin(t)) * 0.5 * (background_color_end[0] - background_color_start[0]) + background_color_start[0])
    g = int((1 + math.sin(t + 2.094)) * 0.5 * (background_color_end[1] - background_color_start[1]) + background_color_start[1])
    b = int((1 + math.sin(t + 4.188)) * 0.5 * (background_color_end[2] - background_color_start[2]) + background_color_start[2])
    background_color = pygame.Color(r, g, b)

    if menu:
        display_menu(font, background_color)
        pygame.mixer.music.load("cyber.mp3")
        pygame.mixer.music.play(-1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if menu:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False
                if event.key == pygame.K_ESCAPE:
                    game_over = True

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -5
                if event.key == pygame.K_RIGHT:
                    player_x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0

    if not game_over and not menu:
        clock.tick(240)

        player_x += player_x_change

        if player_x < stick_radius:
            player_x = stick_radius
        elif player_x > width - stick_radius:
            player_x = width - stick_radius

        if check_collision(player_x, player_y, enemy_x, enemy_y):
            game_over = True

        if not game_over:
            enemy_y += enemy_y_change

            if enemy_y > height:
                enemy_x = random.randint(stick_radius, width - stick_radius)
                enemy_y = random.randint(50, 150)
                score += 1

        screen.fill(background_color)

        draw_stick_ball(player_x, player_y, WHITE)
        draw_stick_ball(enemy_x, enemy_y, pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        display_text("Счет: " + str(score), font, WHITE, 10, 10)

        if game_over:
            display_text("Авария", font, WHITE, 300, 250)
            display_text("Нажмите SPACE чтобы играть снова", font, WHITE, 200, 300)
            pygame.display.update()

            restart = False
            while not restart:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        restart = True
                        game_over = False
                        player_x = 370
                        enemy_x = random.randint(stick_radius, width - stick_radius)
                        enemy_y = random.randint(50, 150)
                        score = 0
                        break
                    if event.type == pygame.QUIT:
                        restart = True
                        game_over = True
                        break

        pygame.display.update()

pygame.quit()
