import math
def mysqrt(a):
    x = 3
    while True:
        y = (x + a/x) / 2
        if y == x:
            return x
        x = y
def test_square_root():
    a = 1.0
    print('=' * 90)
    print('a ----- mysqrt ---------------------- math.sqrt(a) ------------ difff')
    while a < 10.0:
        print(a, end='---- ')
        print(mysqrt(a), end='----------')
        print(math.sqrt(a), end='----------')
        print(mysqrt(a) - math.sqrt(a))
        a += 1
    print('=' * 90)
test_square_root()
