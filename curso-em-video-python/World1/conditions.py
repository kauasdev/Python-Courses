# if condition:
#   This block will be executed if the condition is True
# else:
#   This block will be executed if the condition is False

# Example
age = int(input("How old are you: "))

if age < 18:
    print("You aren't an adult")
else:
    print("You're an adult")

# OR 

print("You aren't an adult" if age < 18 else "You're an adult")