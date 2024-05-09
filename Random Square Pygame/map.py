import pygame


class Border:

    def __init__(self):
        # Define border rectangles
        self.border_left_rect = pygame.Rect(0, 0, 10, 720)
        self.border_right_rect = pygame.Rect(1270, 0, 10, 720)
        self.border_top_rect = pygame.Rect(0, 0, 1280, 10)
        self.border_down_rect = pygame.Rect(0, 710, 1280, 10)

    def draw_border(self, screen):
        # Draw left border
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, 10, 720))
        # Draw down border
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 710, 1280, 10))
        # Draw right border
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(1270, 0, 10, 720))
        # Draw top border
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, 1280, 10))


class Enemy:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Coin:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

