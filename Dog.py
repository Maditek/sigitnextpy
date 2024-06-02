from Animal import Animal


class Dog(Animal):

    def get_type(self):
        return "Dog"

    def talk(self):
        return "woof woof"

    def fetch_stick(self):
        print("There you go, sir!")

    def special_method(self):
        self.fetch_stick()