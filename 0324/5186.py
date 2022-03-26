T = int(input())
for tc in range(1, T+1):
    N = float(input()) # N은 0~1 사이
    s = ''
    divv = 1
    for _ in range(12):
       divv *= 1/2
       if N - divv >= 0:
           s += '1'
           N -= divv
           if N == 0:
               break
       else:
           s += '0'
    if N:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {s}')