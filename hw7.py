print('[구입]')
shopping_bag = {}
while True:
    item = input('상품명? ')
    if item == '':
        break
    quan = input('수량은? ')
    print(f'장바구니에 {item} {quan}개가 담겼습니다.')
    shopping_bag[item] = quan

print()    
print(f'>>> 장바구니 보기: {shopping_bag}')
print()

print('[검색]')
find = input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{find}은(는) {shopping_bag.get(find)}개 담겨 있습니다.')