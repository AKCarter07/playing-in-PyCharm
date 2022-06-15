print("start")

i = 0
while i < 100:
    i += 1
    print(i, end=" ")
    if i == 25 or i == 50 or i == 75 or i == 100:
        print("")

print(type(range(1, 101)))

for num in range(1,101):
    print(num, end = " ")
    if num == 25 or num == 50 or num == 75 or num == 100:
        print("")

for num in range(0,101,3):
    print(num, end=" ")

print("\n")
for _ in range(3):  # by convention, use _ if iterator variable will not be used
    print("nyan")

for num in range(10,0,-1):
    print(num, end=" ")