list = [12,24,35,70,88,120,155]

list = [ e for (i,e) in enumerate(list) if i not in [0,2,4,6]]
print list
