#import sys
#sys.stdin = open("1225.txt","r")

for _ in range(1, 11):
    tc = int(input())
    arr = list(map(int, input().split()))
    i = 0
    num = 0   
    while arr[-1] > 0:
        re = arr.pop(0)
        re -= (num + 1)
        arr.append(re)
        num = (num + 1) % 5  # 뺄거야 5까지 감소하는게 한 사이클이다.
    arr[-1] = 0
    print(f'#{tc} ',end='')
    print(*arr)