from Animal import Animal


class Dragon(Animal):
    def __init__(self, name, hunger, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    def get_type(self):
        return "Dragon"

    def talk(self):
        return "Raaaawr"

    def breath_fire(self):
        print("$@#$#@$")

    def special_method(self):
        self.breath_fire()