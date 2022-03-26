T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s = input()
    stack = [0] * N
    post= ''
    top = -1
    icp = {'+': 1, '*': 2}
    for i in range(N):
        if '0' <= s[i] < '9':
                post += s[i]
        else:
            while top > -1 and icp[stack[top]] >= icp[s[i]]:
                post += stack[top]
                top -= 1
            top += 1
            stack[top] = s[i]
    while top > -1:
        post += stack[top]
        top -= 1

    result =[]
    for k in range(N):
        if post[k] == '*':
            b = int(result.pop())
            a = int(result.pop())
            result.append(a * b)
        elif post[k] == '+':
            b = int(result.pop())
            a = int(result.pop())
            result.append(a + b)
        else:
            result.append(post[k])
    print(f'#{tc} {result.pop()}')
