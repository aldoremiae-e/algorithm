T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]

    num = 0
    end = N - 1
    front = 0
    J = 0
    I = 0
    while num != N * N:
        if J == front and I == front:
            J = end
            for j in range(front, end + 1):
                num += 1
                arr[front][j] = num
        elif J == end and I == front:
            I = end
            for i in range(front + 1, end + 1):
                num += 1
                arr[i][end] = num
        elif J == end and I == end:
            J = front
            for j in range(end - 1, front - 1, -1):
                num += 1
                arr[end][j] = num
        elif J == front and I == end:
            front += 1
            I = front
            for i in range(end - 1, front, -1):
                num += 1
                arr[i][front-1] = num
            end -= 1

    print(arr)
