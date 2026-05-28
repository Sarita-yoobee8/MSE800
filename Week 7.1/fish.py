#parent class fish
class Fish:

    def __init__(self, category):
        self.category = category

    def get_category(self):
        return self.category

#child  class Goldfish
class Goldfish(Fish):

    def __init__(self):
        super().__init__("Goldfish")

#child  class Shark
class Shark(Fish):

    def __init__(self):
        super().__init__("Shark")

#child  class angelfish
class Angelfish(Fish):

    def __init__(self):
        super().__init__("Angelfish")

#child  class tuna 
class Tuna(Fish):

    def __init__(self):
        super().__init__("Tuna")

#child  class salmon
class Salmon(Fish):

    def __init__(self):
        super().__init__("Salmon")