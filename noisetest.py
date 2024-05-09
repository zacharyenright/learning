import pygame
import noise
import random

# Constants
MAP_WIDTH = 1280
MAP_HEIGHT = 720
SCALE = 0.05
OCTAVES = 6
PERSISTENCE = 0.5
LACUNARITY = 2.0
ENEMY_COUNT = 10

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
pygame.display.set_caption("Random Level with Enemies")
clock = pygame.time.Clock()

# Generate noise map for level layout
def generate_noise_map(width, height, scale, octaves, persistence, lacunarity):
    noise_map = [[0] * height for _ in range(width)]
    for y in range(height):
        for x in range(width):
            nx = x / width - 0.5
            ny = y / height - 0.5
            noise_map[x][y] = noise.pnoise2(nx * scale, ny * scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=width, repeaty=height, base=0)
    return noise_map

# Randomly place enemies on the map
def place_enemies(noise_map):
    enemies = []
    for _ in range(ENEMY_COUNT):
        x = random.randint(0, MAP_WIDTH - 1)
        y = random.randint(0, MAP_HEIGHT - 1)
        # Ensure enemy is placed on ground or passable terrain
        if noise_map[x][y] < 0:
            enemies.append((x, y))
    return enemies

# Render the level layout
def render_level(noise_map):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            # Example: Thresholds for ground and obstacles
            if noise_map[x][y] < 0:
                color = (0, 255, 0)  # Ground
            else:
                color = (128, 128, 128)  # Obstacle
            pygame.draw.rect(window, color, (x, y, 1, 1))

# Render enemies on the map
def render_enemies(enemies):
    for enemy in enemies:
        pygame.draw.circle(window, (255, 0, 0), enemy, 5)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate noise map for level layout
    noise_map = generate_noise_map(MAP_WIDTH, MAP_HEIGHT, SCALE, OCTAVES, PERSISTENCE, LACUNARITY)

    # Place enemies randomly on the map
    enemies = place_enemies(noise_map)

    # Render the level layout
    render_level(noise_map)

    # Render enemies
    render_enemies(enemies)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
