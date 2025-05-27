import pygame
import sys
from settings import *
from menu import *
from about import show_about_page

# Инициализация Pygame
pygame.init()
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

# Загрузка изображения для карты
map_image = pygame.image.load("assets/images/map.jpg")
map_image = pygame.transform.scale(map_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Шрифт для текста
font = pygame.font.Font(None, FONT_SIZE)

show_map = False

# Create a clock object to control the frame rate
clock = pygame.time.Clock()
settings_open = False
music_volume = 0.5  # Start volume

def draw_map_button(screen, rect: pygame.Rect, text: str, font: pygame.font.Font, hovered: bool):
    base_color = (200, 0, 0) if hovered else (100, 0, 0)
    outline_color = (255, 255, 255)
    text_color = (255, 255, 255)

    surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    surface.fill((*base_color, 150))  # Полупрозрачный фон
    screen.blit(surface, (rect.x, rect.y))
    
    pygame.draw.rect(screen, outline_color, rect, 2)

    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

regions = {
    "motel": pygame.Rect(123, 40, 230 - 123, 65 - 40),
    "kafe": pygame.Rect(89, 107, 194 - 89, 132 - 107),
    "les": pygame.Rect(348, 145, 453 - 348, 170 - 145),
    "utes": pygame.Rect(194, 201, 300 - 194, 225 - 201),
    "ozero": pygame.Rect(590, 313, 700 - 590, 339 - 313),
    "office_S": pygame.Rect(260, 465, 366 - 260, 488 - 465),
    "bar": pygame.Rect(461, 498, 567 - 461, 522 - 498),
}

# Главный цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if show_map:
                # Зоны карты
                for name, rect in regions.items():
                    if rect.collidepoint(mouse_pos):
                        print(f"Клик по области: {name}")
                        # Здесь может быть переход на сцену, воспроизведение звука и т.п.

                # Кнопка назад
                back_button_rect = pygame.Rect(50, 500, 200, 50)
                if back_button_rect.collidepoint(mouse_pos):
                    fade_transition(screen, map_image, background_image, duration=800)
                    show_map = False
                    pygame.mixer.music.load("assets/sound/Menu_Sound.mp3")
                    pygame.mixer.music.set_volume(music_volume)
                    pygame.mixer.music.play(-1)

            elif settings_open:
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

            elif not show_map and not settings_open:
                for option, button_rect in button_rects:
                    if button_rect.collidepoint(mouse_pos):
                        if option == "Начать игру":
                            print("Игра началась!")
                            try:
                                pygame.mixer.music.load("assets/sound/motel-music.mp3")
                                pygame.mixer.music.set_volume(music_volume)
                                pygame.mixer.music.play(-1)
                            except Exception as e:
                                print("Music error:", e)
                            fade_transition(screen, background_image, map_image, duration=800)
                            show_map = True
                        elif option == "Загрузить игру":
                            print("Загружена сохраненная игра.")
                        elif option == "Настройки":
                            settings_open = True
                        elif option == "Автор":
                            show_about_page(screen, font, clock, about_image)
                        elif option == "Выход":
                            running = False



    # Отрисовка фона или карты или настроек
    if show_map:
        screen.blit(map_image, (0, 0))

        # Рисуем кликабельные зоны
        for name, rect in regions.items():
            pygame.draw.rect(screen, (255, 0, 0), rect, 2)
            text = font.render(name, True, (255, 255, 255))
            screen.blit(text, (rect.x + 5, rect.y + 5))

        # Кнопка "Назад в меню"
        back_button_rect = pygame.Rect(50, 500, 200, 50)
        pygame.draw.rect(screen, GRAY, back_button_rect)
        pygame.draw.rect(screen, BLACK, back_button_rect.inflate(-4, -4))
        back_text_surface = font.render("Назад в меню", True, WHITE)
        back_text_rect = back_text_surface.get_rect(center=back_button_rect.center)
        screen.blit(back_text_surface, back_text_rect)

        # Обработка кликов по зонам и кнопке назад
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Зоны карты
            for name, rect in regions.items():
                if rect.collidepoint(mouse_pos):
                    print(f"Клик по области: {name}")
                    # TODO: переход в сцену / звук / действия

            # Кнопка назад
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