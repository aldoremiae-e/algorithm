def binarySearch(n, key):
    left = 1
    right = n
    cnt = 1
    while True:
        c = int((left+right)/2)
        if c == key:
            return cnt
        # 이진탐색에서의 start와 end는 포함되지 않음
        elif c > key:
            right = c # c-1 이면 c-1은 검사를 못하게 됨
        else:
            left = c # c+1 이면 c+1은 검사를 못하게 됨
        cnt += 1
    return False

T = int(input())
for tc in range(1, T+1):
    page, pa, pb = map(int, input().split())

    a = binarySearch(page, pa)
    b = binarySearch(page, pb)

    if a < b:
        print(f'#{tc} A')
    elif a == b:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} B')