#calc

for tc in range(1, 2):
    N = int(input())
    arr = list(input())
    #s = []
    s = [0] * N
    top = -1
    re = ''
    calc = {'+': 1, '*': 2}

    # 후위 표기식 변환 후 계산
    for x in arr:
        if '0' <= x <= '9':   # 숫자
            re += x

        else:   # 연산자
            # stack이 있고, stack에 있는 것이 현재 것보다 우선순위가 높거나 같을 때
            #while s and calc[s[-1]] >= calc[x]:
            while top > -1 and calc[s[top]] >= calc[x]:
                #re.append(s.pop())    # 결과에 연산자 push
                re += s[top]
                top -= 1
            #s.append(x)# 스택에 연산자 push
            top += 1
            s[top] = x

    # s이 남았다면 남은 거 다꺼내자
    while top > -1:
        #re.append(s.pop())
        re += s[top]
        top -= 1

    s2 = [0] * N
    for x in re:
        if '0' <= x <= '9':
            top += 1
            s2[top] = x
        else:
            if x == '*':
                b = int(s2[top])
                top -= 1
                a = int(s2[top])
                s2[top] = a * b
            else:
                b = int(s2[top])
                top -= 1
                a = int(s2[top])
                s2[top] = a + b
    print(f'#{tc} {s2[top]}')