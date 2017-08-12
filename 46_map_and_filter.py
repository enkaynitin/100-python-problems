list = [1,2,3,4,5,6,7,8,9,10]

square_list = map(lambda x: x**2, filter(lambda x: x%2 == 0, list)) # filter even and map squares and store in square_list


print square_list
