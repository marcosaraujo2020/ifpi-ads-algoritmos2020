print('-=' * 15)
print('Tabuada')
print('-=' * 15)
def main():
    num = 1
    tabuada(num)
def tabuada(x):
    y = 1
    while y < 11:
        print(f'{x} x {y} = {x * y}')
        y += 1
    print('-=' * 15)
    x += 1
    if x < 11:
        return tabuada(x)
main()
