# 삽입할 자료를 매개변수로
def push(item):
    # top증가 -> top위치에 자료를 넣음 : 리스트의 마지막 원소에 추가하는 append메서드 활용
    # python의 list는 크기의 제한이 없기 때문에 overflow 문제 해결    s.append(item)
def pop():
    # top이 -1이면 스택에 자료가 없는 상태
    # 리스트의 크기를 len을 통해 알 수 있어 top의 변수 필요 없음
    if len(s)==0:
        #underfloor
        return
    # stack의 마지막 값을 반환
    # top위치에 있는 값을 리턴함 -> 리스트의 마지막 값을 삭제하고 뽑아오는 pop 메서드 활용
    else:
        return s.pop(-1)
s = []
push(1)
push(2)
push(3)
print("pop item =>", pop())
print("pop item =>", pop())
print("pop item =>", pop())