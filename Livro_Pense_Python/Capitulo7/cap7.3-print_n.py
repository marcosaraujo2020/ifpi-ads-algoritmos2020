def print_n(s, n):
    while n <= 0:
        return
    print(s)
    print_n(s, n-1)
print_n('Hello', 5)
