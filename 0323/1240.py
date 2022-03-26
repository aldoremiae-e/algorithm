import sys
sys.stdin = open("1240in.txt", "r")

h2b = ['0000', '0001', '0010', '0011', '0100', '0101', '0110',  '0111', '1000',
       '1001', '1010', '1011', '1100', '1101', '1110', '1111']
# 마지막 자리 : 홀수자리합 * 3 + 짝수자리합 + 검증코드 = 10의배수
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    codes = [list(map(int, input())) for _ in range(N)]

    for code in codes:
        s = ''
        for i in range(M):
            s += h2b[code[i]]
        for i in range(M*4 // 7):
            print(int(s[i*7:i*7+7], 2), end=' ')
        print()