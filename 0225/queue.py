# 인큐 - 삽입
    # rear = rear + 1
    # q[rear] = item
# 디큐 - 삭제
    # front = front + 1
    # q[front]
# 공백 및 포화상태
    # front == rear  공백
    # rear == len(q) - 1  포화

front = -1
rear = -1
q = [0] * 10

rear += 1
q[rear] = 1
print(front, rear, q)
rear += 1
q[rear] = 2
print(front, rear, q)

front += 1
print(q[front])
front += 1
print(q[front])