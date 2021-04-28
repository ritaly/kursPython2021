# Utwórz klasę Customer, która ma pola imię nazwisko, oraz email klienta
# Dodaj metodę rejestracji, która zwraca datę register_at o tyle dni w przyszłość,
# ile customer ma liter w imieniu i nazwisku

import datetime as t

class Customer:
    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def register(self):
        days = len(self.firstname) + len(self.lastname)
        today = t.datetime.today()
        register_at = today + t.timedelta(days)
        return register_at.strftime('%Y-%m-%d')


if __name__ == '__main__':
    user = Customer('Jon', 'Snow', 'jon@got.com')
    print(user.register())