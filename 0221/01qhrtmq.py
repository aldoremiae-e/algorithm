'''
1차원 배열을 사용하여 구현할 경우 구현이 용이하다
스택의 크기를 변경하기 어렵다
동적 연결리스트를 이용하여 구현 => 메모리를 효율적으로 사용한다
'''
stack = ['']*5
top = -1
#stack.append(10)
top += 1
stack[top] = 10
top += 1
stack[top] = 20
top += 1
stack[top] = 30
print(stack)
print(stack[top])
top -= 1
print(stack[top])
top -= 1
print(stack[top])
top -=1