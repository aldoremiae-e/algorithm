'''
+1 -1 *2 -10
N , M
'''
def bfs(n, m):
    q = []  # 큐 생성
    visited = [0] * 1000001 # 방문 표시 (cnt역할)
    q.append(n)     # 시작점 인큐
    visited[n] = 0
    while q:
        n = q.pop(0)
        if n == m:
            return visited[n]
        for i in (n+1, n-1, n*2, n-10):
            if i > 0 and i <= 1000000:
                if visited[i] == 0:
                    visited[i] = visited[n] + 1
                    q.append(i)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = bfs(N, M)
    print(f'#{tc} {ans}')
