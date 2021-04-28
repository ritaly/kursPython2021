class Account:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__account_number = '12 4530 0000 1001 2345 3213'

    def show_number(self):
        print("Current account number: {}".format(self.__account_number))

    def set_new_account_number(self, new_number):
        self.__account_number = new_number


if __name__ == '__main__':
    bank_account = Account('Anna', 'Nowak')
    bank_account.show_number()

    print(bank_account.last_name)
    bank_account.set_new_account_number('34 5666 2222 1111 4444')
    bank_account.show_number()
