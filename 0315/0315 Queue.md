# 0315 Queue

## [5097] 회전

- queue라는 M크기의 리스트를 만들어서 temp처럼 사용

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    front = -1
    q = [0] * M

    for i in range(M):
        front += 1
        q[front] = arr[0]
        for k in range(N-1):
            arr[k] = arr[k+1]
        arr[N-1] = q[front]
    print(f'#{tc} {arr[0]}')
```

- 다른풀이

  ```python
  T = int(input())
  for tc in range(1, T+1):
      N, M = map(int, input().split())
      arr = list(map(int, input().split()))
  
      ans = arr[M % N]
      print(f'#{tc} {ans}')
  ```

  

```python
'''
3
3 10
5527 731 31274 
5 12
18140 14618 18641 22536 23097 
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907 
'''
#1 731
#2 18641
#3 2412
```

