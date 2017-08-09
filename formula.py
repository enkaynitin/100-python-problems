import math

C = 50
H = 30
calculate = raw_input().split(',')  # raw_input() stores as a string
result =[]

def Q(args):
    l=[]
    D = [d for d in args]
    for d in D:
        d = float(d)
        c = str(int(math.sqrt(( 2 * C * d)/H))) # output of math.sqrt() is
        # converted to int and then to string as per the required output
        l.append(c)
    return l   # l is list of type string elements
result = Q(calculate)
print ','.join(result)
