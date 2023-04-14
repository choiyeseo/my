
def display_multiplication_table():
    for i in range(2, 10):
        for j in range(1, 10):
            if i == 6 and j == 1:
                print()
            print(f'{i} x {j} = {i*j:2d}')


display_multiplication_table()
