'''선택정렬'''
arr = [64, 25, 10, 22, 11]
N = len(arr)
for i in range(N):
    for j in range(i+1,N):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
    print(arr)
