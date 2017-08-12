def SquaresList():
    square_list = list()
    for i in range(1,21):
        square_list.append(i**2)
    square_tuple = tuple(square_list)
    print square_tuple

SquaresList()
