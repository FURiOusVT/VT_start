class Hexagon:
    def __init__(self, s):
        self.side = s

    def hex_p(self):
        return self.side*6

Hexagon = Hexagon(6)
print(Hexagon.hex_p())
