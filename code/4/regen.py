import pygame
import sys
import random

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def left(self):
        self.x -= 5

    def right(self):
        self.x += 5

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), 20)

class Raindrop():
    def __init__(self, x, y=0):
        self.x = x
        self.y = y

    def down(self):
        self.y += 5

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), 5)

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Regen-Spiel")

# Set up the game loop
clock = pygame.time.Clock()

player = Player(400, 550)
raindrops = []

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        screen.blit(text, textpos)
        pygame.display.flip()
        continue

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.left()
    if keys[pygame.K_RIGHT]:
        player.right()

    screen.fill(GREEN)

    # Draw the red circle
    player.draw(screen)

    # randomly add new raindrop
    if random.randint(0, 100) < 15:
        raindrops.append(Raindrop(random.randint(0, WIDTH)))
    
    for raindrop in raindrops:
        raindrop.down()
        raindrop.draw(screen)

        # remove raindrop if it goes off screen
        if raindrop.y > 600:
            raindrops.remove(raindrop)

        # detect collision with player
        if raindrop.y > player.y - 20 and raindrop.y < player.y + 20 and raindrop.x > player.x - 20 and raindrop.x < player.x + 20:
            game_over = True
            raindrops.remove(raindrop)

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()