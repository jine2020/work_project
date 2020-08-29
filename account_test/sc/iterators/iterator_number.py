import random

class IteratorNumber(object):
    #迭代器
    def __init__(self,long):
        self.start=random.randint(1,long)
        self.long=10

    def __iter__(self):
        return self

    def __next__(self):
        if self.start>self.long:
            raise StopIteration
        else:
            return self.start

if __name__ == '__main__':
    pass