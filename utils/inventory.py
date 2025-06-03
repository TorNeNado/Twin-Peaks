class Inventory:
    def __init__(self):
        self.items = []
        self.photos = []
        self.images = {}

    def add_item(self, item: str):
        if item not in self.items:
            self.items.append(item)

    def has_item(self, item: str) -> bool:
        return item in self.items

    def add_photo(self, photo: str):
        if photo not in self.photos:
            self.photos.append(photo)

    def has_photo(self, photo: str) -> bool:
        return photo in self.photos

    def get_image(self, item_name):
        if item_name not in self.images:
            path = os.path.join("assets", "items", f"{item_name.lower()}.png")
            try:
                image = pygame.image.load(path).convert_alpha()
                image = pygame.transform.scale(image, (64, 64))
                self.images[item_name] = image
            except Exception as e:
                print(f"[!] Ошибка загрузки картинки '{item_name}': {e}")
                self.images[item_name] = None
        return self.images[item_name]
