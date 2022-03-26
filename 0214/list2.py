#N = int(input())
#arr2 = [[0]*(N+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(N+2)]
#print(arr2)

#shallow copy 가 되기 때문에 한번에 다 바뀌기 때문에 이렇게 쓰면 안된다!
# 같은 애를 가르키는 애가 4번 반복되는 것이기 떄문에
#arr = [[0]*3 for _ in range(N)]
#print(arr)
#arr[0][1] = 1
#print(arr)

arr = [3,6,7,1,5,4]
n =len(arr)
for i in range(1<<n):				#1<<n :부분집합의 개수
    for j in range(n):				#원소의 수만큼 비트를 비교함
        if i & (1<<j):				# i의 j 번째 비트가 1인경우
            print(arr[j],end=', ')	# j번 원소 출력
    print()
print()