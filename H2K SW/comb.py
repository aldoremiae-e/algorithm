from sys import stdin

'''
내가 해야 할 문제
김현기 사물함찾기 96212
8개의 사물함 - 3개씩 열어
'''
def dfs(n, idx):
    if n == 3:
        # 출력
        print(*locker)
        return
    for i in range(idx, 8):
        if locker[i] == 1:
            continue
        locker[i] = 1
        dfs(n+1, i)
        locker[i] = 0

locker = [0] * 8
dfs(0, 0)