def PrintDic():
    d = dict()
    for i in range(0,21):
        d[i] = i**2
    for (key,square) in d.items():
        print square

PrintDic()
