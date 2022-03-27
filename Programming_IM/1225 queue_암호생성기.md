# 1225 암호생성기



## 코드

```python
for _ in range(1, 11):
    tc = int(input())
    arr = list(map(int, input().split()))
    i = 0
    num = 0   
    while arr[-1] > 0:
        re = arr.pop(0)
        re -= (num + 1)
        arr.append(re)
        num = (num + 1) % 5  # 뺄거야 5까지 감소하는게 한 사이클이다.
    arr[-1] = 0
    print(f'#{tc} ',end='')
    print(*arr)
```

```python
'''에제 답
1
10 6 12 8 9 4 1 3
'''
#1 3 9 4 9 4 4 3 0
```



## 생각해야할 점

문제를 잘 읽자!!!

한 사이클이 5까지 감소하는 것을 간과한 채로 계속 감소하는 식으로 하니 원하는 값이 나오지 않았다.

또한 pop과 append를 이용하니 코드가 아주 간단해졌다.