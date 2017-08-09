print "Enter 2 digits, X,Y"
ar_dim = [int(d) for d in raw_input().split(',')]

d1 = ar_dim[0]
d2 = ar_dim[1]

arr = [[0 for i in range(d2)] for j in range(d1)]

for i in range(d1):
    for j in range(d2):
        arr[i][j] = i*j

print arr
