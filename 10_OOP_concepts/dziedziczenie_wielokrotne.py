class Ojciec:
    def __init__(self):
        print("I'm your father!")

    def oblicz_podatki(self):
        print('obliczone podatki')

class Matka:
    def __init__(self):
        print("Hello I'm your mom")

    def ucz_programowania(self):
        print('Ucz sie Pythona!')

class Dziecko(Ojciec, Matka):
    pass


baby = Dziecko()
baby.oblicz_podatki()
baby.ucz_programowania()