import pygame
from settings import *
from screens.menu_screen import MenuScreen
from screens.map_screen import MapScreen
from screens.settings_screen import SettingsScreen
from screens.about_screen import AboutScreen

class GameApp:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Twin Peaks")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.music_volume = 0.5

        self.running = True
        self.current_screen = MenuScreen(self)

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
                self.current_screen.handle_event(event)

            self.current_screen.update()
            self.current_screen.render()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    GameApp().run()
