T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    rear = N
    front = 0
    q = [(0, 0)] * N # 화덕

    for i in range(N):
        q[i] = [i, cheese[i]]

    pizza = q.pop(0)
    print(pizza)
