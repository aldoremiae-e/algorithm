T = int(input())
for tc in range(1, T+1):
    s = input()

    stack = ['']*len(s)
    top = -1
    ans = 1

    for x in s:
        if x == '(' or x == '{':
            top += 1
            stack[top] = x
        elif x == ')':
            if stack[top] == '(':
                stack[top] = ''
                top -= 1
            else:
                ans = 0
                break
        elif x == '}':
            if stack[top] == '{':
                stack[top] = ''
                top -= 1
            else:
                ans = 0
                break
    else:
        if top != -1:
            ans = 0

    print(f'#{tc} {ans}')