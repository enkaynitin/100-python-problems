def PrintDic():
    d = dict()
    for i in range(1,21):
        d[i] = i**2
    for (key,square) in d.items():
        print square

PrintDic()
