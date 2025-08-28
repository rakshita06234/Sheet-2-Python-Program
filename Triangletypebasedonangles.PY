a=(int(input("Enter three angles: ")))
b=(int(input("Enter three angles: ")))
c=(int(input("Enter three angles: ")))
if a + b + c == 180:
    if 90 in (a, b, c):
        print("Right triangle")
    elif any(angle > 90 for angle in (a, b, c)):
        print("Obtuse triangle")
    else:
        print("Acute triangle")
else:
    print("Not a valid triangle")