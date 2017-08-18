S = ["I", "You"]

O = ["Hockey","Football"]
V = ["Play", "Love"]

for i in range(len(S)):
    for j in range(len(O)):
        for k in range(len(V)):
            print "{} {} {}".format(S[i], O[j], V[k])
