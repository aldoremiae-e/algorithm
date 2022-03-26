# 더이상 갈 수 없는 방향이면 뒷걸음질 치는 방법
# maze
# 부분집합 구하기

def f(i, N, K):    #i 부분집합에 포함될지 결정할 원소인덱스, N 원소개수
    if i == N:  # 한개의 부분집합 완성
        print(bit, end =' ')
        s = 0
        for j in range(N):
            if bit[j]:
                s += a[j]
                #print(a[j], end=' ')
        #print()
        if s == K:
            for j in range(N):
                if bit[j]:
                    print(a[j], end=' ')
        print()
    else:
        bit[i] = 1
        f(i+1, N, K)
        bit[i] = 0
        f(i+1, N, K)

a = [1, 2, 3]
bit = [0, 0, 0]
K = 4
f(0, 3, K)
