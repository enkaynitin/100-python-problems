from timeit import Timer

for i in range(1,100):
    print i

t = Timer("for i in range(1,100): 1+1")
print t.timeit()
print t
