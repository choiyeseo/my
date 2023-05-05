def buy(lst):
    
    while True:
        print('[구입]')
        item = input('상품명? ')
        if item == '':
            return False
        quan = int(input('수량은? '))
        lst[item] = quan
        print(f'장바구니에 {item} {quan}개가 담겼습니다.\n')

def show(lst):
    print(f'\n\n>>> 장바구니 보기: {lst}\n')    

def find(lst):
    print('[검색]')
    find = input('장바구니에서 확인하고자 하는 상품은? ')
    if find not in lst:
        print(f'장바구니에 {find}은(는) 없습니다.')
    else:
        print(f'{find}는 {lst.get(find)}개 담겨 있습니다.')


shopping_bag = {}

while True:
    if buy(shopping_bag) == False:
        break

show(shopping_bag)
find(shopping_bag)