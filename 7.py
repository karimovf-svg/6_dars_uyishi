class Class:
    def __init__(self,low,high):
        self.current=low -1 # -1 O'zidan boshlashi uchun
        self.high=high

    def __iter__(self):
        return self

    def __next__(self):
        self.current +=1
        if self.current < self.high:
            return self.current
        raise StopIteration

for elem in Class(1,10):
    print(elem)