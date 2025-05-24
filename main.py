import pygame
import sys
from settings import *
from menu import *
from about import show_about_page

# Инициализация Pygame
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("assets/sound/mainSound.mp3")  # Percorso del file audio
pygame.mixer.music.set_volume(0.5)  # Imposta il volume (0.0 - 1.0)
pygame.mixer.music.play(-1)  # Riproduci in loop (-1 per infinito)


pygame.mixer.music.load("assets/sound/motel-music.mp3") 
pygame.mixer.music.play(-1)
pygame.mixer.init()
pygame.mixer.music.load("assets/sound/Menu_Sound.mp3")  # Percorso del file audio
pygame.mixer.music.set_volume(0.5)  # Imposta il volume (0.0 - 1.0)
pygame.mixer.music.play(-1)  # Riproduci in loop (-1 per infinito)
clock = pygame.time.Clock()
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

show_map = False

# Create a clock object to control the frame rate
clock = pygame.time.Clock()
settings_open = False
music_volume = 0.5  # Start volume

# Главный цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not show_map and not settings_open:
            mouse_pos = pygame.mouse.get_pos()
            for option, button_rect in button_rects:
                if button_rect.collidepoint(mouse_pos):
                    if option == "Начать игру":
                        print("Игра началась!")
                    elif option == "Загрузить игру":
                        print("Загружена сохраненная игра.")
                    elif option == "Настройки":
                        settings_open = True
                    elif option == "Автор":
                        show_about_page(screen, font, clock, about_image)
                    elif option == "Выход":
                        running = False

        # Настройки: обработка кнопок громкости
        elif event.type == pygame.MOUSEBUTTONDOWN and settings_open:
            mouse_pos = pygame.mouse.get_pos()
            louder_rect = pygame.Rect(300, 250, 200, 50)
            quieter_rect = pygame.Rect(300, 320, 200, 50)
            back_rect = pygame.Rect(300, 390, 200, 50)
            if louder_rect.collidepoint(mouse_pos):
                music_volume = min(1.0, music_volume + 0.1)
                pygame.mixer.music.set_volume(music_volume)
            elif quieter_rect.collidepoint(mouse_pos):
                music_volume = max(0.0, music_volume - 0.1)
                pygame.mixer.music.set_volume(music_volume)
            elif back_rect.collidepoint(mouse_pos):
                settings_open = False

    # Отрисовка фона или карты или настроек
    if show_map:
        screen.blit(map_image, (0, 0))
        # ...назад в меню button code...
        back_button_rect = pygame.Rect(50, 500, 200, 50)
        pygame.draw.rect(screen, GRAY, back_button_rect)
        pygame.draw.rect(screen, BLACK, back_button_rect.inflate(-4, -4))
        back_text_surface = font.render("Назад в меню", True, WHITE)
        back_text_rect = back_text_surface.get_rect(center=back_button_rect.center)
        screen.blit(back_text_surface, back_text_rect)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if back_button_rect.collidepoint(mouse_pos):
                fade_transition(screen, map_image, background_image, duration=800)
                show_map = False
                pygame.mixer.music.load("assets/sound/Menu_Sound.mp3")
                pygame.mixer.music.set_volume(music_volume)
                pygame.mixer.music.play(-1)
    elif settings_open:
        screen.fill(BLACK)
        title = font.render("Настройки", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 150))

        louder_rect = pygame.Rect(300, 250, 200, 50)
        quieter_rect = pygame.Rect(300, 320, 200, 50)
        back_rect = pygame.Rect(300, 390, 200, 50)

        pygame.draw.rect(screen, GRAY, louder_rect)
        pygame.draw.rect(screen, GRAY, quieter_rect)
        pygame.draw.rect(screen, GRAY, back_rect)

        louder_text = font.render("Громче", True, WHITE)
        quieter_text = font.render("Тише", True, WHITE)
        back_text = font.render("Назад", True, WHITE)

        screen.blit(louder_text, louder_rect.move(60, 10))
        screen.blit(quieter_text, quieter_rect.move(60, 10))
        screen.blit(back_text, back_rect.move(60, 10))

        # Show current volume
        vol_text = font.render(f"Громкость: {int(music_volume*100)}%", True, WHITE)
        screen.blit(vol_text, (SCREEN_WIDTH // 2 - vol_text.get_width() // 2, 200))
    else:
        screen.blit(background_image, (0, 0))
        draw_menu(screen, font)

    pygame.display.flip()
    clock.tick(60)

# Завершение Pygame
pygame.quit()
sys.exit()