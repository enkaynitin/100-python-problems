def evenGenerator(n):
    i = 0
    while i <=n :
        if i%2 == 0:
            yield i
        i += 1

n = int(raw_input("n : "))
even_numbers = []
for i in evenGenerator(n):
    even_numbers.append(str(i))

print ",".join(even_numbers)
