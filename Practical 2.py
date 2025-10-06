stnum = input("Enter a number: ")
ndnum = input("Enter another number: ")
def convert(num):
    try:
        return int(num)
    except ValueError:
        try:
            return float(num)
        except ValueError:
            try:
                return complex(num.replace(' ', ''))
            except ValueError:
                raise ValueError("Input is a string, not a number")
stnum = convert(stnum)
ndnum = convert(ndnum)
operators = ['+', '-', '*', '/', '//', '%', '**', '==', '!=', '>', '<', '>=', '<=']

with open("Python_Lab/Practical_Output 2.txt", "a") as file:
    file.write(f"First number: {stnum}\n")
    file.write(f"Second number: {ndnum}\n")
    for op in operators:
        try:
            result = eval(f"{stnum} {op} {ndnum}")
            file.write(f"{stnum} {op} {ndnum} = {result}\n")
        except ZeroDivisionError:
            print(f"Error: Division by zero for {stnum} {op} {ndnum}")
            file.write(f"Error: Division by zero for {stnum} {op} {ndnum}\n")
        except Exception as e:
            print(f"Error: {e}")
            file.write(f"Error: {e}\n")
