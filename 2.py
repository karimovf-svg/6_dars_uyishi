d = [1,2,5,66,7]
d.sort() # Ketma-ketlikda olib beryapti
d_iter=iter(d)
while True:
    try:
        print(next(d_iter))
    except StopIteration:
        break