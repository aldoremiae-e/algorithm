'''
4
1 2 1 3 3 4 3 5
'''
# 전위순회 VLR
def preorder(v):
    if v: # 0번 정점이 없어서 0번은 자식이 없는 경우를 표시
        print(v)
        preorder(ch1[v])
        preorder(ch2[v])
# 중위순회 LVR
def inorder(v):
    if v:
        inorder(ch1[v])
        print(v)
        inorder(ch2[v])
# 후위순회 LRV
def postorder(v):
    if v:
        postorder(ch1[v])
        postorder(ch2[v])
        print(v)

E = int(input())    # 노드 수
arr = list(map(int, input().split()))
V = E + 1           # 정점 수

# 부모를 인덱스로 자식번호 저장
ch1 = [0]*(V+1)     # 왼쪽
ch2 = [0]*(V+1)     # 오른쪽
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    if ch1[v1] == 0: # 아직 자식이 없는 경우
        ch1[v1] = v2
    else: # 자식이 있는 경우
        ch2[v1] = v2
#preorder(1) #12345
#inorder(1) #21435
#postorder(1) #24531