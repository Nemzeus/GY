import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
BALL_SIZE = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 80, 15
FPS = 60
BALL_SPEED = 2
PADDLE_SPEED = 5
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pongy")

ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

ball_dx = ball_dy = BALL_SPEED
paddle_dx = 0

score = 0

font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_dx = -PADDLE_SPEED
            elif event.key == pygame.K_RIGHT:
                paddle_dx = PADDLE_SPEED

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                paddle_dx = 0

    ball.x += ball_dx
    ball.y += ball_dy

    if ball.top <= 0 or ball.left <= 0 or ball.right >= WIDTH:
        ball_dy *= -1
        ball_dx *= -1

    if ball.colliderect(paddle):
        ball_dy *= -1
        score += 1

    if ball.bottom >= HEIGHT:
        running = False

    paddle.x += paddle_dx

    if paddle.left <= 0:
        paddle.left = 0
    if paddle.right >= WIDTH:
        paddle.right = WIDTH

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    score_text = font.render("Счет: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    if not running:
        game_over_text = font.render("GAME OVER", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()

    pygame.time.Clock().tick(FPS)

pygame.quit()
