class Class:
    def __init__(self,start,stop):
        self.start=start -1 # -1 O'zidan boshlashi uchun
        self.stop=stop

    def __iter__(self):
        return self

    def __next__(self):
        self.start -=1
        if self.start > self.stop:
            return self.start
        raise StopIteration

for elem in Class(10,-10):
    print(elem)