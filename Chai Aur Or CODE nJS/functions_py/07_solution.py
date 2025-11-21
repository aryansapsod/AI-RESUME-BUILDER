# args

def fun(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum(args)

print(fun(1,2))
print(fun(1,2,3))