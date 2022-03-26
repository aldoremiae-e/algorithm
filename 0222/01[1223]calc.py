'''
3+4+5*6+7   중위표기법
34+56*+7+    후위표기법
'''
for tc in range(1, 10+1):
    N = int(input())
    text = list(map(str, input()))
    # 우선순위를 위해서 딕셔너리로 한거임
    icp = {'+': 1, '*': 2}
    stack = [0] * N
    top = -1
    res = ''
    # 후위표기법
    for i in range(N):
        if text[i] not in icp:
            res += text[i]
        else:   # 연산자를 만나면
            while top > -1 and icp[stack[top]] >= icp[text[i]]:
                res += stack[top]
                top -= 1
            top += 1
            stack[top] = text[i]

    while top > -1:
        res += stack[top]
        top -= 1

    # 계산
    stack2 = [0] * len(res)
    for k in res:
        if k == '+':
            b = int(stack2[top])
            stack2[top] = 0
            top -= 1
            a = int(stack2[top])
            stack2[top] = 0
            stack2[top] = a + b
        elif k == '*':
            b = int(stack2[top])
            stack2[top] = 0
            top -= 1
            a = int(stack2[top])
            stack2[top] = 0
            stack2[top] = a * b
        else:
            top += 1
            stack2[top] = k
    print(f'#{tc} {stack2[0]}')