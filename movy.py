import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Movy")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
dot_color = (255, 0, 0)

# Dot
dot_radius = 10
dots = []
num_dots = 20

for _ in range(num_dots):
    dot_x = random.randint(0, screen_width - dot_radius * 2)
    dot_y = random.randint(0, screen_height - dot_radius * 2)
    dot_dx = random.randint(-3, 3)
    dot_dy = random.randint(-3, 3)
    dots.append((dot_x, dot_y, dot_dx, dot_dy))


# Game variables
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Check if any dot was clicked
            for i, dot in enumerate(dots):
                dot_x, dot_y, _, _ = dot

                # Check if the mouse click is inside the dot
                if dot_x <= mouse_pos[0] <= dot_x + dot_radius * 2 and dot_y <= mouse_pos[1] <= dot_y + dot_radius * 2:
                    # Remove the clicked dot and increase the score
                    dots.pop(i)
                    score += 1

    # Clear the screen
    screen.fill(black)

    # Update and draw the dots
    for i, dot in enumerate(dots):
        dot_x, dot_y, dot_dx, dot_dy = dot

        # Update dot position
        dot_x += dot_dx
        dot_y += dot_dy

        # Bounce off the edges of the screen
        if dot_x <= 0 or dot_x >= screen_width - dot_radius * 2:
            dot_dx *= -1
        if dot_y <= 0 or dot_y >= screen_height - dot_radius * 2:
            dot_dy *= -1

        # Update the dot in the list
        dots[i] = (dot_x, dot_y, dot_dx, dot_dy)

        # Draw the dot
        pygame.draw.circle(screen, dot_color, (dot_x + dot_radius, dot_y + dot_radius), dot_radius)

    # Draw the score
    score_text = font.render(f"Счет: {score}", True, white)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
