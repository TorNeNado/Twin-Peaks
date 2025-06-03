import pygame
from settings import *
from screens.menu_screen import MenuScreen
from screens.map_screen import MapScreen
from screens.settings_screen import SettingsScreen
from screens.about_screen import AboutScreen
from utils.inventory import Inventory
from pause_menu import draw_pause_menu  # <-- Make sure you have this file

class GameApp:
    def __init__(self):
        pygame.init()

        self.game_started = False

        self.inventory = Inventory()

        self.inventory_visible = False

        pygame.mixer.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Twin Peaks")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.music_volume = 0.5

        self.running = True
        self.current_screen = MenuScreen(self)
        self.pause = False
        pygame.mixer.music.load("assets/sound/Menu_Sound.mp3")
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1)

    def set_screen(self, screen_class):
        self.current_screen = screen_class(self)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        self.inventory_visible = not self.inventory_visible
                    elif event.key == pygame.K_ESCAPE:
                        if self.inventory_visible:
                            self.inventory_visible = False
                        elif self.game_started:
                            self.pause = not self.pause
                    elif event.key == pygame.K_p:
                        if self.game_started:
                            self.pause = not self.pause

                if self.pause:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        for option, rect in self.pause_button_rects:
                            if rect.collidepoint(mouse_pos):
                                if option == "Продолжить":
                                    self.pause = False
                                elif option == "Сохранить игру":
                                    from utils.savegame import save_game
                                    save_game(self.inventory)
                                elif option == "Вернуться в главное меню":
                                    self.set_screen(MenuScreen)
                                    self.pause = False
                                elif option == "Выход":
                                    self.running = False
                elif not self.inventory_visible:
                    self.current_screen.handle_event(event)

            # --- Обновление и рендер ---
            if self.pause:
                self.screen.fill((30, 30, 30))
                self.pause_button_rects = draw_pause_menu(self.screen, self.font)
            else:
                self.current_screen.update()
                self.current_screen.render()
                if self.inventory_visible:
                    self.draw_inventory_overlay()  # <-- Инвентарь поверх сцены

            pygame.display.flip()
            self.clock.tick(60)


            


    def toggle_inventory(self):
        self.inventory_visible = not self.inventory_visible

    def draw_inventory_overlay(self):
        overlay_width = 300
        overlay_height = 400
        overlay = pygame.Surface((overlay_width, overlay_height))
        overlay.fill((20, 20, 20))  # Тёмный фон
        overlay.set_alpha(220)      # Полупрозрачность
        self.screen.blit(overlay, (SCREEN_WIDTH - overlay_width - 20, 20))

        title = self.font.render("Инвентарь", True, (240, 240, 240))  # Светлый заголовок
        self.screen.blit(title, (SCREEN_WIDTH - overlay_width, 30))

        y = 70
        for item in self.inventory.items:
            item_text = self.font.render(f"- {item}", True, (220, 220, 220))  # Светлый текст
            self.screen.blit(item_text, (SCREEN_WIDTH - overlay_width, y))
            y += 30

        for photo in self.inventory.photos:
            photo_text = self.font.render(f"[Фото] {photo}", True, (180, 200, 255))  # Оттенок синего
            self.screen.blit(photo_text, (SCREEN_WIDTH - overlay_width, y))
            y += 30


if __name__ == "__main__":
    GameApp().run()