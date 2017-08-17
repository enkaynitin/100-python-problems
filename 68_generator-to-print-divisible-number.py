def div_num_gen(n):
    for i in range(n+1):
        if i%5 == 0 and i%7 == 0 :
            yield i

n = int(raw_input("n : "))
numbers = []
for i in div_num_gen(n):
    numbers.append(str(i))

print ",".join(numbers)
