import os
import pickle

scores = []
new_scores = []

def input_score():
    count = 1

    print("[점수 입력]")

    while True:
        n = int(input(f"#{count}? "))
        if n > 0:
            scores.append(n)
            count += 1
        else:
            break

def show_score():
    print("\n[점수 출력]")
    print(f"개인 점수 : ", end='')
    print(*scores, end='')
    
def show_avg():
    global avg
    avg = sum(scores) / len(scores)
    print(f'\n평균 : {avg}')
    return avg

filename = 'score.bin'

def save():
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)
        pickle.dump(avg, file)

def load():
    with open(filename, 'rb') as file:
        s = pickle.load(file)
        a = pickle.load(file)
        return s,a

if os.path.exists(filename):
    print('[파일 읽기]')
    print('\n[점수출력]')
    re_s, re_a = load()
    print('개인 점수:', *re_s)
    print('평균:', re_a)
else: # 처음 실행
    input_score()
    show_score()
    show_avg()
    save()