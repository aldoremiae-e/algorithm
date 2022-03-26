def f(n):
    global cnt
    cnt += 1
    if n < 2:
        return n
    else:
        return f(n-1) + f(n-2)
cnt = 0
N = 10
print(f(N),cnt)
