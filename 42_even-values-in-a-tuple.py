tup = (1,2,3,4,5,6,7,8,9,10)
list_even = list()
for i in tup:
    if i%2 == 0:
        list_even.append(i)

tuple_even = tuple(list_even)

print tuple_even
