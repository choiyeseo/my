num = input('세 자리 정수 입력: ') 
n1 = num[0] 
n2 = num[1] 
n3 = num[2] 


def read_single_digit(n):
    if n == '0':
        return '영'
    if n == '1':
        return '일'
    if n == '2':
        return '이'
    if n == '3':
        return '삼'
    if n == '4':
        return '사'
    if n == '5':
        return '오'
    if n == '6':
        return '육'
    if n == '7':
        return '칠'
    if n == '8':
        return '팔'
    if n == '9':
        return '구'
    
def read_number(m1, m2, m3):
    print(m1, m2, m3)

x = read_single_digit(n1)
y = read_single_digit(n2)
z = read_single_digit(n3)
read_number(x,y,z)
