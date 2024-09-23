print("Input Lengths of the Sides of a Triangle")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x == y == z:
	print("Equilateral Triangle")
elif x == y == z:
	print("Isosceles Triangle")
else:
	print("Scalene Triangle")