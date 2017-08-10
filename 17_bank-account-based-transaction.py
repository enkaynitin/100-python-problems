balance = 0
while True :
    transaction = raw_input()
    if not transaction:
        break
    values = transaction.split(' ')
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        balance+=amount
    elif operation=="W":
        balance-=amount
    else:
        pass

print balance        
