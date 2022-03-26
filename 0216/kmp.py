'''
t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t, p)
t = 'AABAACAADAABAABA'
p = 'AABA'
kmp(t, p)
t = 'AAAAABAAABA'
p = 'AAAA'
kmp(t, p)
'''

def kmp(t,p):
    # t의 길이 , p의 길이
    N, M = len(t), len(p)
    # lps의 하는 일은 무엇일까, p+1의 길이
    lps = [0] * (M+1)

    # j는 지금까지 일치한 개수수