lines = []
while True:
    c = raw_input()
    if c:
        lines.append(c.upper())
    else:
        break

for sentence in lines:
    print sentence
