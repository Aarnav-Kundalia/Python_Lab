n_num = int(input("Enter a number: "))
factorial = 1
for i in range(1, n_num + 1):
    factorial *= i
print(f"The factorial of {n_num} is {factorial}")

n_num = int(input("Enter a number: "))
for _ in range(n_num):
    print(f"Current value: {n_num}")
    n_num -= 1
print(f"Final value: {n_num}")