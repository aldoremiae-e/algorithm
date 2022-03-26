T = int(input())
for tc in range(1, T+1):
    txt = input().split()
    N = len(txt)

    stack = [0] * N
    top = -1

    for x in txt:
        if x == '.':
            break
        elif x == '+':
            b = int(stack[top])
            stack[top] = 0
            top -= 1
            a = int(stack[top])
            stack[top] = a + b
        elif x == '*':
            b = int(stack[top])
            stack[top] = 0
            top -= 1
            a = int(stack[top])
            stack[top] = a * b
        elif x == '-':
            b = int(stack[top])
            stack[top] = 0
            top -= 1
            a = int(stack[top])
            stack[top] = a - b
        elif x == '/':
            b = int(stack[top])
            stack[top] = 0
            top -= 1
            a = int(stack[top])
            stack[top] = a // b
        else:
            top += 1
            stack[top] = x

    if top == 0:
        print(f'#{tc} {stack[0]}')
    else:
        print(f'#{tc} error')