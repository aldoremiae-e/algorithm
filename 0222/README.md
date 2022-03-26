## 2차 배열에서 사각영역을 표현

- 사각영역 표현하기

  - 좌상단 좌표, 우하단 좌표

    ```python
    for r in range(r1, r2 + 1):
    	for c in range(c1, c2 + 1):
    		arr[r][c]
    ```

  ![image-20220222185717813](README.assets/image-20220222185717813.png)

  - 좌상단 좌표, 너비, 높이

    ```python
    # 좌상단 좌표 (r, c), h = 4, w = 5
    for i in range(r, r + h):
    	for j in raneg(c, c + w):
    		arr[i][j]
    
    ```

    ![image-20220222190308981](README.assets/image-20220222190308981.png)

------------------------

- 구간합 --> 패턴매칭, 파리퇴치, 회문, ... 
  - 길이가 N인 배열에서 길이 M인 가능한 모든 구간에 대해서 작업

![image-20220222191032384](README.assets/image-20220222191032384.png)

-----------

- 패턴 매칭

  - 텍스트에서 패턴이 존재하는 모든 위치를 찾는 문제

  ```python
  t = []
  p = []
  N, M = len(t), len(p)  
  # i: 텍스트의 인덱스, j: 패턴의 인덱스
  for i in range(0, N - M + 1):
  	# 길이가 M인 패턴을 비교
  	# 상태를 저장하는 변수
  	flag = True
  	for j in range(M): # 0 ~ M - 1
  		if t[i + J] != p[j]:
  			flag = False
  			break
  	# 불일치로 끝난건지, 그냥 끝난건지..
  	# flag = False > break가 걸려서 끝났군
  	if flag:
  		# t[i]에서 패턴을 찾았다.
  
  ```

  - flag 변수 대신 for-else 구문을 활용한다.

```python
t = []
p = []
N, M = len(t), len(p)  
# i: 텍스트의 인덱스, j: 패턴의 인덱스
for i in range(0, N - M + 1):
	# 길이가 M인 패턴을 비교
	for j in range(M): # 0 ~ M - 1
		if t[i + J] != p[j]:
			break
	else:
		break
		# 찾았다.
```

-----------------

- 모든 패턴을 다 찾으려면 

```python
t = []
p = []
N, M = len(t), len(p)  
# i: 텍스트의 인덱스, j: 패턴의 인덱스
i = 0
while i < N - M + 1:
	# 길이가 M인 패턴을 비교
	for j in range(M): # 0 ~ M - 1
		if t[i + J] != p[j]:
			break
	else:
		i = i + M - 1  # 다음라인에서 1 증가하는 걸 고려
	i += 1
```

<img src="README.assets/image-20220222194037148.png" alt="image-20220222194037148" style="zoom:50%;" />















