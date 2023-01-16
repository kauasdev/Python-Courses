numbers = ("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Eighteen", "Nineteen", "Twenty")
num = int(input("Enter the number between 0 and 20: "))

while True:
    if num < 0 or num > 20:
        print("Invalid number! Try again!")
        num = int(input("Enter the number between 0 and 20: "))
    else:
        break
print(f"\nYou chose number {numbers[num - 1]}\n")