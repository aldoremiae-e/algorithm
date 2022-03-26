'''
토너먼트 카드게임
f(i ,j)
if i == j #더이상 그룹을 나눌 수 없으면
    return i
else:
    left = f(i, (i+j)//2)
    right = f((i+j)//2 , j)

    return win(left, right)
'''

def win(a, b, arr):
    # 1:가위 2:바위 3:보
    if arr[a-1] == arr[b-1]:
        return a
    elif arr[a-1] == 1:
        if arr[b-1] == 2:
            return b
        else:
            return a
    elif arr[a-1] == 2:
        if arr[b-1] == 1:
            return a
        else:
            return b
    elif arr[a-1] == 3:
        if arr[b-1] == 1:
            return b
        else:
            return a

def f(i, j):
    if i == j:
        return i
    else:
        left = f(i, (i+j)//2)
        right = f((i+j)//2+1, j)

        return win(left, right, arr)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    i = 1
    j = N
    print(f'#{tc} {f(i, j)}')