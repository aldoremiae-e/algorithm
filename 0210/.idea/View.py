# 빌딩들의 대한 정보가 주어질 떄, 조망권이 확보된 세대의 수
# 한 건물씩 -> 한 층씩 -> 한 건물의 오른쪽 두번째의 같은 층
# 한 층씩 -> 1층에서 2번째 건물 오른쪽 두번째 건물이 있으면
# 0 0 3 5 2 4 9 0 6 4 0 6 0 0
def view(a):
    result = 0
    for i in range(2,len(a)-2):
        #  4개 값 중 최댓값
        max_num = a[i - 2]
        max_l = a[i + 1]
        if a[i - 1] > max_num:
            max_num = a[i - 1]
        if a[i + 2] > max_l:
            max_l = a[i + 2]
        if max_l > max_num:
            max_num = max_l
        # 오른쪽
        if a[i] > a[i-2] and a[i] > a[i-1]:
            # 왼쪽
            if a[i] > a[i+1] and a[i] > a[i+2]:
                result += (a[i] - max_num)
    return result

for tc in range(1,11):
    #가로길이 N = len(arr), 높이 0~225
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {view(arr)}')

