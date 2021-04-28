# otwieranie url do YT
# wyswietlanie ananasa za pomoca ascii

class Pen:
    def __init__(self):
        print('Pen!')


class Pinapple():
    def scream(self):
        print('Pinapple!!!!')


class PenPinapple(Pen, Pinapple):
    def __init__(self):
        print('~~~')
        super().__init__()
        super().scream()




if __name__ == '__main__':
    pppp = PenPinapple()
