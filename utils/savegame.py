import json

def save_game(inventory, filename="savegame.json"):
    """
    Save the inventory state to a JSON file.
    """
    data = {
        "items": inventory.items,
        "photos": inventory.photos
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
