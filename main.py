import pygame
from pygame import mixer
import sys
from player import Player
from map import Border, Enemy, Coin
import random
import noise
pygame.init()
mixer.init()
mixer.music.set_volume(0.7)

curr_level = 0
res = (1280, 720)  # Set Resolution
window = pygame.display.set_mode(res)  # Set window size equal to resolution
pygame.display.set_caption("Random Levels")  # Window name
clock = pygame.time.Clock()  # Create the clock object
FPS = 60  # Variable to limit FPS
font = pygame.font.Font(None, 36)  # Set font
win_font = pygame.font.Font(None, 200)
main_menu_font = pygame.font.Font(None, 100)
keys = pygame.key.get_pressed()
pygame.mixer.music.load("level_win.wav")

# Get player from player.py
player = Player(50, 720/2-50, 50, 50, (0, 0, 255))

# Get map instance
map_instance = Border()

# Get enemy from map.py
enemy = Enemy(1280/2-50, 720/2-50, 50, 50, (255, 0, 0))

# Get coin from map.py
coin = Coin(random.randint(700, 1270), random.randint(10, 710), 50, 50, (255, 255, 0))

enemy_positions = []
enemies_generated = False


def load_level(level):
    pygame.mixer.music.stop()  # Stop music playback after it has been played once
    level += 1
    global curr_level
    curr_level = level

    # Reposition player
    player.rect.x, player.rect.y = 50, res[1] / 2 - 50

    # Reposition enemy
    enemy.rect.x, enemy.rect.y = random.randint(50, 1200), random.randint(80, 660)

    # Reposition coin
    coin.rect.x, coin.rect.y = random.randint(50, 1200), random.randint(80, 660)

    # Reset player speed
    player.speed = 5


def game():
    level_loaded = False
    level_won = False
    while True:
        if not level_loaded:
            load_level(curr_level)
            level_loaded = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        curr_level_text = font.render("Level: " + str(curr_level), True, (255, 255, 255))
        window.blit(curr_level_text, (20, 20))

        keys = pygame.key.get_pressed()  # Update pressed keys inside the loop

        if not level_won:
            # Player Movement
            if keys[pygame.K_a] and not player.rect.colliderect(map_instance.border_left_rect):
                player.move(-player.speed, 0)
            if keys[pygame.K_d] and not player.rect.colliderect(map_instance.border_right_rect):
                player.move(player.speed, 0)
            if keys[pygame.K_w] and not player.rect.colliderect(map_instance.border_top_rect):
                player.move(0, -player.speed)
            if keys[pygame.K_s] and not player.rect.colliderect(map_instance.border_down_rect):
                player.move(0, player.speed)

            # Check if collided with enemy
            if player.rect.colliderect(enemy):
                player.rect.x, player.rect.y = 50, 720/2-50

            # Check if collided with coin
            if player.rect.colliderect(coin):
                pygame.mixer.music.play(loops=0)
                player.speed = 0
                level_won = True

        if level_won:
            # Display "Level Won!" message and prompt to continue
            level_won_text = win_font.render("Level Won!", True, (255, 255, 255))
            continue_text = font.render("Press Space to Continue", True, (255, 255, 255))
            window.blit(level_won_text, (240, 720/2-100))
            window.blit(continue_text, (460, 600))

            # Check for spacebar press to continue
            if keys[pygame.K_SPACE]:
                level_won = False
                level_loaded = False
                window.fill((0, 0, 0))  # Clear the screen
                pygame.display.update()  # Update the display

        # Update the display
        map_instance.draw_border(window)
        player.draw(window)
        enemy.draw(window)
        coin.draw(window)
        pygame.display.update()
        window.fill((0, 0, 0))  # Clear the screen
        clock.tick(FPS)


def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            # Quit if user closes
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for key press events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return  # Exit the main_menu() function to start the game

        main_menu_text = main_menu_font.render("Press Space to Start", True, (255, 255, 255))
        window.blit(main_menu_text, (290, 160))

        pygame.display.update()
        window.fill((0, 0, 0))  # Background
        clock.tick(FPS)


main_menu()
game()


pygame.quit()

