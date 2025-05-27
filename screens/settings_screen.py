import pygame
from screens.base_screen import BaseScreen
from utils.transitions import fade_transition
from settings import SCREEN_WIDTH

class SettingsScreen(BaseScreen):
    def __init__(self, app):
        super().__init__(app)
        self.louder_rect = pygame.Rect(300, 250, 200, 50)
        self.quieter_rect = pygame.Rect(300, 320, 200, 50)
        self.back_rect = pygame.Rect(300, 390, 200, 50)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.louder_rect.collidepoint(mouse_pos):
                self.app.music_volume = min(1.0, self.app.music_volume + 0.1)
                pygame.mixer.music.set_volume(self.app.music_volume)
            elif self.quieter_rect.collidepoint(mouse_pos):
                self.app.music_volume = max(0.0, self.app.music_volume - 0.1)
                pygame.mixer.music.set_volume(self.app.music_volume)
            elif self.back_rect.collidepoint(mouse_pos):
                from screens.menu_screen import MenuScreen
                self.app.set_screen(MenuScreen)


    def render(self):
        self.screen.fill((0, 0, 0))
        title = self.font.render("Настройки", True, (255, 255, 255))
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 150))

        pygame.draw.rect(self.screen, (150, 150, 150), self.louder_rect)
        pygame.draw.rect(self.screen, (150, 150, 150), self.quieter_rect)
        pygame.draw.rect(self.screen, (150, 150, 150), self.back_rect)

        louder_text = self.font.render("Громче", True, (255, 255, 255))
        quieter_text = self.font.render("Тише", True, (255, 255, 255))
        back_text = self.font.render("Назад", True, (255, 255, 255))

        self.screen.blit(louder_text, self.louder_rect.move(60, 10))
        self.screen.blit(quieter_text, self.quieter_rect.move(60, 10))
        self.screen.blit(back_text, self.back_rect.move(60, 10))

        volume_text = self.font.render(f"Громкость: {int(self.app.music_volume * 100)}%", True, (255, 255, 255))
        self.screen.blit(volume_text, (SCREEN_WIDTH // 2 - volume_text.get_width() // 2, 200))
