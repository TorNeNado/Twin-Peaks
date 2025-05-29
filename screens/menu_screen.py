import pygame
from screens.base_screen import BaseScreen
from screens.settings_screen import SettingsScreen
from screens.about_screen import AboutScreen
from screens.map_screen import MapScreen
from utils.transitions import fade_transition
from menu import draw_menu
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

import os

class MenuScreen(BaseScreen):
    def __init__(self, app):
        super().__init__(app)
        bg_path = os.path.join("assets", "images", "startWindow.jpg")
        self.background = pygame.image.load(bg_path)
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for option, rect in self.draw_menu():
                if rect.collidepoint(mouse_pos):
                    if option == "Начать игру":
                        pygame.mixer.music.load("assets/sound/motel-music.mp3")
                        pygame.mixer.music.set_volume(self.app.music_volume)
                        pygame.mixer.music.play(-1)
                        fade_transition(self.screen)
                        from screens.map_screen import MapScreen
                        self.app.set_screen(MapScreen)
                    elif option == "Настройки":
                        from screens.settings_screen import SettingsScreen
                        self.app.set_screen(SettingsScreen)
                    elif option == "Автор":
                        from screens.about_screen import AboutScreen
                        self.app.set_screen(AboutScreen)
                    elif option == "Выход":
                        self.app.running = False

    def draw_menu(self):
        from menu import draw_menu
        return draw_menu(self.screen, self.font)

    def update(self):
        self.update_dialog()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.draw_menu()
        
