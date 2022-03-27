for tc in range(1, 11):
    N = int(input())
    arr = list(input())

    isp = {'(': 0, '+': 1, '*': 2}  # 스택안에 있을 때의 우선순위
    icp = {'(': 3, '+': 1, '*': 2}  # 스택에 넣어줄 떄의 우선순위
    s = []
    re = ''
    for x in arr:
        if '0' <= x <= '9':
           re += x

        else:   # 연산자
            if s:
                if x == ')':    # 괄호가 닫힐때

                    while s[-1] != '(':     #여는 괄호가 있는데까지
                        re += s.pop()   #pop
                    s.pop()     #여는 괄호 없애주기

                elif isp[s[-1]] <= icp[x]:       # 현재 연산자의 우선순위가 더 클 때
                    s.append(x)

                else:       # 스택의 우선순위가 더 클 때
                    while s[-1] != '(':    # 스택에 있는 거 다 pop
                        re += s.pop()
                    s.append(x)
            else:
                s.append(x)

    while s:
        re += s.pop()

    # 계산
    s2 = []
    calc = ['+', '*']
    for x in re:
        if x not in calc:
            s2.append(int(x))
        else:
            if x == '+':
                b = s2.pop()
                a = s2.pop()
                s2.append(a+b)
            else:
                b = s2.pop()
                a = s2.pop()
                s2.append(a*b)
    print(f'#{tc} {s2[-1]}')

