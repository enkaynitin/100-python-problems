import math

C = 50
H = 30
calculate = raw_input().split(',')
result =[]

def Q(args):
    l=[]
    D = [d for d in args]
    for d in D:
        d = float(d)
        c = str(int(math.sqrt(( 2 * C * d)/H)))
        l.append(c)
    return l
result = Q(calculate)
print ','.join(result)
