from Animal import Animal


class Unicorn(Animal):
    def get_type(self):
        return "Unicorn"

    def talk(self):
        return "Good day, darling"

    def sing(self):
        print("I’m not your toy...")

    def special_method(self):
        self.sing()