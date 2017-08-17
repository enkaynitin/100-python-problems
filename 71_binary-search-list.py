import math
def binary_s(list, element):
    bottom = 0
    top = len(list)-1
    index = -1

    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if list[mid] == element:
            index = mid
        elif element < list[mid]:  # element in first half
            top = mid-1
        else:
            bottom = mid+1         # element in second half

    return index

list = [1,2,3,4,5,6,7,8,9,10,11,12,17,222]
print binary_s(list,11)
print binary_s(list,222)
