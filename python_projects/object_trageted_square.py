class Square():
    square_list = []

    def __init__(self, side):
        self.length = side
        self.square_list.append((self.length))
        print("{} на {} на {} на {}".replace('{}', str(self.length)))
        print(self.square_list)

        

Square1 = Square(29)



        
