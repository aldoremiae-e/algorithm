'''이진탐색'''

arr = [2, 4, 7, 9, 11, 19, 23]
N = len(arr)
ser = 7

def b(a, key):
    N = len(a)
    start = 0
    end = N-1
    while start <= end:
        middle = (start+end) //2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

print(b(arr,ser))