print('-=' * 15)
print('Tabuada')
print('-=' * 15)
def main():
    num = 1
    tabuada(num)
def tabuada(x):
    for i in range(1, 11):
        print(f'{x} x {i} = {x * i}')
    print('-=' * 15)
    x += 1
    if x < 11:
        return tabuada(x)
main()
