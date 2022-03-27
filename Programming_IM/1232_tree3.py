import sys
sys.stdin = open("1232.txt", "r")

def post_order(n):
    global lst
    if 0 < n:
        post_order(L[n])
        post_order(R[n])
        lst.append(tree[n])

def cal(num1, num2, calc):
    if calc == '+':
        return num1 + num2
    elif calc == '-':
        return num1 - num2
    elif calc == '*':
        return num1 * num2
    elif calc == '/':
        return num1 / num2

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    L = [0] * (N+1)
    R = [0] * (N+1)
    lst = []
    for i in range(N):
        arr = list(map(str, input().split()))
        if len(arr) == 4:
            L[int(arr[0])] = int(arr[2])
            R[int(arr[0])] = int(arr[3])
            tree[int(arr[0])] = arr[1]
        else:
            tree[int(arr[0])] = int(arr[1])
    post_order(1)


    s = []
    for i in range(len(lst)):
        if type(lst[i]) == int:
            s.append(float(lst[i]))
        else:
            b = s.pop()
            a = s.pop()
            result = cal(a, b, lst[i])
            s.append(result)
    print(f'#{tc} {int(s.pop())}')