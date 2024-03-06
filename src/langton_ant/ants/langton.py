class LangtonAnt:    
    def __init__(
        self,
    ):
        self.x = 0
        self.y = 0
        self.dir = "u"

    def turn_clockwise(self):
        if self.dir == "u":
            self.dir = "r"
        elif self.dir == "r":
            self.dir = "d"
        elif self.dir == "d":
            self.dir = "l"
        elif self.dir == "l":
            self.dir = "u"
    
    def turn_counter_clockwise(self):
        if self.dir == "u":
            self.dir = "l"
        elif self.dir == "l":
            self.dir = "d"
        elif self.dir == "d":
            self.dir = "r"
        elif self.dir == "r":
            self.dir = "u"
        
    def move(self):
        if self.dir == "u":
            self.y += 1
        elif self.dir == "l":
            self.x -= 1
        elif self.dir == "d":
            self.y -= 1
        elif self.dir == "r":
            self.x += 1

    def translate(self, x_offset, y_offset):
        self.x = self.x + x_offset
        self.y = self.y + y_offset
