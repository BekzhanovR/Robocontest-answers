# FIXME: Qate bar soni durislaw kerek
# TODO: Qatelerdi korip shigin'
def find_min_item(array: list):
    minItem = array[0]
    for i in array:
        if i <= minItem:
            minItem = i
    return minItem

def find_max_item(array: list):
    maxItem = array[0]
    for i in array:
        if i >= maxItem:
            maxItem = i
    return maxItem

def removeItem(number: int, array: list):
    newarr = []
    for i in array:
        if i != number:
            newarr.append(i)
    return newarr

def Sum_Array(array: list):
    result = 0
    for i in array:
        result += i
    return result

arr = list(map(int,input().split()))
maxItem = find_max_item(arr)
minItem = find_min_item(arr)
newarr1 = removeItem(maxItem,arr)
newarr2 = removeItem(minItem,arr)
print(Sum_Array(newarr1),Sum_Array(newarr2))

arr = list(map(int,input().split()))
print(sum(arr)-max(arr),sum(arr)-min(arr))