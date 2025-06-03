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
                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_p or event.key == pygame.K_ESCAPE):
                    if self.game_started:  # Only allow pause if game started
                        self.pause = True

                if self.pause:
                    # Handle pause menu events
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
                else:
                    self.current_screen.handle_event(event)

            if self.pause:
                self.screen.fill((30, 30, 30))
                self.pause_button_rects = draw_pause_menu(self.screen, self.font)
            else:
                self.current_screen.update()
                self.current_screen.render()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    GameApp().run()