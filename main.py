operator = input("Enter the operator (+, -, *, /): ")
nums1 = float(input("Enter the value of the first number: "))
nums2 = float(input("Enter the value of the second number: "))

if operator == "+":
    result = nums1 + nums2
    print(f"The value after addition is {result}")

elif operator == "-":
    result = nums1 - nums2
    print(f"The value after subtraction is {result}")

elif operator == "*":
    result = nums1 * nums2
    print(f"The value after multiplication is {result}")

elif operator == "/":
    if nums2 != 0:
        result = nums1 / nums2
        print(f"The value after division is {result}")
    else:
        print("Division by zero is not allowed.")

else:
    print("Invalid operator!")
