# 계산
def calc():
    stack = []
    icp = ['+', '-', '*', '/']  # 연산자 우선순위
# 에러 : 연산자 전에 2개미만이면 에러, 나누는 값 0 이면 에러, . 나왔는데 결과아직이면 에러
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
            
T = int(input())
for tc in range(1, T+1):
    postfix = input().split()  # 고칠곳
    print(f'#{tc} {calc()}')