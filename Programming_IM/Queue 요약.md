## Queue 연산

| 연산           | 기능                                                  |
| -------------- | ----------------------------------------------------- |
| en_Queue(item) | Queue의 뒤쪽(rear 다음)에 원소를 삽입                 |
| de_Queue()     | Queue의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산 |
| create_Queue() | 공백 상태의 Queue를 생성하는 연산                     |
| is_Empty()     | 공백 상태인지 확인                                    |
| is_Full()      | 포화 상태인지 확인                                    |
| Qpeek()        | Queue의 앞쪽(front)에서 원소를 삭제없이 반환하는 연산 |



### 선형 큐

create_Queue():

```python
front = -1
rear = -1
q = [0] * 10
```

en_Queue(item):

```python
rear = rear + 1
q[rear] = item
```

de_Queue():

```python
front = front - 1
q[front]
```

is_Empty(): # 앞이랑 뒤가 같잖아요

```python
front == rear
```

is_Full(): # 뒤가 끝번호랑 같잖아요

```python
rear == len(Queue) - 1
```



### 원형 큐

create_Queue():

```python
front = 0
rear = 0
q = [0] * 10
```

en_Queue(item):

```python
rear = (rear + 1) mod n
q[rear] = item
```

de_Queue():

```python
front = (front + 1) mod n
q[front]
```

is_Empty(): # 앞이랑 뒤가 같잖아요

```python
front == rear
```

is_Full():  # rear 다음 위치가 현재 front랑 같으면 다 찬거지

```python
(rear+1) mod n == front
```



### 연결 큐

create_Queue():

```python
front = NULL
rear = NULL
q = [0] * 10
```

en_Queue(item):		# 앞이 비어있으면

```python
if front = NULL:
    rear = NEW
    front = NEW
```

de_Queue():

> old가 지울 노드를 가르키고 front 재설정
>
> 삭제 후 공백 Q가 되면,  rear = NULL
>
> old가 가리키는 노드를 삭제하고 메모리 반환

```python
old = front
q[front]
front 재설정?
if rear == NULL:
    free(old):
        return item
```

is_Empty(): # 앞이랑 뒤가 같잖아요

```python
front == NULL
```



## BFS (너비 우선 탐색)

```python
def BFS(G, v): # 그래프 G, 탐색 시작점 v
    # 큐 생성
    # 시작점 v를 큐에 삽입
    # 점 v를 방문한 것으로 표시
    while q:
        temp # 큐의 첫번째 원소 반환
        for: # 첫번째 원소와 연결된 모든 선에 대해
            u # temp의 이웃점
            # u가 방분되지 않은 곳이면
            # u를 큐에 넣고, 방문한 것으로 표시
           
```

