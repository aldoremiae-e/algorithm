def bina(n, key):
    left = 1
    right = n
    cnt = 1
    while left <= right:
        c = (left+right)//2
        if c == key:
            return cnt
        elif c > key:
            right = c
        else:
            left = c
        cnt += 1
    return False

T = int(input())
for tc in range(1,T+1):
    page, pa, pb = map(int, input().split())

    a = bina(page, pa)
    b = bina(page, pb)

    if a < b:
        print('a')
    elif a == b:
        print('0')
    else:
        print('b')
