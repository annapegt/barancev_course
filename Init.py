class Init():
    def __init__(self, value):
        try:
            val = int(value)
        except ValueError:
            value = 0
        self.val = value

    def increment_val(self):
        self.val = self.val + 1

my_int = Init(2)
my_int.increment_val()
print (my_int.val)