print("start\n")

print(3 == 3)  # True
print("dog" != "cat")  # True
print("dog" != "dog")  # False
print(3 == 3.0)  # True
print(3 == 3.1)  # False
print(3 == int(3.1))  # True
# print(3 is 3.0)   # False
# print(3 is 5)  # False
# print(3 is 3)  # True
# print("hi" is "Hi")  # False


myString = "hi"
print(myString is "hi")  # True
# myString = input("input a string: ")
# print(myString is "hi")  # will show False, even if "hi" is typed b/c myString will not point to
                         # the "hi" in the string pool
print(myString == "hi")  # True if "hi" is typed

x = 3
# x =int(input("Enter a number: "))
print(x is 3)  # True when x = 3

print(id("hi"))