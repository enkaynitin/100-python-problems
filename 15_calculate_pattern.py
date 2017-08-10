a = input("Enter a:")
n1 = ("{0}".format(a))
n2 = ("{0}{1}".format(a,a))
n3 = ("{0}{1}{2}".format(a,a,a))
n4 = ("{0}{1}{2}{3}".format(a,a,a,a))

print int(n1) + int(n2) + int(n3) + int(n4)
