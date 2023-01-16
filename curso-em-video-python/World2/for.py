# The for is a loop with a control variable

# for variable in range:
#   code

# for i in range(0,6): #range(start, end - 1)
#     print("Hi")
#     print(i)

# print("="*15)

# for i in range(10, 0, -1):
#     print(i)

num = int(input("Enter the number: "))

for i in range(0, num + 1):
    print(i)
print("End")