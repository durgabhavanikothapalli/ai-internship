

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")

choice = input("Enter choice (1/2/3): ")

if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
else:
    print("Invalid choice")