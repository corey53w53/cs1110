class Parent(object):
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

    def add_one(self):
        self.age += 1


class Child(Parent):
    def __init__(self, age, gender):
        super().__init__(age, gender)

    def __str__(self):
        return f'I am {self.age} years old and am a {self.gender}'


me = Child(4, "boy")
print(me)