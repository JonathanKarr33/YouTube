def pack_it(*args):
    print(args)
    print(type(args))
a = "A"
b = "B"
c = "c"
pack_it(a,b,c)

def unpack_it(x,y):
    print(x)
    print(y)
args = (5,10)
unpack_it(*args)