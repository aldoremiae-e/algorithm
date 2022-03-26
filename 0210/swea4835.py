# 부분합

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    re = []
    for i in range(len(lst)-M+1):
        lst2 = lst[i:i+M]
        cnt = 0
        for j in range(len(lst2)):
            cnt += lst2[j]
        re.append(cnt)
    min_num = re[0]
    max_num = re[0]
    for i in range(len(re)):
        if re[i] < min_num:
            min_num = re[i]
    for i in range(len(re)):
        if re[i] > max_num:
            max_num = re[i]
    print(f'#{tc} {max_num - min_num}')

## 하나빼고 하나더하는 식으로해보자 ( M : 엄청크면 힘들어)


