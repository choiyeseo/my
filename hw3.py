def get_fixed_price(rate, discounted_price): 
    original_price = discounted_price / (1-rate) # 원래 가격 = 할인된 가격 * rate 
    return original_price

rate = int(input('할인율은? ')) # 20% 입력
rate = rate / 100
discounted_price_a = int(input('A 상품의 할인된 가격은? '))
discounted_price_b = int(input('B 상품의 할인된 가격은? '))

original_price_a = int(get_fixed_price(rate, discounted_price_a))
original_price_b = int(get_fixed_price(rate, discounted_price_b))
print('A 상품의 정가는', original_price_a, '원')
print('B 상품의 정가는', original_price_b, '원')