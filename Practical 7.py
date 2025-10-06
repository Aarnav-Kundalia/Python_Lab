a = input("Enter base number: ")
b = input("Enter power number: ")
try:
    for i in range(1, int(b) + 1):
        int(a) *= int(a)
    print(f"The power of {a} to {b} is {a}")
except ValueError:
    print("Invalid input. Please enter numeric values.")