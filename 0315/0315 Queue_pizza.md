# 0315 Queue_pizza



```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    rear = N
    front = 0
    q = [0] * N     # 화덕
    idx = [0] * N
    # 초기 화덕에 피자를 채워넣음
    for i in range(N):
        q[i] = cheese[i]
        idx[i] = i
    while sum(q) != 0:  # 화덕에 피자가 없을 때
        check = front % N # 인덱스
        # 치즈 반갈
        q[check] = q[check] // 2
        if q[check] == 0:
            if rear < M:    # 다음피자가 존재할 때
                idx[check] = rear   # 화덕에 피자변경
                q[check] = cheese[rear]
                rear += 1
            else:
                q[check] = 0
        front += 1
        
    # while문을 빠져나올 떄 마지막으로 본 화덕 인덱스 : check
    # 화덕에 있던 피자의 인덱스
    print(f'#{tc} {idx[check]+1}')
```

```python
'''
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2
'''

#1 4
#2 8
#3 6
```

