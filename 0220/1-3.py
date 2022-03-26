'''카운팅 정렬'''

arr = [0, 4, 1, 3, 1, 2, 4, 1]
count = [0 for _ in range(10)]
result = [0 for _ in range(len(arr))]

# 개수만큼 인덱스에 +1
for i in range(len(arr)):
    count[arr[i]] += 1
# count 배열의 원소를 누적값으로 갱신
for j in range(1, len(count)):
    count[j] += count[j-1]
    print(count)

#  result에 삽입
for num in arr:
    idx = count[num]
    result[idx-1] = num
    count[num] -= 1
    print(result)
    print('-'*25)