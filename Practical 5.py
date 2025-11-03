'''n_num = int(input("Enter a number: "))
factorial = 1
for i in range(1, n_num + 1):
    factorial *= i
print(f"The factorial of {n_num} is {factorial}")'''

n_num = int(input("Enter a number: "))
factorial = 1
for i in range(n_num, 0, -1):
    factorial *= i
print(f"The factorial of {n_num} is {factorial}")
