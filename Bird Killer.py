import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bird Hunter Demo")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player (shooter) properties
player_width = 50
player_height = 20
player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 7

# Bird properties
bird_width = 40
bird_height = 20
birds = []
bird_speed = 3

# Egg properties
egg_width = 10
egg_height = 10
eggs = []
egg_speed = 5

# Bullet properties
bullet_width = 5
bullet_height = 10
bullets = []
bullet_speed = 7

# Score
score = 0

# Game over flag
game_over = False

# Font
font = pygame.font.SysFont(None, 36)

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_width, player_height))

def draw_bird(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, bird_width, bird_height))

def draw_egg(x, y):
    pygame.draw.rect(screen, RED, (x, y, egg_width, egg_height))

def draw_bullet(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, bullet_width, bullet_height))

def show_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed
    # if keys[pygame.K_UP] and player_y > 0:
    #     player_y += player_speed
    # if keys[pygame.K_DOWN] and player_y :
    #     player_y -= player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 6:  # Limit the number of bullets on screen
            bullets.append([player_x + player_width // 2, player_y])

    # Update bird positions
    for bird in birds:
        bird[0] += bird[2]  # Update x position
        if bird[0] < 0 or bird[0] > SCREEN_WIDTH - bird_width:
            bird[2] *= -1  # Reverse direction
        if random.random() < 0.005:  # Randomly drop eggs
            eggs.append([bird[0] + bird_width // 2, bird[1] + bird_height])

    # Update egg positions
    for egg in eggs[:]:
        egg[1] += egg_speed
        if egg[1] > SCREEN_HEIGHT:
            eggs.remove(egg)
        elif player_x < egg[0] < player_x + player_width and player_y < egg[1] < player_y + player_height:
            game_over = True

    # Update bullet positions
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Check for bullet collisions with birds
    birds_to_remove = []
    bullets_to_remove = []

    for bird in birds:
        for bullet in bullets:
            if (
                bird[0] < bullet[0] < bird[0] + bird_width
                and bird[1] < bullet[1] < bird[1] + bird_height
            ):
                if bird not in birds_to_remove:
                    birds_to_remove.append(bird)
                if bullet not in bullets_to_remove:
                    bullets_to_remove.append(bullet)

    # Remove collided birds and bullets
    for bird in birds_to_remove:
        if bird in birds:
            birds.remove(bird)
            score += 10 

    for bullet in bullets_to_remove:
        if bullet in bullets:
            bullets.remove(bullet)
        
    # Spawn new birds
    if random.random() < 0.005:
        birds.append([random.randint(0, SCREEN_WIDTH - bird_width), random.randint(50, 200), bird_speed])

    # Draw objects
    draw_player(player_x, player_y)
    for bird in birds:
        draw_bird(bird[0], bird[1])
    for egg in eggs:
        draw_egg(egg[0], egg[1])
    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])

    show_score()

    # Check for game over
    if game_over:
        game_over_text = font.render("Game Over", True, RED)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
