class Pen:
    def __init__(self):
        self.__name = "Pen"

    def get_pen(self):
        return self.__name

class Pinapple:
    def __init__(self):
        self.__name = "Pinappple"

    def get_pinapple(self):
        return self.__name

class PenPinapple(Pen, Pinapple):
    pen_name = ""
    pinapple_name = ""

    def get_name(self):
        self.pen_name = Pen().get_pen()
        self.pinapple_name = Pinapple().get_pinapple()

    def print_name(self):
        print(self.pen_name + self.pinapple_name)


if __name__ == '__main__':
    c1 = PenPinapple()
    print(c1.pen_name)
    c1.get_name()
    c1.print_name()
