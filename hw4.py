
name = input('Input his/her name: ')
msg1 = ('Hello ' + name + ',')
msg2 = 'Welcome to Seoul.'

if (len(msg1) > len(msg2)):
    nstr = len(msg1)
else:
    nstr = len(msg2)

def rep_char(a, b):
    print(a * b)

def draw_the_line(c):
    rep_char('-', nstr)
    print(msg1)
    print(msg2)
    rep_char('-', nstr)

draw_the_line(name)
