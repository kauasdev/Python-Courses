lines = []
for i in range(3):
    lines.append(float(input("What's the length of the line: ")))

side_a, side_b, side_c = lines

if side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_a + side_b:
    print("Lines can form a triangles")
else:
    print("Lines can't form a triangle")