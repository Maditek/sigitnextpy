from Animal import Animal


class Cat(Animal):
    def get_type(self):
        return "Cat"

    def talk(self):
        return "meow"

    def chase_laser(self):
        print("Meeeeow")

    def special_method(self):
        self.chase_laser()