x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x > y and x > z:
    print("Maximum is:", x)
elif y > z:
    print("Maximum is:", y)
else:
    print("Maximum is:", z)
