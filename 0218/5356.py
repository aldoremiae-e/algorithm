# Null 문자이용!!!!!! '\0'

T = int(input())
for tc in range(1, T+1):
    text = [list('_'*15) for _ in range(5)]
    input_text = [list(input()) for _ in range(5)]
    for i in range(5):
        for j in range(15):
            if j < len(input_text[i]):
                text[i][j] = input_text[i][j]
    print(f'#{tc}', end=' ')
    for j in range(15):
        for i in range(5):
            if text[i][j] == '_':
                continue
            print(text[i][j], end='')
    print()
