'''
1. 시작정점 결정 후 방문
2. 정점 v 에 인접한 정점 중
    2-1 방문하지않은 정점 w가 있으면,
        정점 v를 스택에 push, 정점 w를 방문
        w를 v로 바꾸고 2 반복
    2-2 방문하지 않은 정점이 없으면,
        탐색의 방향을 바꾸기 위해 스택을 pop하여 받고
        가장 마지막 방문 정점을 v로 하여 다시 2를 반복
3. 스택이 공백이 될때까지 2 반복복'''
visited = [] #방문 유무
stack = []

def DFS(v):
    if visited[v]