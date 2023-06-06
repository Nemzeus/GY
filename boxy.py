import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Boxy")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the player character
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5

# Set up the obstacles
obstacle_size = 50
obstacle_x = random.randint(0, width - obstacle_size)
obstacle_y = -obstacle_size
obstacle_speed = 3

# Set up points
points = 0
font = pygame.font.Font(None, 36)

# Set up game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    # Update obstacle position
    obstacle_y += obstacle_speed

    # Check for collision
    if (
        player_x < obstacle_x + obstacle_size
        and player_x + player_size > obstacle_x
        and player_y < obstacle_y + obstacle_size
        and player_y + player_size > obstacle_y
    ):
        points += 1
        obstacle_x = random.randint(0, width - obstacle_size)
        obstacle_y = -obstacle_size

    # Check if the player missed a square
    if obstacle_y > height:
        running = False

    # Draw everything on the screen
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(
        window, WHITE, (obstacle_x, obstacle_y, obstacle_size, obstacle_size)
    )

    # Display points
    text = font.render("Счет: " + str(points), True, WHITE)
    window.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

    # Limit frames per second
    clock.tick(60)

# Game over
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    window.fill(BLACK)
    game_over_text = font.render("GAME OVER", True, WHITE)
    window.blit(game_over_text, (width // 2 - 80, height // 2 - 18))
    pygame.display.update()
