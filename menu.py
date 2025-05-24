import pygame
from settings import *

# Create a list to store button rectangles
button_rects = []

def draw_menu(screen, font):
    menu_x = 50  # Позиция меню слева
    menu_y = 50  # Позиция меню сверху
    menu_width = 200
    menu_height = 50
    padding = 10

    button_rects.clear()  # Clear the list of button rectangles

    for i, option in enumerate(MENU_OPTIONS):
        # Define the button rectangle
        button_rect = pygame.Rect(menu_x, menu_y + i * (menu_height + padding), menu_width, menu_height)
        button_rects.append((option, button_rect))  # Store the option and its rectangle

        # Draw the button
        pygame.draw.rect(screen, GRAY, button_rect)  # Рамка кнопки
        pygame.draw.rect(screen, BLACK, button_rect.inflate(-4, -4))  # Заливка кнопки

        # Render the text
        text_surface = font.render(option, True, WHITE)
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

    return button_rects

def fade_transition(screen, from_surface, to_surface, duration=1000):
    """Fade from one surface to another over 'duration' milliseconds."""
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    alpha_surface = to_surface.copy()
    while True:
        now = pygame.time.get_ticks()
        elapsed = now - start_time
        alpha = min(255, int(255 * elapsed / duration))
        screen.blit(from_surface, (0, 0))
        alpha_surface.set_alpha(alpha)
        screen.blit(alpha_surface, (0, 0))
        pygame.display.flip()
        if alpha >= 255:
            break
        clock.tick(60)