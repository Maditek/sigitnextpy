from Animal import Animal


class Skunk(Animal):
    def __init__(self, name, hunger, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def get_type(self):
        return "Skunk"

    def talk(self):
        return "tsssss"

    def stink(self):
        print("Dear lord!")

    def special_method(self):
        self.stink()
