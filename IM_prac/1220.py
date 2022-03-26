'''
1: 빨강 2: 파랑
한 열에 한개만 있을 때 없어짐
1행 - 2, 마지막 행 - 1일때 없어짐
한 열에 1,2가 (1,1) (2,1) (1,2) 있을 때 cnt +1 -> 둘중 작은걸로 더하기
두개를 써야해 (2,2) 라면 cnt +2 같으면 같은 숫자로

델타를 이용하려면 이친구를 자성체가 움직이도록
'''


'''
열우선 탐색
상태가 0일 떄 1을 만난 경우
상태가 1일 때 2를 만난 경우
'''

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    cnt = 0 # 교착 상태 수
    for j in range(100):
       state = 0
       for i in range(100):
           if state == 0 and arr[i][j] == 1:
               state = 1
           elif state == 1 and arr[i][j] == 2:
               cnt += 1
               state = 0
           print(cnt)