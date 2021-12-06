from itertools import count, cycle

def coun():
    for i in count(3):
        if i > 10:
            break
        else:
            print(i)

def cycl():
    my_list = ['ABC', 10.5, None, True, 568]
    c = 0
    for i in cycle(my_list):
        if c > 10:
            break
        print(i)
        c += 1
coun()
cycl()
