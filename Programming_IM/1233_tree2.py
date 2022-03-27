import sys
sys.stdin = open("1233.txt", "r")

def post_order(n):
    global lst
    if n <= N:
        post_order(n*2)
        post_order(n*2+1)
        lst.append(tree[n])

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [''] * (N+1)
    lst = []
    for i in range(N):
        arr = list(map(str, input().split()))
        tree[int(arr[0])] = arr[1]
    post_order(1)
    result = 1
    s = []
    for i in range(len(lst)):
        if '0' <= lst[i] <= '9':
            s.append(int(lst[i]))
        elif lst[i] == '/' or lst[i] == '*' or lst[i] == '-' or lst[i] == '+':
            if len(s) < 2:
                result = 0
            else:
                if lst[i] == '/':
                    b = s.pop()
                    a = s.pop()

                    s.append(a // b)
                elif lst[i] == '*':
                    b = s.pop()
                    a = s.pop()
                    s.append(a * b)
                elif lst[i] == '-':
                    b = s.pop()
                    a = s.pop()
                    s.append(a - b)
                elif lst[i] == '+':
                    b = s.pop()
                    a = s.pop()
                    s.append(a + b)
    print(f'#{tc} {result}')