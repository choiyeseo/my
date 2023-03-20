# 연습문제 3.7
# 3520원을 동전으로 교환하고자 할 때 가장 적은 개수의 동전을 제안하는 프로그램

def exchange(money):
    n500 = money // 500 # n500 = 7
    money = money % 500 # money = 20원
    print('500원:', n500, '개')
    
    n100 = money // 100 # 0
    money = money % 100 # 20
    print('100원:', n100, '개')
    
    n50 = money // 50 # 0
    money = money % 50 # 20
    print('50원:', n50, '개')
    
    n10 = money // 10 # 2
    money = money % 10 # 0
    print('10원:', n10, '개')


money = int(input('동전으로 교환하고자 하는 금액은? '))
exchange(money)
