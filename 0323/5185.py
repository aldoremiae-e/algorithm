h2b = ['0000', '0001', '0010', '0011', '0100', '0101', '0110',  '0111', '1000',
       '1001', '1010', '1011', '1100', '1101', '1110', '1111']

T = int(input())
for tc in range(1, T+1):
    N, num = map(str, input().split())
    num = list(num)

    for i in range(int(N)):
        if '0' <= num[i] <= '9':
            num[i] = int(num[i])
        else:   # A~F
            num[i] = ord(num[i]) - ord('A') + 10
    s = ''
    for i in range(int(N)):
        s += h2b[num[i]]
    print(f'#{tc} {s}')