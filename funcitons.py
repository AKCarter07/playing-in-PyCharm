def greet():
    print("Hi!")


def annoyed():
    print("je suis annoyed")


def name(lname):
    print("My last name is ", lname)


def change_x(x):
    x += 1
    return x


def add(x, y):
    return x + y


greet()
annoyed()
name("Carter")
print(change_x(1))
print(add(1,2))