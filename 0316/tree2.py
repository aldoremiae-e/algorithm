'''
4
2 1 2 4 4 3 4 5
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

# 자식의 번호를 인덱스로, 부모번호를 저장
par = [0] * (V+1) # [0, 2, 0, 4, 2, 4] ( 1, 4 인덱스 2를 부모로가지고, 3, 5 인덱스는 4를 부모로 가짐)
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    par[v2] = v1

# root (최상단) 찾기
root = 0
for i in range(1, V+1):
    if par[i] == 0: # 부모를 안가지고 있는게 부모겠지
        root = i
        break
# 조상찾기
c = 5 #(정점 c 상단의 이어지는 조상정점들을 다 찾는 방식
anc = []
while par[c]!= 0:
    anc.append(par[c])
    c = par[c]
print(*anc)