#calc

for tc in range(1, 11):
    N = int(input())
    arr = list(input())
    s = []
    # 후위 표기식
    for x in arr:
        if x == '+':
            if len(s) >= 2:
                b = s.pop()
                a = s.pop()
                s.append(a+b)
        else:
          s.append(int(x))

    b = s.pop()
    a = s.pop()
    print(f'#{tc} {a+b}')