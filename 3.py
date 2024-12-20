def gen_yigindi(a,b):
    s=0
    for i in range(a,b, -1):
        s +=i
        yield s
r= gen_yigindi(10,5)
for i in r:
    print(i)