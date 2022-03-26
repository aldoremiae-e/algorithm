def f_memo(n):
    global cnt
    cnt += 1
    if n >= 2 and memo[n] == 0:
        memo[n] = f_memo(n-1) + f_memo(n-2)
    return memo[n]

N = 10
cnt = 0
memo = [0] * (N+1)
memo[0] = 0
memo[1] = 1
# 값을 저장해서 회귀를 좀 줄여줌
print(f_memo(N), memo, cnt)