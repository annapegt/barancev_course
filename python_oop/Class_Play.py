import random


class Class_Play(object):
    def to_do(self):
        self.rand_new = random.randint(1,10)


new_inst = Class_Play()
new_inst.to_do()
print(new_inst.rand_new)