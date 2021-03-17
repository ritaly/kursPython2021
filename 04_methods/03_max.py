# Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def maximum_of_2(arg_1,  arg_2):
    return arg_1 if arg_1 > arg_2 else arg_2


def maximum_of(a, b, c):
    return maximum_of_2(c, maximum_of_2(a, b))

print(maximum_of(17, 1, 9))