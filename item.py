class Item:
    def __init__(self, name: str, days_until_expiration: int, quality: int):
        self.name = name
        self.days_until_expiration = days_until_expiration
        self.quality = quality

    def __str__(self):
        return f"name: {self.name}, days_until_expiration: {self.days_until_expiration}, quality: {self.quality}"