'''
괄호는 연산자, 스택이 비어있음 - > 스택에 푸쉬
토큰은 그대로 출력
연산자는 스택에 쌓아야함, 연산자 우선순위가 top보다 높으면 top을 변경하여 스택에 추가
연산자 우선순위가 같을 때는 top을 pop하여 출력후 top에 스택을 추가
닫는 괄호는 자기와 짝이 만날때까지 모두 pop함 ,짝이 되면 버리기.
'''
'''
피연산자를 만나면 stack에 푸시
연산자를 만나면 필요한 만큼의 피연산자를 stack에서 pop하고, 연산결과를 push
수식이 끝나면 stack을 pop하여 출력
'''

for tc in range(1, 11):
    N = int(input())
    infix = input()
    postfix = ''  # 고칠곳
    stack = [0] * N
    top = -1
    icp = {'+': 1, '*': 2}  # 연산자 우선순위

    for i in range(N):
        # 피연산자인 경우 그대로 출력
        if '0' <= infix[i] <= '9':
            postfix += infix[i]
        else:
            # stack이 있고, stack 우선순위가 같거나 높으면 pop
            while top > -1 and icp[stack[top]] >= icp[infix[i]]:
                postfix += stack[top]  # pop 1
                top -= 1  # pop 2
            # top을 쌓아 스택에 추가
            top += 1
            stack[top] = infix[i]
    # 스택에 있는 모든것을 pop
    while top > -1:
        postfix += stack[top]
        top -= 1

    # 계산
    stack2 = []
    for k in range(len(postfix)):
        if postfix[k] == '+':
            b = int(stack2.pop())
            a = int(stack2.pop())
            stack2.append(a + b)

        elif postfix[k] == '*':
            b = int(stack2.pop())
            a = int(stack2.pop())
            stack2.append(a * b)
        else:
            stack2.append(postfix[k])

    print(f'#{tc} ', end='')
    print(*stack2)