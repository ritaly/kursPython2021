
#y_indexes = [i for i, x in enumerate(name_base) if x == 'y']

arr = [1, 2, 4, 2, 1, 5, 7, 9, 12]
# chcemy mieć indeksy liczb parzystych
# even_indexes = [index for index, value in enumerate(arr) if value % 2 == 0]
# print(even_indexes)
# print(list(enumerate(arr)))

# even_indexes = []
# for index, value in enumerate(arr):
#     if value % 2 == 0:
#         even_indexes.append(index)
#
# print(even_indexes)

print('------------')
even_indexes = []
for index in range(len(arr)):
    if arr[index] % 2 == 0:
        even_indexes.append(index)
print(even_indexes)