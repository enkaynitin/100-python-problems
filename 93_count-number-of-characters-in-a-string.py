dictionary = {}
s = raw_input("String : ")
for s in s:
    dictionary[s] = dictionary.get(s,0) + 1

print '\n'.join(["{} {}".format(k,v) for k, v in dictionary.items()])
