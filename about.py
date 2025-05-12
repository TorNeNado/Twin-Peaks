import pygame
import sys
from settings import *

def show_about_page(screen, font, clock, about_image):
    about_running = True
    while about_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Кнопка "Назад"
                back_button_rect = pygame.Rect(50, 500, 200, 50)
                if back_button_rect.collidepoint(mouse_pos):
                    about_running = False

        # Отрисовка изображения "Автор"
        screen.blit(about_image, (0, 0))

        # Отрисовка кнопки "Назад"
        back_button_rect = pygame.Rect(50, 500, 200, 50)
        pygame.draw.rect(screen, GRAY, back_button_rect)  # Рамка кнопки
        pygame.draw.rect(screen, BLACK, back_button_rect.inflate(-4, -4))  # Заливка кнопки
        back_text_surface = font.render("Назад", True, WHITE)
        back_text_rect = back_text_surface.get_rect(center=back_button_rect.center)
        screen.blit(back_text_surface, back_text_rect)

        # Обновление экрана
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        clock.tick(60)