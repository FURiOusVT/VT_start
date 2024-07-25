class Horse:
    def __init__(self, rider, speed, age):
        self.rider = rider
        self.speed = speed
        self.age = age

class Rider:
    def __init__(self, name):
        self.name = name

rider = Rider("Mathew")
horse = Horse(rider, 50, 12)
print(horse.rider.name)
        
