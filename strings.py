my_string_1 = "trololololol"
my_string_1 = my_string_1.replace("l", "p")
print(my_string_1)
my_string_1 = my_string_1.replace("p", "l")
print(my_string_1)

fname = "paul"
lname = "raynes"
age = 23
fname = fname[0].upper() + fname[1:5]
lname = lname.capitalize()
print(fname)

greet = "Hi, my name is {} {}, and my age is {}.".format(fname, lname, age)
print(greet)
greet2 = f"Hi, my name is {lname}, {fname}, and I am {age} years old."
print(greet2)

print("a", end=", ")
print("b", end=",\t")
print("c")

print("a", "b", "c", sep="\t")

print(greet.count("name"))

print(greet.find("name"))
print(greet.find("a"))
print("greet length = ", len(greet))
fname = "Bobby"
lname = "Clemmons"
greet = "Hi, my name is {} {}, and my age is {}.".format(fname, lname, age)
print(greet)
print("greet length = ", len(greet))
greet3 = "Hi, my name is  , and my age is ."
print("greet3 length = ", len(greet3))
