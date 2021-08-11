def foo (a_inner):
    print(id(a_inner))
    return a_inner
a_outer = []
foo(a_outer)

print(id(a_outer))

print( a_outer is foo(a_outer) )

