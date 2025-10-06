n_num = int(input("Enter a number: "))
factorial = 1
while n_num > 0:
    factorial *= n_num
    n_num -= 1
print("Factorial is:", factorial)