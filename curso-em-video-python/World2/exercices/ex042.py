lines = []
for i in range(3):
    lines.append(float(input("What's the length of the line: ")))

side_a, side_b, side_c = lines

if side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_a + side_b:
    print("Lines can form a triangles")

    if side_a == side_b == side_c:
        print("Equilateral triangle")
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print("Isosceles Triangle")
    elif side_a != side_b != side_c != side_a:
        print("Scalene Triangle")

else:
    print("Lines can't form a triangle")