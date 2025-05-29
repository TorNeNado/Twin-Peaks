class Inventory:
    def __init__(self):
        self.items = []  # список улик
        self.photos = []  # список фотографий

    def add_item(self, item: str):
        if item not in self.items:
            self.items.append(item)

    def add_photo(self, photo: str):
        if photo not in self.photos:
            self.photos.append(photo)

    def has_item(self, item: str) -> bool:
        return item in self.items

    def has_photo(self, photo: str) -> bool:
        return photo in self.photos
