from compute.calc import add, subtract, multiply, divide
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Exponentiate")
print("7. Floor Divide")
print("8. Exit")
choice = input("Enter choice (1/2/3/4/5/6/7/8): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
elif choice == '5':
    print(f"{num1} % {num2} = {modulus(num1, num2)}")
elif choice == '6':
    print(f"{num1} ** {num2} = {exponentiate(num1, num2)}")
elif choice == '7':
    print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
elif choice == '8':
    print("Exiting the calculator. Goodbye!")
else:
    print("Invalid input")