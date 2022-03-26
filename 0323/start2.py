def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output, end=' ')
# 16진수로 나타내려면 0x 10~15(a~f로 표현) 16진수 한자리값 2진수로 나타냄
a = 0x10
x = 0x01020304
print("%d = " % a, end='')
Bbit_print(a)
print()
print("0%X = " % x, end='')
for i in range(0, 4):
    Bbit_print((x >> i*8) & 0xff)

