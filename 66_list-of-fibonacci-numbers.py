def nth_fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return nth_fibonacci_number(n-1) + nth_fibonacci_number(n-2)

n = int(raw_input("n : "))
fib_list = [str(nth_fibonacci_number(i)) for i in range(0,n+1)]
print ",".join(fib_list)
