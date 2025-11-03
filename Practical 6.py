n_num = int(input("Enter a number: "))
factorial = 1
while n_num > 0:
    factorial *= n_num
    n_num -= 1
print("Factorial is:", factorial)


'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

num = 5
print(f"The factorial of {num} is {factorial(num)}")'''