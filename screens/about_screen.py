import pygame
from screens.base_screen import BaseScreen

class AboutScreen(BaseScreen):
    def __init__(self, app):
        super().__init__(app)
        self.image = pygame.image.load("assets/images/about.png")
        self.image = pygame.transform.scale(self.image, (self.screen.get_width(), self.screen.get_height()))
        self.back_button_rect = pygame.Rect(50, 500, 200, 50)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button_rect.collidepoint(pygame.mouse.get_pos()):
                from screens.menu_screen import MenuScreen
                self.app.set_screen(MenuScreen)


    def render(self):
        self.screen.blit(self.image, (0, 0))

        pygame.draw.rect(self.screen, (200, 200, 200), self.back_button_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.back_button_rect.inflate(-4, -4))

        text_surface = self.font.render("Назад в меню", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.back_button_rect.center)
        self.screen.blit(text_surface, text_rect)

    def update(self):
        self.update_dialog()
