class Parent(object):
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

    def add_one(self):
        self.age += 1

    def __str__(self):
        return "I am parent"


class Child(Parent):
    def __init__(self, age, gender):
        super(Child, self).__init__(age, gender)

    def __str__(self):
        return f'I am {self.age} years old and am a {self.gender}'


class Grandchild(Child):
    def __init__(self, age, gender, cute):
        super(Grandchild, self).__init__(age, gender)
        self.cute = cute
        pass

    def __str__(self):
        return super(Child, self).__str__()


me = Child(4, "boy")
print(me)
m = Grandchild(3, "boy", True)
print(m)
