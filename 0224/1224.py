'''괄호 들어간 계산기'''
# 계산
def calc():
    stack = []

    for k in range(len(postfix)):

        if postfix[k] in icp and len(stack) < 2:
            return 'error'

        elif postfix[k] == '+':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a + b)

        elif postfix[k] == '-':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a - b)

        elif postfix[k] == '*':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a * b)

        elif postfix[k] == '/':
            b = int(stack.pop())
            a = int(stack.pop())
            if b == 0:
                return 'error'
            stack.append(int(a / b))

        elif postfix[k] == '.':
            if len(stack) == 1:
                return int(stack.pop())
            else:
                return 'error'

        else:
            stack.append(postfix[k])


for tc in range(1, 11):
    N = int(input())
    infix = input()
    postfix = []  # 고칠곳
    stack = []
    top = -1
    icp = ['(', '+', '-', '*', '/', ')']  # 연산자 우선순위 # 연산자 우선순위

    for i in range(N):
        # 피연산자인 경우 그대로 출력
        if '0' <= infix[i] <= '9':
            postfix.append(infix[i])
        else:
            # 연산자인데 괄호인데 처음들어옴
            if infix[i] == '(':
                stack.append(infix[i])
            # 괄호 짝을 찾을 때까지 postfix에 pop
            if infix[i] == ')':
                while stack[-1] != '(':
                    postfix.append(stack.pop())

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