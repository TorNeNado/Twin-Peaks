class BaseScreen:
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.font = app.font

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def render(self):
        pass
