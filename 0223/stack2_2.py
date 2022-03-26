'''DFS + 합을 같이 구하는 방법 ( 백트래킹 ) '''
def f(i, N, K, S): # S: i-1원소까지 고려한 합
    global cnt
    cnt += 1
    # 모든원소가 고려되지 않았는데 합이 S==K가 되었을 때
    if S == K:
        for j in range(N):
            if bit[j]:
                print(a[j], end=' ')
        print()
    elif i == N: # 한개의 부분집합이 완성될 경우
        return
    # K를 너무 많이 집어넣었는데, 부분집합이 완성되지도 않았어
    elif S > K:
        return
    else:
        bit[i] = 1
        f(i+1, N, K, S+a[i])
        bit[i] = 0
        f(i+1, N, K, S)
    return

N = 10
a = [x for x in range(1, N+1)]
bit = [0] * N
K = 10
cnt = 0
f(0, N, K, 0)
print(cnt)