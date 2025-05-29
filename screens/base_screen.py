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
        self.choices = []
        self.choice_buttons = []    

    def set_dialog(self, text: str, choices: list[tuple[str, callable]] = None):
        self.dialog_text = text
        self.dialog_shown = ""
        self.dialog_index = 0
        self.dialog_last_update = pygame.time.get_ticks()
        self.choices = choices if choices else []


    def update_dialog(self):
        now = pygame.time.get_ticks()
        if self.dialog_index < len(self.dialog_text):
            if now - self.dialog_last_update >= self.dialog_speed:
                self.dialog_index += 1
                self.dialog_shown = self.dialog_text[:self.dialog_index]
                self.dialog_last_update = now

    def render_dialog(self):
        font = pygame.font.Font(None, 14)
        box_width = 550
        box_height = 150
        margin = 20

        dialog_box = pygame.Rect(
            250,
            SCREEN_HEIGHT - box_height - margin,
            box_width,
            box_height
        )

        overlay = pygame.Surface((dialog_box.width, dialog_box.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (dialog_box.x, dialog_box.y))

        pygame.draw.rect(self.screen, (255, 255, 255), dialog_box, 2)

        text_surface = font.render(self.dialog_shown, True, (255, 255, 255))
        self.screen.blit(text_surface, (dialog_box.x + 10, dialog_box.y + 10))

        # Рисуем кнопки выбора
        self.choice_buttons = []
        button_width = 160
        button_height = 30
        spacing = 20
        total_width = len(self.choices) * (button_width + spacing) - spacing
        start_x = dialog_box.centerx - total_width // 2
        y = dialog_box.bottom - button_height - 10

        for i, (text, _) in enumerate(self.choices):
            rect = pygame.Rect(start_x + i * (button_width + spacing), y, button_width, button_height)
            pygame.draw.rect(self.screen, (200, 200, 200), rect)
            pygame.draw.rect(self.screen, (255, 255, 255), rect, 2)
            label = font.render(text, True, (0, 0, 0))
            self.screen.blit(label, label.get_rect(center=rect.center))
            self.choice_buttons.append(rect)

    def handle_dialog_click(self, pos):
        for i, rect in enumerate(self.choice_buttons):
            if rect.collidepoint(pos):
                _, callback = self.choices[i]
                callback()
                break

    def some_screen_enter(self):
        self.set_dialog(
            "Что вы хотите сделать?",
            [
                ("Осмотреть комнату", self.inspect_room),
                ("Выйти", self.leave_room)
            ]
        )



