from .animal import Animal


class Wolf(Animal):
    def __init__(self, name="Luna"):
        super().__init__(name, species="Wolf")

    def sound(self):
        return "Howl"

    def action(self):
        return "Emerges when the full moon is out."