def pack_it(**kwargs):
    print(kwargs)
    print(type(kwargs))
pack_it(a = "animal", b = "bear")

def unpack_it(c,d):
    print(c)
    print(d)
kwargs = {"c":"cat","d":"dog"}
unpack_it(**kwargs)