list = raw_input().split(',')
odd_list = []
print list
for i in range(len(list)):
    if int(list[i])%2 == 0:
        pass
    else:
        odd_list.append(list[i])
print ','.join(odd_list)
