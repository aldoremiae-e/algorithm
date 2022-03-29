def f(n, k):    # 순열
   if n == k:
       print(p)
   else:
       for i in range(k):      # used 사용하지 않은 숫자 검색
            if used[i] == 0:    # 앞에서 사용하지 않은 숫자인 경우
                used[i] = 1     # 사용함으로 표시
                p[n] = a[i]
                f(n+1, k)
                used[i] = 0     #a[i]를 다른 위치에서 사용할 수 있도록 함

a = [1, 2, 3]
p = [0] * 3
used = [0] * 3
f(0, 3)