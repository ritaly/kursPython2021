# numbers = input('Podaj liczby po przecinku: ')
# numbers = numbers.split(',')
# print(numbers)
#
# print('Czy pierwsza i ostania liczba są takie same:', numbers[0] == numbers[-1])

counter = int(input("Ile liczb chcesz podać?"))

list_of_num = []
for i in range(counter):
    num = float(input("Podaj liczbe: "))
    list_of_num.append(num)

if list_of_num[0] == list_of_num[-1]:
    print('pierwsza i ostatnia liczba taka sama')
else:
    print('nie są takie same')