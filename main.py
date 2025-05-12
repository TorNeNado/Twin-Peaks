import pygame
import sys
from settings import *
from menu import draw_menu, button_rects
from about import show_about_page

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Twin Peaks")

# Загрузка фонового изображения
background_image = pygame.image.load(BACKGROUND_IMAGE_PATH)
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Загрузка изображения для страницы "Автор"
about_image = pygame.image.load("assets/images/about.png")
about_image = pygame.transform.scale(about_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Шрифт для текста
font = pygame.font.Font(None, FONT_SIZE)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Главный цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Handle clicks directly
            mouse_pos = pygame.mouse.get_pos()
            for option, button_rect in button_rects:  # Use the separate button_rects list
                if button_rect.collidepoint(mouse_pos):  # Check if the click is inside the button
                    if option == "Начать игру":
                        print("Игра началась!")
                    elif option == "Загрузить игру":
                        print("Загружена сохраненная игра.")
                    elif option == "Настройки":
                        print("Открыть настройки.")
                    elif option == "Автор":
                        show_about_page(screen, font, clock, about_image)  # Показать страницу "Автор"
                    elif option == "Выход":
                        running = False

    # Отрисовка фона
    screen.blit(background_image, (0, 0))

    # Отрисовка меню
    draw_menu(screen, font)

    # Обновление экрана
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Завершение Pygame
pygame.quit()
sys.exit()