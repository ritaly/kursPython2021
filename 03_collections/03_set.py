# Utwórz 2 krotki.
# Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
# oraz nieparzystych elementów z drugiej.
# Przekształć powstałą listę w set.

tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = (0, 1, 2, 'c', 4, 5)

list1 = list(tuple1[::2])
print(list1)
list2 = list(tuple2[1::2])
print(list2)

set_all = set(list1 + list2)
print(set_all)
