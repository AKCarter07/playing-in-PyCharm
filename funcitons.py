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


print(greet())
greet()
annoyed()
name("Carter")
print(change_x(1))
print(add(1,2))
c = add(4,2)
print(c)
print(add(4,5))  # contains 3  expressions: 4, 5, & add(4,5) == 9 (4th expression: print evals to None)
print(print(c))