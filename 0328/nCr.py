def f(n, r, s, k):      # n개에서 r개를 고르는 조합, s는 선택구간의 시작, k 고른 개수
    if r == 0:
        print(comb)
    else:
        for i in range(s, n-r+1):     #n-r+k 선택할 수 있는 구간의 끝
            comb[k-r] = arr[i]
            f(n, r-1, i+1, k)
n = 10
r = 3
k = r
arr = [i for i in range(1, n+1)]
comb = [0] * r
f(n, r, 0, k)