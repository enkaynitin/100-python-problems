sentence = raw_input()
d = {
    "DIGITS":0, "LETTERS":0
}

for c in sentence:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]
        
