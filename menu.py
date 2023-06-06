import pygame
import os
import subprocess
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the list of games
games = {'RACEY': 'race.py', 'PONGY': 'pongy.py', 'BOXY': 'boxy.py', 'MOVY': 'movy.py'}

def display_menu():
    screen.fill(BACKGROUND_COLOR)

    for i, game in enumerate(games.keys()):
        text_surface = font.render(game, True, TEXT_COLOR)
        screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2 + i * 50))

    pygame.display.flip()

def handle_click(pos):
    for i, game in enumerate(games.keys()):
        text_surface = font.render(game, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 50))

        if text_rect.collidepoint(pos):
            run_game(games[game])

def run_game(game_file):
    subprocess.call([sys.executable, game_file])

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 1 is the left mouse button
                    handle_click(event.pos)

        display_menu()

    pygame.quit()

if __name__ == '__main__':
    main()
