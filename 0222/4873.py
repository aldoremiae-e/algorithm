T = int(input())
for tc in range(1, T+1):
    txt = list(map(str, input()))
    n = len(txt)

    stack = [''] * n
    top = -1

    for i in txt:
        # stack에 i가 없거나 같지 않으면
        if stack[top] != i:
            #push
            top += 1
            stack[top] = i
        # stack에 i가 있으면
        else:
            #pop
            top -= 1
    # 남은 스택의 수
    print(f'#{tc} {top+1}')






