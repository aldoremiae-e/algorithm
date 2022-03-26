'''괄호 세기
4
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
())
(()


'''
#왼쪽 괄호를 만나면 스택에 삽입
#오른쪽 괄호를 만나면 스탭에서 top 괄호를 삭제한 후
#오른쪽 괄호와 짝이 맞는지 검사
    # 스택이 비어있으면 조건1 또는 조건2에 위배
    # 괄호의 짝이 맞지 않으면 조건3에 위배
    # 스택에 괄호가 남아 있으면 조건 1에 위배
def check(s):
    stack = []
    bracket = {')': '(', '}': '{'}

    for i in s:
        # 여는괄호이면 push
        if i == '(' or i == '{':
            stack.append(i)
        # 닫는괄호이면 pop
        elif i == ')' or i == '}':
            # stack이 비어있거나 top에 있는게 여는괄호와 맞지 않다면 실패
            if len(stack) == 0 or stack[-1] != bracket[i]:
                return 0
            stack.pop()
    # stack이 남아있으면 실패
    if stack:
        return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} {check(input())}')