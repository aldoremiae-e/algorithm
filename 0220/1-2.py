'''[55 7 78 12 42] 오름차순 정렬'''

arr = [55, 7, 78, 12, 42]
# 배열의 마지막 인덱스부터
for i in range(len(arr)-1, 0, -1):
    # 왼쪽 원소들을 차례로 비교, i번째 전까지
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    print('-'*25)