items = [1, 2.3, 0, "lala", {"Marta": 12}, (1, "jojo"), 14, 22222.111, "gimmie", {}, False]

try:
    index = int(input("Give me index 0 - 9:  "))
    my_division = 1 / items[index]
    print("The result: ", my_division)
except (TypeError, ZeroDivisionError) as err:
    print("Error: ", err)
except (ValueError, IndexError) as err:
    print('Incorrect index ->', err)