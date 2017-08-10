number = raw_input().split(',')
bin_div_by_5 = []

l = len(number)
if l != 4:
    print "Enter 4 binary numbers"

def binary_check(args):
    binary = ['0','1']
    position = {
        1:'st',
        2:'nd',
        3:'rd',
        'more':'th',
    }
    for i in range(l):
        for j in range(4):
            if args[i][j] not in binary:
                if i < 3 :
                    print i+1,position[i+1], "number is not a binary"
                elif i > 3:
                    print i+1,position['more'],"number is not a binary"
                    i+=1
            if i == 3 and j == 3:
                return True

def divisilibity_check(arg,d):
    if arg%d == 0:
        return True

if binary_check(number):
    for n in number:
        if divisilibity_check(int(n),5):
            bin_div_by_5.append(n)

print ','.join(bin_div_by_5)
