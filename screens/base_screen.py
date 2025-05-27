import pygame
import os
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class BaseScreen:
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.font = app.font
        self.dialog_text = ""
        self.dialog_shown = ""
        self.dialog_index = 0
        self.dialog_last_update = pygame.time.get_ticks()
        self.dialog_speed = 30  # миллисекунд на символ

    def set_dialog(self, text: str):
        self.dialog_text = text
        self.dialog_shown = ""
        self.dialog_index = 0
        self.dialog_last_update = pygame.time.get_ticks()

    def update_dialog(self):
        now = pygame.time.get_ticks()
        if self.dialog_index < len(self.dialog_text):
            if now - self.dialog_last_update >= self.dialog_speed:
                self.dialog_index += 1
                self.dialog_shown = self.dialog_text[:self.dialog_index]
                self.dialog_last_update = now

    def render_dialog(self):
        dialog_box = pygame.Rect(30, SCREEN_HEIGHT - 100, SCREEN_WIDTH - 60, 70)
        pygame.draw.rect(self.screen, (0, 0, 0), dialog_box)
        pygame.draw.rect(self.screen, (255, 255, 255), dialog_box, 2)

        text_surface = self.font.render(self.dialog_shown, True, (255, 255, 255))
        self.screen.blit(text_surface, (dialog_box.x + 10, dialog_box.y + 20))
