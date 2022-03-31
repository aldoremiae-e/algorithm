def f(n, k, m):    # 순열    - m개 중에 k개를 뽑는 경우
   if n == k:   # k개를 고른 경우
       print(p)
   else:
       for i in range(m):      # used 사용하지 않은 숫자 검색
            if used[i] == 0:    # 앞에서 사용하지 않은 숫자인 경우
                used[i] = 1     # 사용함으로 표시
                p[n] = a[i]
                f(n+1, k, m)
                used[i] = 0     #a[i]를 다른 위치에서 사용할 수 있도록 함

a = [1, 2, 3, 4, 5]
p = [0] * 3
used = [0] * 5
f(0, 3, 5)