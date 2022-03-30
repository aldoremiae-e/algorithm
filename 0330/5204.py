def merge(l, r):
    global cnt
    global num
    num += 1
    result = []
    if l[-1] > r[-1]:
        cnt += 1
    i, j = 0, 0
    while len(l) > i or len(r) > j:
        if len(l) > i and len(r) > j:
            if l[i] <= r[j]:
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1
        elif len(l) > i:
            result.append(l[i])
            i += 1
        elif len(r) > j:
            result.append(r[j])
            j += 1
    return result

def msort(lst):
    if len(lst) == 1:
        return lst
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    left = msort(left)
    right = msort(right)
    return merge(left, right)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    num = 0
    result = msort(arr)
    print(f'#{tc} {result[N//2]}, {cnt} num={num}')