T = int(input())
for tc in range(1,T+1):
    text = list(map(str, input()))

    stack = [''] * len(text)
    top = -1

    for i in range(len(text)):
        if text[i] not in stack:
            top += 1
            stack[top] = text[i]

        elif text[i] in stack:
            if text[i] == stack[top]:
                stack[top] = ''
                top -= 1
            else:
                top += 1
                stack[top] = text[i]
    cnt = 0
    for x in stack:
        if x != '':
            cnt += 1
    print(f'#{tc} {cnt}')