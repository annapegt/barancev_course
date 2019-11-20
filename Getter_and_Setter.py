class Age(object):
    def set_age(self, age_val):
        try:
            age_val = int(age_val)
        except ValueError:
            return
        self.age_val = age_val

    def get_val(self):
        return print(self.age_val)

    def increment_val(self):
        self.age_val = self.age_val + 1


my_age = Age()
my_age.set_age (22)
print(my_age.increment_val())


