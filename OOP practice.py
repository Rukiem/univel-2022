def hello():
    print("hi")
# print(type(hello))

class Dog:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def set_name(self, value):
        self.name = value

    def set_age(self, value):
        self.age = value

# dog1 = Dog("Tim", 12)
# dog1.set_age(15)
# print(dog1.get_age())


