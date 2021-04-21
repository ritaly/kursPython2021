# Utwórz klasę sklep.
# Sklep posiada różne produkty. W sklepie można pordukt zobaczyc, przymierzyc, kupic, zwrocic.

class Shop:
    store = [
        'dress',
        't-shirt',
        'trousers',
        'shoes',
        'skirt'
    ]

    def show(self, index):
        print(self.store[index])

    def try_product(self, item):
        print('product was tired')

    def buy(self, item):
        if item in self.store:
            for index, value in enumerate(self.store):
                if value == item:
                    product_to_buy = self.store.pop(index)
                    return product_to_buy
        else:
            return 'brak produktu'

    def return_product(self, item):
        self.store.append(item)



if __name__ == '__main__':
    my_shop = Shop()
    print(my_shop.store)

    my_shop.show(3)



