def get_books():
    counter = int(input('How many books you want to add to the collections? '))

    books_collection = []
    for book in range(counter):
        title = input('Book title: ')
        rate = int(input(f'{title} - rate [0-10]: '))
        books_collection.append([title, rate])

    return books_collection

def show_rate(books_list):
    nr = int(input('Which rate you want to see? (give me a number: '))
    index = nr - 1

    if nr > len(books_list) or nr < 0:
        print('No such book in collection')
    else:
        print(f'Book -> {books_list[index][0]} is rated -> { books_list[index][1] } / 10 ')


#---- main part ----
print('Welcome to library! ----')
books = get_books()
print('Added!')
print('--------------')
show_rate(books)