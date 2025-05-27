import pygame
from screens.base_screen import BaseScreen
from utils.transitions import fade_transition
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class MapScreen(BaseScreen):
    def __init__(self, app):
        super().__init__(app)
        self.map_image = pygame.image.load("assets/images/map.jpg")
        self.map_image = pygame.transform.scale(self.map_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.regions = {
            "motel": pygame.Rect(123, 40, 107, 25),
            "kafe": pygame.Rect(89, 107, 105, 25),
            "les": pygame.Rect(348, 145, 105, 25),
            "utes": pygame.Rect(194, 201, 106, 24),
            "ozero": pygame.Rect(590, 313, 110, 26),
            "office_S": pygame.Rect(260, 465, 106, 23),
            "bar": pygame.Rect(461, 498, 106, 24),
        }
        self.back_button_rect = pygame.Rect(50, 500, 200, 50)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for name, rect in self.regions.items():
                if rect.collidepoint(mouse_pos):
                    print(f"Клик по области: {name}")
            if self.back_button_rect.collidepoint(mouse_pos):
                background = pygame.image.load("assets/images/startWindow.jpg")
                background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
                fade_transition(self.screen, self.map_image, background, duration=800)

                # ЛОКАЛЬНЫЙ ИМПОРТ — разрывает цикл
                from screens.menu_screen import MenuScreen
                self.app.set_screen(MenuScreen)

                pygame.mixer.music.load("assets/sound/Menu_Sound.mp3")
                pygame.mixer.music.set_volume(self.app.music_volume)
                pygame.mixer.music.play(-1)

    def render(self):
        self.screen.blit(self.map_image, (0, 0))
        for rect in self.regions.values():
            pygame.draw.rect(self.screen, (255, 0, 0), rect, 2)
        pygame.draw.rect(self.screen, (200, 200, 200), self.back_button_rect)
        text = self.font.render("Назад в меню", True, (0, 0, 0))
        text_rect = text.get_rect(center=self.back_button_rect.center)
        self.screen.blit(text, text_rect)


