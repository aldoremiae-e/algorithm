# 표준 입출력 방법
#import sys
#sys.stdin = open("a.txt", "r")

def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)

for i in range(-5, 6):
    print("%2d = " %i , end='')
    Bbit_print(i)