width = input("Please enter the width of the room: ")
length = input("Please enter the length of the room: ")
unit = input("Please enter the unit of the area (ft or m): ")

area = float(length) * float(width)
print(f"The area of the room is: {area:.4f} [{unit}^2]" )            