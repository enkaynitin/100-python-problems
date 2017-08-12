def Compare_print_max(a,b):
    if len(a) > len(b):
        print a
    elif len(a) == len(b):
        print a, "\n"
        print b
    else:
        print b


Compare_print_max("Nitin", "Kumar")
