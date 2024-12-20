def gen_kvadrati():
    n=1
    n *= 1
    print("bajarildi")
    yield n

    n=2
    n *= 2
    print("bajarildi 2")
    yield n

    n=3
    n *= 3
    print("bajarildi 3")
    yield n

    n=4
    n *= 4
    print("bajarildi 4")
    yield n

    n=5
    n *= 5
    print("bajarildi 5")
    yield n


result = gen_kvadrati()
# Sikl bilan olish

for i in result:
    print(i)