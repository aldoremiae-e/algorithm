N = 10
arr = [[0]*N for _ in range(N)]
r = c =7

# 우
for i in range(c+1, N):
    arr[r][i] = 1
# 하
for i in range(r + 1, N):
    arr[i][c] = 2
# 좌
for i in range(c-1,-1,-1):
    arr[r][i] = 3
# 상
for i in range(r-1,-1,-1):
    arr[i][c] = 4

for lst in arr:
    print(*lst)