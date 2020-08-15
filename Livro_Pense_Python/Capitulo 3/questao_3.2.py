def do_twice(f, g):
    f(g)
    f(g)

def do_four(f, g):
    do_twice(f, g)
    do_twice(f, g)

do_twice(print, 'spam')
do_four(print, 'spam')

