import pygame
import os
from screens.base_screen import BaseScreen
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class MotelRoomScreen(BaseScreen):
    def __init__(self, app):
        super().__init__(app)
        self.room_image = pygame.image.load("assets/images/motel/room.png")
        self.room_image = pygame.transform.scale(self.room_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.table_rect = pygame.Rect(50, 400, 200, 50)
        self.board_rect = pygame.Rect(550, 100, 200, 50)
        self.back_rect = pygame.Rect(50, 500, 200, 50)
        self.set_dialog("Вы вошли в номер мотеля. Что-то здесь не так...")

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.table_rect.collidepoint(mouse_pos):
                from screens.motel_screen import MotelTableScreen
                self.app.set_screen(MotelTableScreen)
            elif self.board_rect.collidepoint(mouse_pos):
                from screens.motel_screen import MotelBoardScreen
                self.app.set_screen(MotelBoardScreen)
            elif self.back_rect.collidepoint(mouse_pos):
                from screens.map_screen import MapScreen
                self.app.set_screen(MapScreen)

    def update(self):
        self.update_dialog()

    def render(self):
        self.screen.blit(self.room_image, (0, 0))
        pygame.draw.rect(self.screen, (180, 180, 180), self.table_rect)
        self.screen.blit(self.font.render("Стол", True, (0, 0, 0)), self.table_rect.move(60, 10))
        pygame.draw.rect(self.screen, (180, 180, 180), self.board_rect)
        self.screen.blit(self.font.render("Доска", True, (0, 0, 0)), self.board_rect.move(60, 10))
        pygame.draw.rect(self.screen, (180, 180, 180), self.back_rect)
        self.screen.blit(self.font.render("Назад", True, (0, 0, 0)), self.back_rect.move(60, 10))
        self.render_dialog()


class MotelTableScreen(BaseScreen):
    def __init__(self, app):
        super().__init__(app)
        self.image = pygame.image.load("assets/images/motel/table.png")
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.back_rect = pygame.Rect(50, 500, 200, 50)
        self.set_dialog("На столе пока ничего нет... но это может измениться.")

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_rect.collidepoint(pygame.mouse.get_pos()):
                from screens.motel_screen import MotelRoomScreen
                self.app.set_screen(MotelRoomScreen)

    def update(self):
        self.update_dialog()

    def render(self):
        self.screen.blit(self.image, (0, 0))
        pygame.draw.rect(self.screen, (180, 180, 180), self.back_rect)
        self.screen.blit(self.font.render("Назад", True, (0, 0, 0)), self.back_rect.move(60, 10))
        self.render_dialog()


class MotelBoardScreen(BaseScreen):
    def __init__(self, app):
        super().__init__(app)
        self.image = pygame.image.load("assets/images/motel/board.png")
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.back_rect = pygame.Rect(50, 500, 200, 50)
        self.set_dialog("Доска пуста... но здесь скоро появятся зацепки.")

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_rect.collidepoint(pygame.mouse.get_pos()):
                from screens.motel_screen import MotelRoomScreen
                self.app.set_screen(MotelRoomScreen)

    def update(self):
        self.update_dialog()

    def render(self):
        self.screen.blit(self.image, (0, 0))
        pygame.draw.rect(self.screen, (180, 180, 180), self.back_rect)
        self.screen.blit(self.font.render("Назад", True, (0, 0, 0)), self.back_rect.move(60, 10))
        self.render_dialog()
