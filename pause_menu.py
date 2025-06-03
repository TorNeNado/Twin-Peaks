import pygame
from settings import *

PAUSE_OPTIONS = [
    "Продолжить",
    "Сохранить игру",
    "Вернуться в главное меню",
    "Выход"
]

def draw_pause_menu(screen, font):
    menu_x = 250
    menu_y = 180
    menu_width = 300
    menu_height = 50
    padding = 20

    pause_button_rects = []

    for i, option in enumerate(PAUSE_OPTIONS):
        button_rect = pygame.Rect(menu_x, menu_y + i * (menu_height + padding), menu_width, menu_height)
        pause_button_rects.append((option, button_rect))

        pygame.draw.rect(screen, GRAY, button_rect)
        pygame.draw.rect(screen, BLACK, button_rect.inflate(-4, -4))
        text_surface = font.render(option, True, WHITE)
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

    return pause_button_rects