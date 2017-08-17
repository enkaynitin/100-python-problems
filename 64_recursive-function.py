def rf(n):
    if n == 0:
        return 0
    else:
        return rf(n-1) + 100

n = int(raw_input("n : "))
print rf(n)
